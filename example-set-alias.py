#!/usr/bin/env python3
#
# This is an example script of how to push an alias to all online devices
# or those of a specific tag. The requests are done in batches of
# concurrently and results are reported in the final output.
#
# Example run:
#   PYTHONPATH=py PASSWORD=controllerpassword python3 ./example-set-aliases.py {tags}
#
# where {tags} is a comma-separated list of tags
#

import asyncio
import base64
import httpx
import json
import os
import sys
import time
import threading

from pfapi import Client, AuthenticatedClient

#
# Controller APIs
#
from pfapi.models import *
from pfapi.api.login import login, refresh_access_token
from pfapi.types import Response

from pfapi.api.mim import get_controlled_devices
from pfapi.api.system import get_status
from pfapi.api.aliases import firewall_get_aliases, firewall_add_alias

###########################################

tags = ""
if len(sys.argv) < 2:
	print("Comma-separated list of tags not provided, applying to all devices")
else:
	tags = sys.argv[1]


# URL of controller and username password to log into it.
CONTROLLER_URL = 'https://10.100.0.38:8443'
USER = 'admin'

# Controller password.
PASSWORD = os.getenv("PASSWORD")
if not PASSWORD:
	print("PASSWORD environment variable not set")
	sys.exit(1)


class RequestClient:
	'''
	Representation of a single request, which tracks the status of its API calls.
	There should only be a single parent API client, which deals with
	authentication and maintaining authorization tokens.
	'''

	def __init__(self, parent=None, controller_url=CONTROLLER_URL):
		'''
		RequestClient constructor.

		:param RequestClient parent: an instance of the parent request
		       client. If this is the main client, then specify None.
		'''
		self.parent = parent
		self.controller_url = controller_url
		self.username = ""

		self.client = None
		self.start = None
		self.token = None
		self.sessInfo = None
		self.expires = None
		self.device_id = ""

		self.children = []

	def login(self, username, password):
		'''
		Log into the controller.

		:param str username: login username.
		:param str password: user's password.
		:return: True if login succeeds.
		'''

		if self.token:
			# No overlapping logins
			print("session already in progress; create a new instance if wanting to login")
			return False

		# Username and password must be base64 encoded.
		# For security, the credentials should be loaded from a protected file
		# on the system or entered interactively (using other python libraries)
		client = Client(base_url=self.controller_url+"/api",
						verify_ssl=False,
						headers={"Content-Type": "application/json"},
						timeout=httpx.Timeout(40, connect=10))

		username = base64.b64encode(username.encode('utf-8')).decode('utf-8')
		password = base64.b64encode(password.encode('utf-8')).decode('utf-8')
		loginCred = LoginCredentials(username=username, password=password)

		print("Logging in...")
		resp = login.sync(client=client, body=loginCred)

		self.username = username

		# Successful login will return a token in LoginReponse
		if isinstance(resp, LoginResponse):
			# Retain all login tokens and session information
			self.token = resp.token
			self.sessInfo = json.loads(base64.b64decode(self.token.split(".")[1].encode('utf-8') + b'==').decode('utf-8'))
			self.expires = time.localtime(self.sessInfo['exp'])
			self.start = time.time()

			# Print expiration of access token, must call refresh_access_token to continue
			# to access API.
			print("Token expires at:", time.strftime("%a, %d %b %Y %H:%M:%S +0000", self.expires))

			# Cookie jar contains the 24-hour refresh token, which is used to refresh
			# the session access token (via API: /login/refresh)
			self.cookies = client.get_httpx_client().cookies

			# Create an authenticated client, which will send the bearer (access) token for
			# all API requests to the controller
			self.client = AuthenticatedClient(base_url=self.controller_url+"/api",
					verify_ssl=False,
					headers={"Content-Type": "application/json"},
					cookies=self.cookies,
					token=self.token)

			# Periodically trigger session token refresh
			self.refreshTimer = threading.Timer(15, self.__refreshToken)
			self.refreshTimer.start()

			return True

		elif isinstance(resp, Error):
			print("login failed:", resp)
			return False

	def __refreshToken(self):
		'''
		Performs a renewal of the session's refresh token, if required,
		and returns True if it was done.
		'''
		if self.parent:
			# Only the parent does the session refreshing
			return self.parent.refreshToken()

		now = time.time()
		if now - self.start > 240:
			# renew the session token with the controller after 4 minutes
			print("*** refreshing session token")
			refreshResp = refresh_access_token.sync(client=self.client, body=RefreshTokenParam(username=self.username))
			if isinstance(refreshResp, LoginResponse):
				print("Refresh access token response:", refreshResp.token)
				self.client.token = refreshResp.token

				# update all children tokens
				for child in self.children:
					child.client.token = self.client.token
			else:
				print("Token refresh failed:", refreshResp)
				sys.exit(1)

			self.start = now
			return True
		return False

	def stop(self):
		if self.refreshTimer:
			self.refreshTimer.cancel()

	def createDeviceApiChild(self, device_id, timeout=120):
		'''
		Create a child instance of this RequestClient for the specified device_id.

		:param str device_id: identity of the device to action work with
		'''

		if self.token is None:
			print("sesssion not established, cannot create child")
			return None

		# Set the base path for each device API. It has the format:
		#   /api/device/{device-type}/{device-id}/api
		child_client = AuthenticatedClient(base_url=self.controller_url+"/api/device/pfsense/{}/api".format(device_id),
						verify_ssl=False,
						headers={"Content-Type": "application/json"},
						cookies=self.cookies,
						token=self.token)
		child = RequestClient(parent=self)
		child.cookies = self.cookies
		child.token = self.token
		child.client = child_client
		child.client.with_timeout(httpx.Timeout(timeout, connect=20))
		child.device_id = device_id

		self.children.append(child)
		return child

	def clone(self, timeout=30):
		'''
		Create a clone instance of this client, but don't add it to the parent's
		set of children. This is intended for short-lived, one-shot clients.

		:param int timeout: set the timeout of an API call
		'''
		if self.device_id == "":
			client = AuthenticatedClient(base_url=self.controller_url+"/api",
					verify_ssl=False,
					headers={"Content-Type": "application/json"},
					cookies=self.cookies,
					token=self.token)
		else:
			client = AuthenticatedClient(base_url=self.controller_url+"/api/device/pfsense/{}/api".format(self.device_id),
						verify_ssl=False,
						headers={"Content-Type": "application/json"},
						cookies=self.cookies,
						token=self.token)

		client.with_timeout(httpx.Timeout(timeout, connect=20))

		clone = RequestClient()
		clone.client = client

		return clone

	def call(self, func, **kwargs):
		'''
		Call an API function with the specified arguments. The API client
		is applied as an argument to the function.
		'''
		if not "client" in kwargs:
			kwargs["client"] = self.client
		return func(**kwargs)

	def call_async(self, callback, func, **kwargs):
		'''
		Run an async runction and call the callback function with the result.
		'''
		if not "client" in kwargs:
			kwargs["client"] = self.client

		async def async_task(func, kwargs):
			result = await func(**kwargs)
			callback(result)

		asyncio.run(async_task(func, kwargs))


# Create a session client, which is used as the parent to all the per-device API clients.
sessionClient = RequestClient(controller_url=CONTROLLER_URL)

if not sessionClient.login(USER, PASSWORD):
	print("Login failed... quitting")
	sys.exit(1)

# Get list of devices by their tags.
# Multiple tags can be supplied using comma separation.
taggedDevicesResult = sessionClient.call(get_controlled_devices.sync, tags=tags)

if taggedDevicesResult.devices is None or len(taggedDevicesResult.devices) == 0:
	print("No devices with the specified tag(s) found")
	sys.exit(1)

print("")
print(f"{'NAME':<{35}} {'DEVICE-ID':<{50}} STATE")
for dev in taggedDevicesResult.devices:
	nameCol = (dev.name[:30 - 3] + "...") if len(dev.name) > 30 else dev.name
	devidCol = (dev.device_id[:50 - 3] + "...") if len(dev.device_id) > 50 else dev.device_id
	stateCol = dev.state

	print(f"{nameCol:<{35}} {devidCol:<{50}} {stateCol}")

print("")
online_devs = []
for device in taggedDevicesResult.devices:
	print("Device:", device.name, "state:", device.state)

	if device.state != "online":
		# Skip offline device
		print("device {} is offline, skipping...".format(device.name))
		continue

	#
	# Create a per-device API client instance, to interface with the device
	#
	devApi = sessionClient.createDeviceApiChild(device.device_id)
	if devApi is None:
		print("Failed to create child API instance... quitting")
		sys.exit(1)

	# stash the device name
	devApi.device_name = device.name

	# Print device information. Use a clone of the device client
	# so that a custom timeout can be used.
	try:
		print("=======================================")
		clonedClient = devApi.clone(timeout=10)
		sysStatus = clonedClient.call(get_status.sync)
	except Exception as e:
		print("get_status for device failed with exception:", e)
		continue

	for v in sysStatus.status.to_dict().items():
		if v[0] in ("host", "osver", "machine"):
			val = v[1]
			if isinstance(val, str):
				val = val.replace('\n', '')
			print("\t{:<10} {}".format(v[0], val))
	print("")


	online_devs.append(devApi)

# -------------- example async functions for setting alias on the devices --------------

async def set_device_alias(dev, new_alias):
	'''
	Example of how to call the API asynchronously to get
	the device's current set of aliases and add the new alias if it
	doesn't exit.

	:param RequestClient dev: device API client
	:param pfapi.api.aliases.FWAliasReq new_alias: new alias value
	:return: a message from the completion of the request
	'''

	start = time.time()
	result = await firewall_get_aliases.asyncio(client=dev.client)
	if isinstance(result, Error):
		return f"{dev.device_id} - ERROR Failed to get aliases for device => {result}"

	# check that alias is not a system alias
	for alias in result.system_aliases:
		if alias.name.lower() == new_alias.name.lower():
			return f"{dev.device_id} - ERROR alias is a system alias on device"

	# check alias doesn't exist
	for alias in result.aliases:
		if alias.name.lower() == new_alias.name.lower():
			return f"{dev.device_id} - device already has alias"

	result = await firewall_add_alias.asyncio(client=dev.client, body=new_alias)
	if isinstance(result, Error):
		return f"{dev.device_id} - ERROR failed to set alias on device {dev.device_id}"

	end = time.time()
	return f"{dev.device_id} - successfully set alias on device. Duration: {round(end-start, 3)}s"


async def batch_alias_req(devs):
	'''
	Batch alias requests to the list of device clients

	:param list[RequestClient] devs: a list of device request clients
	'''

	print("\nSending requests to:")
	print('\n'.join(['\t- '+ d.device_id + '    ' + d.device_name for d in devs]))

	# Construct the new alias payload.
	# Host aliases take a list of targets, defining the addreses.
	targets = [
		FWTarget(name="1.2.3.4", descr="host-ipv4"),
		FWTarget(name="f3::1", descr="host-ipv6")
	]
	newAlias = FWAliasReq(name="mytestalias", type_=FWAliasReqType(value="host"), targets=targets)

	# Bulk request send, and wait for all of them to complete with asyncio.gather()
	tasks = []
	for dev in devs:
		tasks.append(set_device_alias(dev, newAlias))

	results = await asyncio.gather(*tasks)

	print("\nResults:")
	for result in results:
	   print(f"\t- {result}")


# Bulk set-alias request to the online devices.
print("\nCommencing set-alias on devices:")

# Work in blocks of N_DEVICES (10) devices so
# that it's lighter on the controller and easier
# to track progress.
N_DEVICES=10
for i in range(0, len(online_devs), N_DEVICES):
	asyncio.run(batch_alias_req(online_devs[i:i+N_DEVICES]))

# Stop the refresh timer to exit, otherwise it will wait until the timer event happens
sessionClient.stop()