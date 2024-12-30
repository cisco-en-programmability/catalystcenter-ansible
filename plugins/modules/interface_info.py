#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: interface_info
short_description: Information module for Interface Info
description:
- This module represents an alias of the module interface_v1_info
version_added: '6.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  interfaceUuid:
    description:
    - InterfaceUuid path parameter. Interface ID.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices LegitOperationsForInterfaceV1
  description: Complete reference of the LegitOperationsForInterfaceV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!legit-operations-for-interface
notes:
  - SDK Method used are
    devices.Devices.legit_operations_for_interface_v1,

  - Paths used are
    get /dna/intent/api/v1/interface/{interfaceUuid}/legit-operation,
  - It should be noted that this module is an alias of interface_v1_info

"""

EXAMPLES = r"""
- name: Get all Interface Info
  cisco.catalystcenter.interface_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    interfaceUuid: string
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
        "interfaceUuid": "string",
        "properties": [
          {
            "name": "string",
            "applicable": "string",
            "failureReason": "string"
          }
        ],
        "operations": [
          {
            "name": "string",
            "applicable": "string",
            "failureReason": "string"
          }
        ]
      },
      "version": "string"
    }
"""
