#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_device_role_info
short_description: Information module for Sda Device
  Role
description:
  - Get all Sda Device Role.
  - Get device role in SDA Fabric.
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
      - DeviceManagementIpAddress query parameter. Device
        Management IP Address.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA GetDeviceRoleInSDAFabric
    description: Complete reference of the GetDeviceRoleInSDAFabric
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-device-role-in-sda-fabric
notes:
  - SDK Method used are
    sda.Sda.get_device_role_in_sda_fabric,
  - Paths used are
    get /dna/intent/api/v1/business/sda/device/role,
"""

EXAMPLES = r"""
---
- name: Get all Sda Device Role
  cisco.catalystcenter.sda_device_role_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    deviceManagementIpAddress: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "roles": [
        "string"
      ],
      "status": "string",
      "description": "string"
    }
"""
