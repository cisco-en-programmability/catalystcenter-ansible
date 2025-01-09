#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sda_fabric_edge_device_info
short_description: Information module for Sda Fabric Edge Device Info
description:
- This module represents an alias of the module sda_fabric_edge_device_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deviceManagementIpAddress:
    description:
    - DeviceManagementIpAddress query parameter.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for SDA GetEdgeDeviceFromSDAFabricV1
  description: Complete reference of the GetEdgeDeviceFromSDAFabricV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-edge-device-from-sda-fabric
notes:
  - SDK Method used are
    sda.Sda.get_edge_device,

  - Paths used are
    get /dna/intent/api/v1/business/sda/edge-device,
  - It should be noted that this module is an alias of sda_fabric_edge_device_v1_info

"""

EXAMPLES = r"""
- name: Get all Sda Fabric Edge Device Info
  cisco.catalystcenter.sda_fabric_edge_device_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    deviceManagementIpAddress: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "deviceManagementIpAddress": "string",
      "deviceName": "string",
      "roles": "string",
      "siteNameHierarchy": "string",
      "fabricSiteNameHierarchy": "string",
      "status": "string",
      "description": "string"
    }
"""
