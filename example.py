#!/usr/bin/env python3
#
# Example script to use pfapi. To run this:
#   PYTHONPATH=py PASSWORD=secret ./example.py
#
# where PYTHONPATH is the parent directory containing the pfapi package
#       PASSWORD is the admin password on the controller
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

#
# Per-device api
#
from pfapi.api.system import get_status, get_system_update_info
from pfapi.api.aliases import firewall_get_aliases

###########################################

CONTROLLER_URL = "https://10.100.0.38:8443"
USER = "admin"
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

# Successful login will return a token in LoginReponse; keep it to
# create Authenticated client.
if isinstance(resp, LoginResponse):
	print("Response token received from controller:", resp.token)
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

# Example to refresh the session access token.
# This step needs to be carried out before the session access token expires so
# that the client can continue to make API requests without reauthenticating.
time.sleep(2)
resp = refresh_access_token.sync(client=client, body=RefreshTokenParam(username=username))
if isinstance(resp, LoginResponse):
	print("Refresh access token response:", resp.token)
	token = resp.token
	client.token = token
elif isinstance(resp, Error):
	print("login failed:", resp)
	sys.exit(1)


# Eample API interfacing:
#   Query the controller for the of managed devices.
#   For each device, get its system update information
resp = get_controlled_devices.sync(client=client)
for device in resp.devices:
	print("=============================================================")
	print(device.name, "\tState:", device.state,"\tAlias:", device.alias, "\tTags:", device.tags, "\tVPN address:", device.auth.vpn_address)
	if device.state != "online":
		# Skip querying offline device
		print("device is offline, skipping...")
		continue

	#
	# Create a per-device API client instance and use the same
	# cookie jar and session token.
	#
	# Set the base path for each device API. It has the format:
	#   /api/device/{device-type}/{device-id}/api
	#

	devApi = AuthenticatedClient(base_url=CONTROLLER_URL+"/api/device/pfsense/{}/api".format(device.device_id),
				verify_ssl=False,
				headers={"Content-Type": "application/json"},
				cookies=cookies,
				token=token)

	sysStatus = get_status.sync(client=devApi)
	for v in sysStatus.status.to_dict().items():
		val = v[1]
		if isinstance(val, str):
			val = val.replace('\n', '')
		print("\t{:<10} {}".format(v[0], val))

	info = get_system_update_info.sync(client=devApi)
	print("Update info: base={}, current={}, status={}".format(info.latest_base_system, info.curr_base_system, info.status_message))

	# Get firewall aliases from device
	aliasResp = firewall_get_aliases.sync(client=devApi)
	print("Aliases:")
	for item in aliasResp.to_dict()["aliases"]:
		print("\t* {}: descr='{}', address={}, targets={}".format(item["name"], item["descr"], item["address"], item["targets"]))
