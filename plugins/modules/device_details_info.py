#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_details_info
short_description: Information module for Device Details
description:
  - Get all Device Details. - > Returns detailed Network
    Device information retrieved by Mac Address, Device
    Name or UUID for any given point of time.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  timestamp:
    description:
      - Timestamp query parameter. UTC timestamp of
        device data in milliseconds.
    type: float
  identifier:
    description:
      - Identifier query parameter. One of "macAddress",
        "nwDeviceName", "uuid" (case insensitive).
    type: str
  searchBy:
    description:
      - SearchBy query parameter. MAC Address, device
        name, or UUID of the network device.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices
      GetDeviceDetail
    description: Complete reference of the GetDeviceDetail
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-device-detail
notes:
  - SDK Method used are
    devices.Devices.get_device_detail,
  - Paths used are
    get /dna/intent/api/v1/device-detail,
"""

EXAMPLES = r"""
---
- name: Get all Device Details
  cisco.catalystcenter.device_details_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
    timestamp: 0
    identifier: string
    searchBy: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "noiseScore": 0,
      "policyTagName": "string",
      "interferenceScore": 0,
      "opState": "string",
      "powerSaveMode": "string",
      "mode": "string",
      "resetReason": "string",
      "nwDeviceRole": "string",
      "protocol": "string",
      "powerMode": "string",
      "connectedTime": "string",
      "ringStatus": true,
      "ledFlashSeconds": "string",
      "ip_addr_managementIpAddr": "string",
      "stackType": "string",
      "subMode": "string",
      "serialNumber": "string",
      "nwDeviceName": "string",
      "deviceGroupHierarchyId": "string",
      "cpu": 0,
      "utilization": "string",
      "nwDeviceId": "string",
      "siteHierarchyGraphId": "string",
      "nwDeviceFamily": "string",
      "macAddress": "string",
      "homeApEnabled": "string",
      "deviceSeries": "string",
      "collectionStatus": "string",
      "utilizationScore": 0,
      "maintenanceMode": true,
      "interference": "string",
      "softwareVersion": "string",
      "tagIdList": [
        {}
      ],
      "powerType": "string",
      "overallHealth": 0,
      "managementIpAddr": "string",
      "memory": "string",
      "communicationState": "string",
      "apType": "string",
      "adminState": "string",
      "noise": "string",
      "icapCapability": "string",
      "regulatoryDomain": "string",
      "ethernetMac": "string",
      "nwDeviceType": "string",
      "airQuality": "string",
      "rfTagName": "string",
      "siteTagName": "string",
      "platformId": "string",
      "upTime": "string",
      "memoryScore": 0,
      "powerSaveModeCapable": "string",
      "powerProfile": "string",
      "airQualityScore": 0,
      "location": "string",
      "flexGroup": "string",
      "lastBootTime": 0,
      "powerCalendarProfile": "string",
      "connectivityStatus": 0,
      "ledFlashEnabled": "string",
      "cpuScore": 0,
      "avgTemperature": 0,
      "maxTemperature": 0,
      "haStatus": "string",
      "osType": "string",
      "timestamp": 0,
      "apGroup": "string",
      "redundancyMode": "string",
      "featureFlagList": [
        "string"
      ],
      "freeMbufScore": 0,
      "HALastResetReason": "string",
      "wqeScore": 0,
      "redundancyPeerStateDerived": "string",
      "freeTimerScore": 0,
      "redundancyPeerState": "string",
      "redundancyStateDerived": "string",
      "redundancyState": "string",
      "packetPoolScore": 0,
      "freeTimer": 0,
      "packetPool": 0,
      "wqe": 0,
      "freeMbuf": 0
    }
"""
