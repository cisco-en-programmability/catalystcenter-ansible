#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: network_devices_id_info
short_description: Information module for Network Devices Id Info
description:
- This module represents an alias of the module network_devices_id_v1_info
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
    - Id path parameter. Unique identifier for the network device.
    type: str
  views:
    description:
    - >
      Views query parameter. The specific views being requested. This is an optional parameter which can be passed
      to get one or more of the network device data. If this is not provided, then it will default to BASIC views.
      If multiple views are provided, the response will contain the union of the views. Available values BASIC,
      RESYNC, USER_DEFINED_FIELDS.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices GetDetailsOfASingleNetworkDeviceV1
  description: Complete reference of the GetDetailsOfASingleNetworkDeviceV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-details-of-a-single-network-device
notes:
  - SDK Method used are
    devices.Devices.get_details_of_a_single_network_device_v1,

  - Paths used are
    get /dna/intent/api/v1/networkDevices/{id},
  - It should be noted that this module is an alias of network_devices_id_v1_info

"""

EXAMPLES = r"""
- name: Get Network Devices Id Info by id
  cisco.catalystcenter.network_devices_id_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    views: string
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
        "id": "string",
        "managementAddress": "string",
        "dnsResolvedManagementIpAddress": "string",
        "hostname": "string",
        "macAddress": "string",
        "serialNumbers": [
          "string"
        ],
        "type": "string",
        "family": "string",
        "series": "string",
        "status": "string",
        "platformIds": [
          "string"
        ],
        "softwareType": "string",
        "softwareVersion": "string",
        "vendor": "string",
        "stackDevice": true,
        "bootTime": 0,
        "role": "string",
        "roleSource": "string",
        "apEthernetMacAddress": "string",
        "apManagerInterfaceIpAddress": "string",
        "apWlcIpAddress": "string",
        "deviceSupportLevel": "string",
        "snmpLocation": "string",
        "snmpContact": "string",
        "reachabilityStatus": "string",
        "reachabilityFailureReason": "string",
        "managementState": "string",
        "lastSuccessfulResyncReasons": [
          "string"
        ],
        "resyncStartTime": 0,
        "resyncEndTime": 0,
        "resyncReasons": [
          "string"
        ],
        "resyncRequestedByApps": [
          "string"
        ],
        "pendingResyncRequestCount": 0,
        "pendingResyncRequestReasons": [
          "string"
        ],
        "resyncIntervalSource": "string",
        "resyncIntervalMinutes": 0,
        "errorCode": "string",
        "errorDescription": "string",
        "userDefinedFields": {}
      },
      "version": "string"
    }
"""
