# pfSense API Software Toolkit

pfSense® Plus software is a widely deployed, robust, and easy to use firewall solution.
This repository contains the set of packages to extend the powerful management
capabilities of pfSense Plus through the availability a RESTful interface provided
by the pfSense Multi-instance Management Controller.

An [OpenAPI schema](./pfapi_openapi.yml) is provided for language agnostic client implementations. The
included generated definitions are for Python 3; other language support will be added in the future.

The schema generated document can be viewed here: https://netgate.github.io/pfsense-api/

## Usage

### Python

The Python package was generated using [openapi-python-client](https://github.com/openapi-generators/openapi-python-client).
Two examples are provided to demonstrate the use of this API library.

| File                   | Description                             |
|------------------------|-----------------------------------------|
| example-add-devices.py | demonstrates how to register the Controller to each pfSense device<br>and add them to the Controller |
| example.py             | authenticates with the Controller, iterates through each device,<br>queries them for their system update information and obtains their firewall aliases |
| example-upgrade-devices.py | upgrade a set of devices by their tags |
| example-set-alias.py   | add an alias to a set of devices by their tags using async batch requests |

#### Requirements

* Python 3.6 or newer
* [httpx](https://www.python-httpx.org) required by openapi-python-client generated code
* [Python Paramiko](https://www.paramiko.org/) used by `example-add-devices.py` for SSH

#### Running

Ensure that MIM is enabled on all devices that are going to be centrally managed.

To run the scripts in a `bash` or similar shell:

```shell
# example-add-devices.py
# Modify:
#   CONTROLLER_URL to the address of the MIM controller
#   SSHUSER admin username
#   pfsense_addresses list of pfSense system addresses
PYTHONPATH=py SSHPASS=ssh_password PASSWORD=controller_password python3 ./example-add-devices.py

# example.py
# Modify:
#   CONTROLLER_URL to the address of the MIM controller
PYTHONPATH=py PASSWORD=controller_password python3 ./example.py

# example-upgrade-devices.py
# Modify:
#   CONTROLLER_URL to the address of the MIM controller
PYTHONPATH=py PASSWORD=controller_password python3 ./example-upgrade-devices.py tag1,tag2
```

where the environment variables are:
* PYTHONPATH specifies the location of the Python pfSense API library, e.g. `py` which is relative to the examples.
* SSHPASS the admin's SSH password to login to each pfSense device. This doesn't need to be set if SSH keys are used. The `example-add-devices.py` script connects to each pfSense system using SSH to configure the local controller process.
* PASSWORD is the admin user's password to log into the Controller.

