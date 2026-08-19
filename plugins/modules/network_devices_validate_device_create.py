#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_devices_validate_device_create
short_description: Resource module for Network Devices Validate Device Create
description:
  - Manage operation create of the resource Network Devices Validate Device Create. - > Validates the credentials and connectivity
    of a network device. This endpoint checks if the provided details are correct and if the device can be.
version_added: '2.3.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  category:
    description: Category of the device. Used to determine the type of the device being added. | Category | Description |
      Required Credentials | Optional Credentials | | ------------------------------------------- |
          -----------------------------------------------------------...
      | -------------------- | -------------------- | | `NETWORK_DEVICE` | Standard Cisco network devices like switches, routers,
      controllers | CLI, SNMP | HTTP, NETCONF | | `COMPUTE_DEVICE` | Server or computing system manufactured by Cisco such
      as Unified Computing System (UCS) | HTTP | CLI, SNMP | | `THIRD_PARTY_DEVICE` | Non-Cisco network devices that support
      SNMP monitoring | SNMP | - | | `MERAKI_DASHBOARD` | Cisco Meraki cloud-managed devices accessed via Meraki Dashboard
      | Meraki | - | | `FIREWALL_MANAGEMENT_CENTER` | Cisco Secure Firewall Management Center (FMC) | HTTP | - |.
    type: str
  credentials:
    description: Credentials used to access the network device.
    suboptions:
      http:
        description: Extra properties for HTTP(S) credentials.
        suboptions:
          protocol:
            description: HTTP protocol. Compute device require HTTPS.
            type: str
        type: dict
    type: dict
  managementAddress:
    description: Either an IP address or a fully-qualified domain name.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices ValidatesANetworkDevice
    description: Complete reference of the ValidatesANetworkDevice API.
    link: https://developer.cisco.com/docs/dna-center/#!validates-a-network-device
notes:
  - SDK Method used are
    devices.Devices.validates_a_network_device,
  - Paths used are
    post /dna/intent/api/v1/networkDevices/validateDevice,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.network_devices_validate_device_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    category: string
    credentials:
      http: {}
    managementAddress: {}
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
