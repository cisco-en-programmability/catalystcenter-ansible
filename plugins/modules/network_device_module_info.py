#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: network_device_module_info
short_description: Information module for Network Device Module Info
description:
- This module represents an alias of the module network_device_module_v1_info
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
  limit:
    description:
    - Limit query parameter. The number of records to show for this page. Min 1, Max 500.
    type: int
  offset:
    description:
    - Offset query parameter.
    type: int
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
  id:
    description:
    - Id path parameter. Module id.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices GetModuleInfoByIdV1
  description: Complete reference of the GetModuleInfoByIdV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-module-info-by-id
- name: Cisco DNA Center documentation for Devices GetModulesV1
  description: Complete reference of the GetModulesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-modules
notes:
  - SDK Method used are
    devices.Devices.get_module_info_by_id_v1,
    devices.Devices.get_modules_v1,

  - Paths used are
    get /dna/intent/api/v1/network-device/module,
    get /dna/intent/api/v1/network-device/module/{id},
  - It should be noted that this module is an alias of network_device_module_v1_info

"""

EXAMPLES = r"""
- name: Get all Network Device Module Info
  cisco.catalystcenter.network_device_module_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    deviceId: string
    limit: 0
    offset: 0
    nameList: []
    vendorEquipmentTypeList: []
    partNumberList: []
    operationalStateCodeList: []
  register: result

- name: Get Network Device Module Info by id
  cisco.catalystcenter.network_device_module_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
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
        "assemblyNumber": "string",
        "assemblyRevision": "string",
        "attributeInfo": {},
        "containmentEntity": "string",
        "description": "string",
        "entityPhysicalIndex": "string",
        "id": "string",
        "isFieldReplaceable": "string",
        "isReportingAlarmsAllowed": "string",
        "manufacturer": "string",
        "moduleIndex": 0,
        "name": "string",
        "operationalStateCode": "string",
        "partNumber": "string",
        "serialNumber": "string",
        "vendorEquipmentType": "string"
      },
      "version": "string"
    }
"""
