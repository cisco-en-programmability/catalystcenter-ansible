#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: network_device_global_polling_interval_info
short_description: Information module for Network Device Global Polling Interval Info
description:
- This module represents an alias of the module network_device_global_polling_interval_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices GetPollingIntervalForAllDevicesV1
  description: Complete reference of the GetPollingIntervalForAllDevicesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-polling-interval-for-all-devices
notes:
  - SDK Method used are
    devices.Devices.get_polling_interval_for_all_devices_v1,

  - Paths used are
    get /dna/intent/api/v1/network-device/collection-schedule/global,
  - It should be noted that this module is an alias of network_device_global_polling_interval_v1_info

"""

EXAMPLES = r"""
- name: Get all Network Device Global Polling Interval Info
  cisco.catalystcenter.network_device_global_polling_interval_info:
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
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": 0,
      "version": "string"
    }
"""
