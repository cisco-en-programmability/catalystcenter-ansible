#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: tag_member_type_info
short_description: Information module for Tag Member
  Type
description:
  - Get all Tag Member Type.
  - Returns list of supported resource types.
version_added: '3.1.0'
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
seealso:
  - name: Cisco DNA Center documentation for Tag GetTagResourceTypes
    description: Complete reference of the GetTagResourceTypes
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-tag-resource-types
notes:
  - SDK Method used are
    tag.Tag.get_tag_resource_types,
  - Paths used are
    get /dna/intent/api/v1/tag/member/type,
"""

EXAMPLES = r"""
---
- name: Get all Tag Member Type
  cisco.catalystcenter.tag_member_type_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": [
        "string"
      ]
    }
"""
