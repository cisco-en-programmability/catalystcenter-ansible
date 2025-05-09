#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_device_module_count_v1_info
short_description: Information module for Network Device Module Count V1
description:
  - Get all Network Device Module Count V1.
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
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices GetModuleCountV1
    description: Complete reference of the GetModuleCountV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-module-count
notes:
  - SDK Method used are devices.Devices.get_module_count_v1,
  - Paths used are get /dna/intent/api/v1/network-device/module/count,
"""
EXAMPLES = r"""
- name: Get all Network Device Module Count V1
  cisco.catalystcenter.network_device_module_count_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
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
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": 0,
      "version": "string"
    }
"""
