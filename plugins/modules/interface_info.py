#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: interface_info
short_description: Information module for Interface
description:
  - Get all Interface.
  - Get list of all properties & operations valid for
    an interface.
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
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices
      LegitOperationsForInterface
    description: Complete reference of the LegitOperationsForInterface
      API.
    link: https://developer.cisco.com/docs/dna-center/#!legit-operations-for-interface
notes:
  - SDK Method used are
    devices.Devices.legit_operations_for_interface,
  - Paths used are
    get /dna/intent/api/v1/interface/{interfaceUuid}/legit-operation,
"""

EXAMPLES = r"""
---
- name: Get all Interface
  cisco.catalystcenter.interface_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    interfaceUuid: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
