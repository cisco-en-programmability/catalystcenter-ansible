#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: security_threats_rogue_allowed_list_info
short_description: Information module for Security Threats Rogue Allowed-List
description:
  - Get all Security Threats Rogue Allowed-List.
  - Intent API to fetch all the allowed mac addresses in the system.
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  offset:
    description:
      - Offset query parameter. The offset of the first item in the collection to return.
    type: int
  limit:
    description:
      - >
        Limit query parameter. The maximum number of entries to return. If the value exceeds the total count,
        then the maximum entries will be returned.
    type: int
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Devices GetAllowedMacAddress
    description: Complete reference of the GetAllowedMacAddress API.
    link: https://developer.cisco.com/docs/dna-center/#!get-allowed-mac-address
notes:
  - SDK Method used are
    devices.Devices.get_allowed_mac_address,
  - Paths used are
    get /dna/intent/api/v1/security/threats/rogue/allowed-list,
"""

EXAMPLES = r"""
---
- name: Get all Security Threats Rogue Allowed-List
  cisco.catalystcenter.security_threats_rogue_allowed_list_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    offset: 0
    limit: 0
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "macAddress": "string",
        "category": 0,
        "lastModified": 0
      }
    ]
"""
