#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: interface_v1_info
short_description: Information module for Interface V1
description:
  - Get all Interface V1.
  - Get list of all properties & operations valid for an interface.
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
  - SDK Method used are devices.Devices.legit_operations_for_interface_v1,
  - Paths used are get /dna/intent/api/v1/interface/{interfaceUuid}/legit-operation,
"""
EXAMPLES = r"""
- name: Get all Interface V1
  cisco.catalystcenter.interface_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
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
