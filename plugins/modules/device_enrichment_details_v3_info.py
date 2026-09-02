#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_enrichment_details_v3_info
short_description: Information module for Device Enrichment Details V3
description:
  - Get all Device Enrichment Details V3. - > Enriches a given network device context device id or device Mac Address or device
    management IP address with details about the device and neighbor topology.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices DeviceEnrichmentDetails
    description: Complete reference of the DeviceEnrichmentDetails API.
    link: https://developer.cisco.com/docs/dna-center/#!device-enrichment-details
notes:
  - SDK Method used are
    devices.Devices.device_enrichment_details,
  - Paths used are
    get /dna/intent/api/v1/deviceEnrichmentDetails,
"""

EXAMPLES = r"""
---
- name: Get all Device Enrichment Details V3
  cisco.catalystcenter.device_enrichment_details_v3_info:
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
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "response": [
          {
            "deviceDetails": {
              "family": "string",
              "type": "string",
              "location": {},
              "errorCode": "string",
              "macAddress": "string",
              "role": "string",
              "apManagerInterfaceIp": "string",
              "associatedWlcIp": "string",
              "bootDateTime": "string",
              "collectionStatus": "string",
              "interfaceCount": "string",
              "lineCardCount": "string",
              "lineCardId": "string",
              "managementIpAddress": "string",
              "memorySize": "string",
              "platformId": "string",
              "reachabilityFailureReason": "string",
              "reachabilityStatus": "string",
              "snmpContact": "string",
              "snmpLocation": "string",
              "tunnelUdpPort": {},
              "waasDeviceMode": {},
              "series": "string",
              "inventoryStatusDetail": "string",
              "collectionInterval": "string",
              "serialNumber": "string",
              "softwareVersion": "string",
              "roleSource": "string",
              "hostname": "string",
              "upTime": "string",
              "lastUpdatedTime": 0,
              "errorDescription": "string",
              "locationName": {},
              "tagCount": "string",
              "createdTime": "string",
              "id": "string",
              "neighborTopology": {
                "nodes": [
                  {
                    "role": "string",
                    "name": "string",
                    "id": "string",
                    "description": "string",
                    "deviceType": "string",
                    "platformId": "string",
                    "family": "string",
                    "ip": "string",
                    "softwareVersion": "string",
                    "userId": {},
                    "nodeType": "string",
                    "radioFrequency": {},
                    "clients": {},
                    "count": {},
                    "healthScore": 0,
                    "level": 0,
                    "fabricGroup": {},
                    "connectedDevice": {},
                    "fabricRole": [
                      "string"
                    ],
                    "stackType": "string",
                    "additionalInfo": {}
                  }
                ],
                "links": [
                  {
                    "source": "string",
                    "label": [
                      {}
                    ],
                    "target": "string",
                    "id": {},
                    "portUtilization": {},
                    "linkStatus": "string",
                    "sourcelinkStatus": "string",
                    "targetlinkStatus": "string",
                    "sourceInterfaceName": "string",
                    "targetInterfaceName": "string",
                    "sourceDuplexInfo": "string",
                    "targetDuplexInfo": "string",
                    "sourcePortMode": "string",
                    "targetPortMode": "string",
                    "sourceAdminStatus": "string",
                    "targetAdminStatus": "string",
                    "apRadioAdminStatus": "string",
                    "apRadioOperStatus": "string",
                    "sourcePortVLANInfo": "string",
                    "targetPortVLANInfo": "string"
                  }
                ]
              }
            }
          }
        ],
        "version": "string"
      }
    ]
"""
