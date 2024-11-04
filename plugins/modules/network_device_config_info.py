#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_config_info
short_description: Information module for Network Device Config
description:
- Get all Network Device Config.
- Get Network Device Config by id.
- >
   Returns the config for all devices. This API has been deprecated and will not be available in a Cisco Catalyst
   Center release after Nov 1st 2024 23 59 59 GMT.
- Returns the device config by specified device ID.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  networkDeviceId:
    description:
    - NetworkDeviceId path parameter.
    type: str
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Devices GetDeviceConfigByIdV1
  description: Complete reference of the GetDeviceConfigByIdV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-device-config-by-id-v-1
- name: Cisco CATALYST Center documentation for Devices GetDeviceConfigForAllDevicesV1
  description: Complete reference of the GetDeviceConfigForAllDevicesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-device-config-for-all-devices-v-1
notes:
  - SDK Method used are
    devices.Devices.get_device_config_by_id_v1,
    devices.Devices.get_device_config_for_all_devices_v1,

  - Paths used are
    get /dna/intent/api/v1/network-device/config,
    get /dna/intent/api/v1/network-device/{networkDeviceId}/config,

"""

EXAMPLES = r"""
- name: Get all Network Device Config
  cisco.catalystcenter.network_device_config_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result

- name: Get Network Device Config by id
  cisco.catalystcenter.network_device_config_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    networkDeviceId: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": "string",
      "version": "string"
    }
"""
