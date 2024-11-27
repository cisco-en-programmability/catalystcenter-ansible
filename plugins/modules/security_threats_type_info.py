#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: security_threats_type_info
short_description: Information module for Security Threats Type Info
description:
- This module represents an alias of the module security_threats_type_v1_info
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- catalystcentersdk >= 2.3.7.6
- python >= 3.5
notes:
  - SDK Method used are
    devices.Devices.get_threat_types_v1,

  - Paths used are
    get /dna/intent/api/v1/security/threats/type,
  - It should be noted that this module is an alias of security_threats_type_v1_info

"""

EXAMPLES = r"""
- name: Get all Security Threats Type Info
  cisco.catalystcenter.security_threats_type_info:
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
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
