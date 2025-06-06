#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: tag_member_type_v1_info
short_description: Information module for Tag Member Type V1
description:
  - Get all Tag Member Type V1.
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
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Tag GetTagResourceTypesV1
    description: Complete reference of the GetTagResourceTypesV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-tag-resource-types
notes:
  - SDK Method used are tag.Tag.get_tag_resource_types_v1,
  - Paths used are get /dna/intent/api/v1/tag/member/type,
"""
EXAMPLES = r"""
- name: Get all Tag Member Type V1
  cisco.catalystcenter.tag_member_type_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
