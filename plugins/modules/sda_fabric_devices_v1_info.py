#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_fabric_devices_v1_info
short_description: Information module for Sda Fabric Devices V1
description:
- Get all Sda Fabric Devices V1.
- Returns a list of fabric devices that match the provided query parameters.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  fabricId:
    description:
    - FabricId query parameter. ID of the fabric this device belongs to.
    type: str
  networkDeviceId:
    description:
    - NetworkDeviceId query parameter. Network device ID of the fabric device.
    type: str
  deviceRoles:
    description:
    - >
      DeviceRoles query parameter. Device roles of the fabric device. Allowed values are CONTROL_PLANE_NODE,
      EDGE_NODE, BORDER_NODE, WIRELESS_CONTROLLER_NODE, EXTENDED_NODE.
    type: str
  offset:
    description:
    - Offset query parameter. Starting record for pagination.
    type: float
  limit:
    description:
    - >
      Limit query parameter. Maximum number of records to return. The maximum number of objects supported in a
      single request is 500.
    type: float
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for SDA GetFabricDevicesV1
  description: Complete reference of the GetFabricDevicesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-fabric-devices
notes:
  - SDK Method used are
    sda.Sda.get_fabric_devices_v1,

  - Paths used are
    get /dna/intent/api/v1/sda/fabricDevices,

"""

EXAMPLES = r"""
- name: Get all Sda Fabric Devices V1
  cisco.catalystcenter.sda_fabric_devices_v1_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    fabricId: string
    networkDeviceId: string
    deviceRoles: string
    offset: 0
    limit: 0
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
          "id": "string",
          "networkDeviceId": "string",
          "fabricId": "string",
          "deviceRoles": [
            "string"
          ],
          "borderDeviceSettings": {
            "borderTypes": [
              "string"
            ],
            "layer3Settings": {
              "localAutonomousSystemNumber": "string",
              "isDefaultExit": true,
              "importExternalRoutes": true,
              "borderPriority": 0,
              "prependAutonomousSystemCount": 0
            }
          }
        }
      ],
      "version": "string"
    }
"""
