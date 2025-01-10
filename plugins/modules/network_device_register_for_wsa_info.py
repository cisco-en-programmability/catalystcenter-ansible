#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: network_device_register_for_wsa_info
short_description: Information module for Network Device Register For Wsa Info
description:
- This module represents an alias of the module network_device_register_for_wsa_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  serialNumber:
    description:
    - SerialNumber query parameter. Serial number of the device.
    type: str
  macaddress:
    description:
    - Macaddress query parameter. Mac addres of the device.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices GetDevicesRegisteredForWSANotificationV1
  description: Complete reference of the GetDevicesRegisteredForWSANotificationV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-devices-registered-for-wsa-notification
notes:
  - SDK Method used are
    devices.Devices.get_devices_registered_for_wsa_notification_v1,

  - Paths used are
    get /dna/intent/api/v1/network-device/tenantinfo/macaddress,
  - It should be noted that this module is an alias of network_device_register_for_wsa_v1_info

"""

EXAMPLES = r"""
- name: Get all Network Device Register For Wsa Info
  cisco.catalystcenter.network_device_register_for_wsa_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    serialNumber: string
    macaddress: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "macAddress": "string",
        "modelNumber": "string",
        "name": "string",
        "serialNumber": "string",
        "tenantId": "string"
      },
      "version": "string"
    }
"""
