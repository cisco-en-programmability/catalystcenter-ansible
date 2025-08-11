#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: security_threats_type_info
short_description: Information module for Security Threats
  Type
description:
  - Get all Security Threats Type.
  - Intent API to fetch all threat types defined.
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
notes:
  - SDK Method used are
    devices.Devices.get_threat_types,
  - Paths used are
    get /dna/intent/api/v1/security/threats/type,
"""

EXAMPLES = r"""
---
- name: Get all Security Threats Type
  cisco.catalystcenter.security_threats_type_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "value": 0,
        "name": "string",
        "label": "string",
        "isCustom": true,
        "isDeleted": true
      }
    ]
"""
