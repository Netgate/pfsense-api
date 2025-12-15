# Common set of helper functions for pfSense API requests.

import asyncio
import base64
import httpx
import json
import os
import sys
import time
import threading

if not os.getenv('PYTHONPATH') and os.path.exists('py'):
	sys.path.append('py')

from pfapi import Client, AuthenticatedClient

#
# Controller APIs
#
from pfapi.models import *
from pfapi.api.login import login, refresh_access_token

from pfapi.api.mim import get_controlled_devices
from pfapi.api.system import get_status

# =====================================================

_CONTROLLER_URL = os.getenv('CONTROLLER_URL', 'https://10.100.0.38:8443')
if not _CONTROLLER_URL.startswith('http'):
	_CONTROLLER_URL = 'https://' + _CONTROLLER_URL

class Settings:
	pass

def get_settings():
	'''
	Returns the settings of the script. Combines both
	environment variables and configuration file options.
	'''

	v = Settings()

	# scan through sys.argv to see if there is a -c <config file> flag
	v.config_file = ''
	v.TAGS = ''

	tags = []
	cfg_file_idx = 0
	for i, opt in enumerate(sys.argv):
		if opt == '-c' or opt == '--config':
			if i < len(sys.argv)-1:
				v.config_file = sys.argv[i+1]
				cfg_file_idx = i+1
		elif i > cfg_file_idx:
			# all other options are tags
			tags.append(opt)

	if v.config_file:
		# load options from file; key-value pairs
		try:
			with open(v.config_file, 'r') as f:
				for line in f:
					if '=' in line:
						k, val = line.split('=', 1)
						if k.strip()[0] != '#':
							setattr(v, k.strip(), val.strip())
		except Exception as e:
			print("error in confg file parsing:", e)

	if len(tags) > 0:
		v.TAGS = ','.join(tags)

	# URL of controller and username password to log into it.
	if not hasattr(v, 'CONTROLLER_URL'):
		v.CONTROLLER_URL = _CONTROLLER_URL

	if not hasattr(v, 'USER'):
		v.USER = 'admin'

	# Controller password.
	envpasswd = os.getenv("PASSWORD")
	if envpasswd:
		v.PASSWORD = envpasswd
	elif not hasattr(v, 'PASSWORD'):
		print("PASSWORD environment variable or config not set")
		sys.exit(1)

	return v

class RequestClient:
	'''
	Representation of a single request, which tracks the status of its API calls.
	There should only be a single parent API client, which deals with
	authentication and maintaining authorization tokens.
	'''

	def __init__(self, parent=None, controller_url=_CONTROLLER_URL):
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


def get_online_devices(sessionClient, tags):
	'''
	Get list of devices by their tags.
	Multiple tags can be supplied using comma separation.

	:param RequestClient sessionClient: the main API client
	:param str tags: comma separated list of device tags
	:return [RequestClient]: list of online device clients
	'''

	taggedDevicesResult = sessionClient.call(get_controlled_devices.sync, tags=tags)

	if taggedDevicesResult.devices is None or len(taggedDevicesResult.devices) == 0:
		raise Exception(f"No devices with the specified tag(s) {tags} found")

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

		# stash the device name and details
		devApi.device_name = device.name
		devApi.device = device

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

	return online_devs