#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sda_device_info
short_description: Information module for Sda Device Info
description:
- This module represents an alias of the module sda_device_v1_info
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
- catalystcentersdk >= 2.3.7.6
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for SDA GetDeviceInfoFromSDAFabricV1
  description: Complete reference of the GetDeviceInfoFromSDAFabricV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-device-info-from-sda-fabric
notes:
  - SDK Method used are
    sda.Sda.get_device_info,

  - Paths used are
    get /dna/intent/api/v1/business/sda/device,
  - It should be noted that this module is an alias of sda_device_v1_info

"""

EXAMPLES = r"""
- name: Get all Sda Device Info
  cisco.catalystcenter.sda_device_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
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
      "status": "string",
      "description": "string",
      "name": "string",
      "roles": [
        "string"
      ],
      "deviceManagementIpAddress": "string",
      "siteHierarchy": "string"
    }
"""
