#!/usr/bin/env python3
#
# This is an example script to upgrade a set of devices by their tags.
# It iterates through each device to detect if an upgrade is available
# before running the upgrade. The in-progress upgrade logs are printed out
# as they are returned via the progress API.
#
# Example run:
#   PYTHONPATH=py PASSWORD=controllerpassword python3 ./example-upgrade-devices.py {tags}
#
# where {tags} is a comma-separated list of tags
#

import base64
import json
import os
import sys
import time

from pfapi import Client, AuthenticatedClient

#
# Controller APIs
#
from pfapi.models import *
from pfapi.api.login import login, refresh_access_token
from pfapi.types import Response

from pfapi.api.mim import get_controlled_devices
from pfapi.api.system import get_status, get_system_update_info, perform_system_update, get_system_update_progress

###########################################


tags = ""
if len(sys.argv) < 2:
	print("comma-separated list of tags not provided")
	#sys.exit(1)
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

# Login to controller. Username and password must be base64 encoded.
# For security, the credentials should be loaded from a protected file
# on the system or entered interactively (using other python libraries)
client = Client(base_url=CONTROLLER_URL+"/api",
				verify_ssl=False,
				headers={"Content-Type": "application/json"})

username = base64.b64encode(USER.encode('utf-8')).decode('utf-8')
password = base64.b64encode(PASSWORD.encode('utf-8')).decode('utf-8')
loginCred = LoginCredentials(username=username, password=password)
resp = login.sync(client=client, body=loginCred)

# Successful login will return a token in LoginReponse; keep it to create Authenticated client.
if isinstance(resp, LoginResponse):
	token = resp.token
	sessInfo = json.loads(base64.b64decode(token.split(".")[1].encode('utf-8') + b'==').decode('utf-8'))
	expires = time.localtime(sessInfo['exp'])

	# Print expiration of access token, must call refresh_access_token to continue
	# to access API.
	print("Token expires at:", time.strftime("%a, %d %b %Y %H:%M:%S +0000", expires))

elif isinstance(resp, Error):
	print("login failed:", resp)
	sys.exit(1)

# Cookie jar contains the 24-hour refresh token, which is used to refresh
# the session access token (via API: /login/refresh)
cookies = client.get_httpx_client().cookies

# Create an authenticated client, which will send the bearer (access) token for
# all API requests to the controller
client = AuthenticatedClient(base_url=CONTROLLER_URL+"/api",
				verify_ssl=False,
				headers={"Content-Type": "application/json"},
				cookies=cookies,
				token=token)

# Get list of devices by their tags.
# Multiple tags can be supplied using comma separation.
taggedDevicesResult = get_controlled_devices.sync(client=client, tags=tags)

if taggedDevicesResult.devices is None or len(taggedDevicesResult.devices) == 0:
	print("No devices with the specified tag(s) found")
	sys.exit(1)

print("")
print(f"{'NAME':<{30}}{'DEVICE-ID':<{40}}")
for dev in taggedDevicesResult.devices:
	nameCol = (dev.name[:30 - 3] + "...") if len(dev.name) > 30 else dev.name
	devidCol = (dev.device_id[:50 - 3] + "...") if len(dev.device_id) > 50 else dev.device_id

	print(f"{nameCol:<{30}}{devidCol:<{50}}")


start = time.time()

# return True if a new refresh token was requested
def refreshToken(client):
	global start
	now = time.time()
	if now - start > 240:
		# renew the session token with the controller after 4 minutes
		refreshResp = refresh_access_token.sync(client=client, body=RefreshTokenParam(username=username))
		if isinstance(refreshResp, LoginResponse):
			print("Refresh access token response:", resp.token)
			client.token = resp.token
		else:
			print("Token refresh failed:", refreshResp)
			sys.exit(1)

		start = now
		return True
	return False

def newDevApiClient(client, device_id):
	# Set the base path for each device API. It has the format:
	#   /api/device/{device-type}/{device-id}/api
	return AuthenticatedClient(base_url=CONTROLLER_URL+"/api/device/pfsense/{}/api".format(device_id),
	                           verify_ssl=False,
	                           headers={"Content-Type": "application/json"},
	                           cookies=cookies,
	                           token=client.token)

print("")
print("Checking each device's upgradability")
for device in taggedDevicesResult.devices:
	if device.state != "online":
		# Skip offline device
		print("device {} is offline, skipping...".format(device.name))
		continue

	#
	# Create a per-device API client instance and use the same
	# cookie jar and session token.
	#
	refreshToken(client)
	devApi = newDevApiClient(client, device.device_id)

	# Print device information
	try:
		sysStatus = get_status.sync(client=devApi.with_timeout(10))
	except Exception as e:
		print("get_status for device failed with exception:", e)
		continue

	print("")
	for v in sysStatus.status.to_dict().items():
		if v[0] in ("host", "osver", "machine"):
			val = v[1]
			if isinstance(val, str):
				val = val.replace('\n', '')
			print("\t{:<10} {}".format(v[0], val))

	print("")
	print("Checking available system update(s) for {}".format(device.name))
	info = get_system_update_info.sync(client=devApi)
	try:
		if info.update_messages is not None and len(info.update_messages) > 0:
			print("Repo update messages:", '\n'.join(info.update_messages))
			print("")
	except Exception as e:
		pass

	try:
		if info.latest_base_system == "" or info.curr_base_system == "" or info.latest_base_system == info.curr_base_system:
			print("Skipping device {} ({}), no new version available".format(device.name, device.address))
			print("")
			continue
	except Exception as e:
		print("Skipping device {} ({}), due to exception".format(device.name, device.address), e)
		continue

	print("Upgrading device {} ({}) to {}...".format(device.name, device.address, info.latest_base_system))
	upgradeOpt = SystemUpdateOptions(firmware_branch=info.firmware_branch)

	result = perform_system_update.sync(client=devApi, body=upgradeOpt)
	print("perform_system_update request returned", result)

	print("\nUpgrade progress:")

	# query upgrade progress until it has completed or fails
	lastMsgs = ""
	progressStarted = False
	while True:
		# This can take a long time to complete so always check if the refresh token needs to be renewed.
		# Create a new devApi client if a new refresh token was obtained.
		if refreshToken(client):
			devApi = newDevApiClient(client, device.device_id)

		progress = get_system_update_progress.sync(client=devApi)
		if not progressStarted and progress.completed > 0:
			progressStarted = True

		if progressStarted and progress.completed == 0:
			# Completion would reset to 0 if the log file cycles or the
			# system has rebooted. Mark as a completed upgrade.
			print("\n--- upgrade completed ---")
			break

		if progress.messages is None:
			if progressStarted:
				break
			# progress messages might not be available if upgrade has not logged anything
			continue
		try:
			msgsAll = '\n'.join(progress.messages)
			if len(msgsAll) > len(lastMsgs):
				print(msgsAll[len(lastMsgs):], end="")

				# print the current completed percent (guessed)
				#print(" {{completed {}%}} ".format(progress.completed), end="")
			lastMsgs = msgsAll
			time.sleep(1.0)
		except Exception as e:
			print("Exception", e)
			print("Progress returned", progress)
			break

		if progress.completed == 100:
			print("\n--- upgrade completed ---")
			break

	print("")
