#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_anchor_capable_devices_info
short_description: Information module for Wireless Controllers Anchor Capable Devices
description:
  - Get all Wireless Controllers Anchor Capable Devices.
  - This API allows the user to get all anchor capable devices.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless GetAllAnchorCapableDevices
    description: Complete reference of the GetAllAnchorCapableDevices API.
    link: https://developer.cisco.com/docs/dna-center/#!get-all-anchor-capable-devices
notes:
  - SDK Method used are
    wireless.Wireless.get_all_anchor_capable_devices,
  - Paths used are
    get /dna/intent/api/v1/wirelessControllers/anchorCapableDevices,
"""

EXAMPLES = r"""
---
- name: Get all Wireless Controllers Anchor Capable Devices
  cisco.catalystcenter.wireless_controllers_anchor_capable_devices_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "deviceIp": "string",
        "deviceName": "string",
        "wirelessMgmtIP": "string",
        "wirelessMgmtIPv6": {},
        "interfaceIpAddresses": [
          "string"
        ]
      }
    ]
"""
