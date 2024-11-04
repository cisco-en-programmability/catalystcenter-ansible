#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_replacement_info
short_description: Information module for Device Replacement
description:
- Get all Device Replacement.
- >
   Get list of replacement devices with replacement details and it can filter replacement devices based on Faulty
   Device Name,Faulty Device Platform, Replacement Device Platform, Faulty Device Serial Number,Replacement Device
   Serial Number, Device Replacement status, Product Family.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  faultyDeviceName:
    description:
    - FaultyDeviceName query parameter. Faulty Device Name.
    type: str
  faultyDevicePlatform:
    description:
    - FaultyDevicePlatform query parameter. Faulty Device Platform.
    type: str
  replacementDevicePlatform:
    description:
    - ReplacementDevicePlatform query parameter. Replacement Device Platform.
    type: str
  faultyDeviceSerialNumber:
    description:
    - FaultyDeviceSerialNumber query parameter. Faulty Device Serial Number.
    type: str
  replacementDeviceSerialNumber:
    description:
    - ReplacementDeviceSerialNumber query parameter. Replacement Device Serial Number.
    type: str
  replacementStatus:
    description:
    - >
      ReplacementStatus query parameter. Device Replacement status READY-FOR-REPLACEMENT, REPLACEMENT-IN-PROGRESS,
      REPLACEMENT-SCHEDULED, REPLACED, ERROR, NETWORK_READINESS_REQUESTED, NETWORK_READINESS_FAILED. 
    elements: str
    type: list
  family:
    description:
    - Family query parameter. List of familiesRouters, Switches and Hubs, AP. 
    elements: str
    type: list
  sortBy:
    description:
    - SortBy query parameter. SortBy this field. SortBy is mandatory when order is used.
    type: str
  sortOrder:
    description:
    - SortOrder query parameter. Order on displayNameASC,DESC.
    type: str
  offset:
    description:
    - Offset query parameter.
    type: int
  limit:
    description:
    - Limit query parameter.
    type: int
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Device Replacement ReturnListOfReplacementDevicesWithReplacementDetailsV1
  description: Complete reference of the ReturnListOfReplacementDevicesWithReplacementDetailsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!return-list-of-replacement-devices-with-replacement-details-v-1
notes:
  - SDK Method used are
    device_replacement.DeviceReplacement.return_replacement_devices_with_details,

  - Paths used are
    get /dna/intent/api/v1/device-replacement,

"""

EXAMPLES = r"""
- name: Get all Device Replacement
  cisco.catalystcenter.device_replacement_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    faultyDeviceName: string
    faultyDevicePlatform: string
    replacementDevicePlatform: string
    faultyDeviceSerialNumber: string
    replacementDeviceSerialNumber: string
    replacementStatus: []
    family: []
    sortBy: string
    sortOrder: string
    offset: 0
    limit: 0
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "creationTime": 0,
          "family": "string",
          "faultyDeviceId": "string",
          "faultyDeviceName": "string",
          "faultyDevicePlatform": "string",
          "faultyDeviceSerialNumber": "string",
          "id": "string",
          "neighbourDeviceId": "string",
          "networkReadinessTaskId": "string",
          "replacementDevicePlatform": "string",
          "replacementDeviceSerialNumber": "string",
          "replacementStatus": "string",
          "replacementTime": 0,
          "workflowId": "string",
          "workflowFailedStep": "string",
          "readinesscheckTaskId": "string"
        }
      ],
      "version": "string"
    }
"""
