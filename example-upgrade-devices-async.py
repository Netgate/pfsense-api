#!/usr/bin/env python3
#
# This is an example script to concurrently upgrade a set of devices by their tags.
# This is the same as example-upgrade-devices, but uses async API calls so that
# the request act on multiple devices at the same time.
#
# Example run:
#   PASSWORD=controllerpassword python3 ./example-upgrade-devices-async.py {tags}
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
from pfapi.api.system import get_status, get_system_update_info, perform_system_update, get_system_update_progress

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

# -------------- example async functions for upgrading the devices --------------

async def upgrade_device(dev):
	devaddr = dev.device.address.split(':',1)[0]
	devname = dev.device_name.split('.',1)[0]
	print(f"{dev.device_name} - Checking available system update(s)")
	info = await get_system_update_info.asyncio(client=dev.client)
	try:
		if info.update_messages is not None and len(info.update_messages) > 0:
			print(f"{devname} - Update messages:")
			prefix = f"{devname} ({devaddr}) - "
			msg_str = '\n'.join([prefix+m for m in info.update_messages])
			print(msg_str + '\n')
			if 'not been registered' in msg_str:
				try:
					i = msg_str.index(' <a href')
					msg_str = msg_str[:i]
				except:
					pass
				return msg_str
	except Exception as e:
		if isinstance(info, Error):
			return f"{devname} {devaddr} - system update check returned Error {info.errmsg}"
		else:
			return f"{devname} {devaddr} - system update check returned {info}"

	try:
		if info.latest_base_system == "" or info.curr_base_system == "" or info.latest_base_system == info.curr_base_system:
			print(f"{devname} ({devaddr}) - skipping upgrade, no new version available")
			return f"{devname} ({devaddr}) - skipping upgrade, no new version available"
	except Exception as e:
		print(f"{devname} {devaddr} - skipping device due to exception: {e}")
		return f"{devname} {devaddr} - skipping device due to exception: {e}"

	print(f"{devname} {devaddr} - Upgrading device to {info.latest_base_system}")
	upgradeOpt = SystemUpdateOptions(firmware_branch=info.firmware_branch)

	result = await perform_system_update.asyncio(client=dev.client, body=upgradeOpt)
	print(f"{devname} {devaddr} - perform_system_update request returned: {result}")

	print(f"{devname} {devaddr} - commenced upgrade; progress follows:")

	# query upgrade progress until it has completed or fails
	lastMsgs = ""
	progressStarted = False
	while True:
		progress = await get_system_update_progress.asyncio(client=dev.client)
		if not progressStarted and progress.completed > 0:
			progressStarted = True

		if progressStarted and progress.completed == 0:
			# Completion would reset to 0 if the log file cycles or the
			# system has rebooted. Mark as a completed upgrade.
			return f"{devname} {devaddr} - Upgrade completed"

		if progress.messages is None:
			if progressStarted:
				break
			# progress messages might not be available if upgrade has not logged anything
			continue
		try:
			prefix = f"{devname} ({devaddr}): "
			msgs_all = '\n'.join([prefix+m for m in progress.messages])
			if len(msgs_all) > len(lastMsgs):
				print(msgs_all[len(lastMsgs):], end="")

				# print the current completed percent (guessed)
				#print(" {{completed {}%}} ".format(progress.completed), end="")
			lastMsgs = msgs_all
			time.sleep(1.0)
		except Exception as e:
			print("Exception", e)
			print("Progress returned", progress)
			return f"{devname} {devaddr} - Upgrade exception {e}, messages: {progress}"

		if progress.completed == 100:
			return f"{devname} {devaddr} - Upgrade completed"

async def batch_upgrade(devs):
	'''
	Batch alias requests to the list of device clients

	:param list[RequestClient] devs: a list of device request clients
	'''

	print("\nSending requests to:")
	print('\n'.join(['\t- '+ d.device_id + '    ' + d.device_name for d in devs]) + "\n")

	# Bulk request send, and wait for all of them to complete with asyncio.gather()
	tasks = []
	for dev in devs:
		tasks.append(upgrade_device(dev))

	results = await asyncio.gather(*tasks)

	print("\nResults:")
	for result in results:
	   print(f"\t- {result}")


# Bulk upgrade request to the online devices.
print("\nCommencing upgrades on devices:")

# Work in blocks of N_DEVICES (10) devices so
# that it's lighter on the controller and easier
# to track progress.
N_DEVICES=10
for i in range(0, len(online_devs), N_DEVICES):
	asyncio.run(batch_upgrade(online_devs[i:i+N_DEVICES]))

# Stop the refresh timer to exit, otherwise it will wait until the timer event happens
sessionClient.stop()