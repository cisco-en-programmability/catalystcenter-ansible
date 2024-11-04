#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_module_count_info
short_description: Information module for Network Device Module Count
description:
- Get all Network Device Module Count.
- Returns Module Count.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deviceId:
    description:
    - DeviceId query parameter.
    type: str
  nameList:
    description:
    - NameList query parameter. 
    elements: str
    type: list
  vendorEquipmentTypeList:
    description:
    - VendorEquipmentTypeList query parameter. 
    elements: str
    type: list
  partNumberList:
    description:
    - PartNumberList query parameter. 
    elements: str
    type: list
  operationalStateCodeList:
    description:
    - OperationalStateCodeList query parameter. 
    elements: dict
    type: list
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Devices GetModuleCountV1
  description: Complete reference of the GetModuleCountV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-module-count-v-1
notes:
  - SDK Method used are
    devices.Devices.get_module_count_v1,

  - Paths used are
    get /dna/intent/api/v1/network-device/module/count,

"""

EXAMPLES = r"""
- name: Get all Network Device Module Count
  cisco.catalystcenter.network_device_module_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    deviceId: string
    nameList: []
    vendorEquipmentTypeList: []
    partNumberList: []
    operationalStateCodeList: []
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": 0,
      "version": "string"
    }
"""
