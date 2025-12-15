#!/usr/bin/env python3
#
# This is an example script of how to push an alias to all online devices
# or those of a specific tag. The requests are done in batches of
# concurrently and results are reported in the final output.
#
# Example run:
#   PASSWORD=controllerpassword python3 ./example-set-alias.py {tags}
#
# where {tags} is a comma-separated list of tags
#

import asyncio
import sys
import time

from helper_funcs import *

#
# Controller APIs
#
from pfapi.models import *

from pfapi.api.aliases import firewall_get_aliases, firewall_add_alias

###########################################

settings = get_settings()
tags = settings.TAGS
if not tags:
	print("Comma-separated list of tags not provided, applying to all devices")

# Create a session client, which is used as the parent to all the per-device API clients.
sessionClient = RequestClient(controller_url=settings.CONTROLLER_URL)

if not sessionClient.login(settings.USER, settings.PASSWORD):
	print("Login failed... quitting")
	sys.exit(1)

online_devs = get_online_devices(sessionClient, tags)

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