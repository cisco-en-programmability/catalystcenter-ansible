#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: discovery_device_range_v1_info
short_description: Information module for Discovery Device Range V1
description:
  - Get all Discovery Device Range V1.
  - >
    Returns the network devices discovered for the given discovery and for the given
    range. The maximum number of
    records that can be retrieved is 500. Discovery ID can be obtained using the "Get
    Discoveries by range" API.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Discovery ID.
    type: str
  startIndex:
    description:
      - StartIndex path parameter. Starting index for the records.
    type: int
  recordsToReturn:
    description:
      - RecordsToReturn path parameter. Number of records to fetch from the start
        index.
    type: int
  taskId:
    description:
      - TaskId query parameter.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Discovery GetDiscoveredDevicesByRangeV1
    description: Complete reference of the GetDiscoveredDevicesByRangeV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-discovered-devices-by-range
notes:
  - SDK Method used are discovery.Discovery.get_discovered_devices_by_range_v1,
  - Paths used are get /dna/intent/api/v1/discovery/{id}/network-device/{startIndex}/{recordsToReturn},
"""
EXAMPLES = r"""
- name: Get all Discovery Device Range V1
  cisco.catalystcenter.discovery_device_range_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    taskId: string
    id: string
    startIndex: 0
    recordsToReturn: 0
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "anchorWlcForAp": "string",
          "authModelId": "string",
          "avgUpdateFrequency": 0,
          "bootDateTime": "string",
          "cliStatus": "string",
          "duplicateDeviceId": "string",
          "errorCode": "string",
          "errorDescription": "string",
          "family": "string",
          "hostname": "string",
          "httpStatus": "string",
          "id": "string",
          "imageName": "string",
          "ingressQueueConfig": "string",
          "interfaceCount": "string",
          "inventoryCollectionStatus": "string",
          "inventoryReachabilityStatus": "string",
          "lastUpdated": "string",
          "lineCardCount": "string",
          "lineCardId": "string",
          "location": "string",
          "locationName": "string",
          "macAddress": "string",
          "managementIpAddress": "string",
          "memorySize": "string",
          "netconfStatus": "string",
          "numUpdates": 0,
          "pingStatus": "string",
          "platformId": "string",
          "portRange": "string",
          "qosStatus": "string",
          "reachabilityFailureReason": "string",
          "reachabilityStatus": "string",
          "role": "string",
          "roleSource": "string",
          "serialNumber": "string",
          "snmpContact": "string",
          "snmpLocation": "string",
          "snmpStatus": "string",
          "softwareVersion": "string",
          "tag": "string",
          "tagCount": 0,
          "type": "string",
          "upTime": "string",
          "vendor": "string",
          "wlcApDeviceStatus": "string"
        }
      ],
      "version": "string"
    }
"""
