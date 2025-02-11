#!/usr/bin/env python3 
#
# This is an example script to activate the controller on pfSense devices
# (using SSH) and register them to the controller (using the MIM APIs).
#
# The details about each pfSense device are retrieved via SSH.
# If access to the pfSense device(s) require an SSH password, then set it in
# the SSHPASS environment variable.
# SSH should use authorized_keys rather than passwords.
#
# Requires: Python Paramiko for SSH sessions
#
# Example run:
#   PYTHONPATH=py SSHPASS=sshsecret PASSWORD=controllerpassword python3 ./example-add-devices.py

import base64
import json
import os
import subprocess
import sys
import time

import paramiko

from pfapi import Client, AuthenticatedClient

#
# Controller APIs
#
from pfapi.models import *
from pfapi.api.login import login, refresh_access_token
from pfapi.types import Response

from pfapi.api.mim import get_mim_controller_summary, add_controlled_device

###########################################


# URL of controller and username password to log into it.
CONTROLLER_URL = 'https://10.100.0.38:8443'
USER = 'admin'

# Controller password.
PASSWORD = os.getenv("PASSWORD")
if not PASSWORD:
	print("PASSWORD environment variable not set")
	sys.exit(1)

# SSH account to connect to pfSense device. If SSHPASS environment variable is set, then
# that is the password to use.
SSHUSER = 'admin'
SSHPASS = os.getenv("SSHPASS")

# Set the list of pfsense device addresses that can be connected to via SSH here:
pfsense_addresses = [
		"192.168.101.160",
	]


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

# Get controller information to register to pfsense devices

summaryResp = get_mim_controller_summary.sync(client=client)
controller_info = json.dumps(summaryResp.to_dict())
print("CONTROLLER_SUMMARY:", controller_info)

controller_info_escaped = controller_info.replace('"', '\\"')


# This following commands are run on the pfsense device(s) to:
# 1. add the controller to pfsense, which will initiate a connection to the controller
# 2. retrieve the identity of this pfsense device for registration on the controller
device_script = '''
curl -s -f --unix-socket /var/run/pfnet-controller.sock -H "Content-Type: application/json" -d "{}" http://unix/api/mim/controllers >/dev/null
if [ $? != 0 ]; then
	# try with deprecated API
	curl -s -f --unix-socket /var/run/pfnet-controller.sock -H "Content-Type: application/json" -d "{}" http://unix/api/system/controller >/dev/null
	if [ $? != 0 ]; then
		echo -n "Failed to apply controller info to device $HOSTNAME via curl" >&2
		exit 1
	fi
fi
curl -s -f --unix-socket /var/run/pfnet-controller.sock http://unix/api/mim/device/identity
if [ $? != 0 ]; then
	# try with deprecated API
	curl -s -f --unix-socket /var/run/pfnet-controller.sock http://unix/api/system/mim/devid
	if [ $? != 0 ]; then
		echo -n "Failed to get device $HOSTNAME info via curl" >&2
		exit 1
	fi
fi
'''.format(controller_info_escaped, controller_info_escaped)

#
# Main loop for connect to each pfSense device and register it
#
start = time.time()
for pfip in pfsense_addresses:

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

	try:
		print("====> {}".format(pfip))
		sshclient = paramiko.client.SSHClient()

		# comment this line out if all pfsense devices are in known_hosts:
		sshclient.set_missing_host_key_policy(paramiko.AutoAddPolicy())

		# if ssh password is defined, then use it
		if SSHPASS:
			sshclient.connect(pfip, username=SSHUSER, password=SSHPASS)
		else:
			sshclient.connect(pfip, username=SSHUSER)
		stdin, stdout, stderr = sshclient.exec_command(device_script)
		val = stdout.read().decode()
		try:
			# Expect JSON output from the API request. If we get anything else,
			# then it's not useful and cannot be used to register the device
			# to the controller
			device_info = json.loads(val)

		except Exception as e:
			print("Expected JSON output from device identity request, got: '{}'".format(val))
			try:
				err = stderr.read().decode()
				if err:
					print("Error:", err)
			except:
				pass

			raise

		sshclient.close()
		sshclient = None

		#
		# Add the device to the controller
		#

		controlledDev = DeviceIdentity.from_dict(device_info)
		addDevResp = add_controlled_device.sync(client=client, body=controlledDev)
		if isinstance(addDevResp, ControlledDevice):
			print("Successfully added device {}, ID: {}".format(pfip, addDevResp.device_id))
		else:
			print("Failed to add device {}:".format(pfip), addDevResp)

	except Exception as e:
		print("Configuring device {} failed: {}".format(pfip, e))
		continue

	finally:
		if sshclient:
			sshclient.close()

