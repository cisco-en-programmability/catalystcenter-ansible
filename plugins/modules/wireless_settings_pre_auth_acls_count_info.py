#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_settings_pre_auth_acls_count_info
short_description: Information module for Wireless Settings Pre Auth Acls Count
description:
  - Get all Wireless Settings Pre Auth Acls Count. - > This API allows users to retrieve the total count of Pre-Auth ACLs
    configured in the system. This API allows users to retrieve the total count of Pre-Auth ACLs configured in the system.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless GetPreAuthACLCount
    description: Complete reference of the GetPreAuthACLCount API.
    link: https://developer.cisco.com/docs/dna-center/#!get-pre-auth-acl-count
notes:
  - SDK Method used are
    wireless.Wireless.get_pre_auth_acl_count,
  - Paths used are
    get /dna/intent/api/v1/wirelessSettings/preAuthAcls/count,
"""

EXAMPLES = r"""
---
- name: Get all Wireless Settings Pre Auth Acls Count
  cisco.catalystcenter.wireless_settings_pre_auth_acls_count_info:
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
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "count": 0
      },
      "version": "string"
    }
"""
