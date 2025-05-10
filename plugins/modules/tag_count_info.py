#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: tag_count_info
short_description: Information module for Tag Count Info
description:
  - This module represents an alias of the module tag_count_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  name:
    description:
      - Name query parameter.
    type: str
  nameSpace:
    description:
      - NameSpace query parameter.
    type: str
  attributeName:
    description:
      - AttributeName query parameter.
    type: str
  size:
    description:
      - Size query parameter. Size in kilobytes(KB).
    type: str
  systemTag:
    description:
      - SystemTag query parameter.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Tag GetTagCountV1
    description: Complete reference of the GetTagCountV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-tag-count
notes:
  - SDK Method used are tag.Tag.get_tag_count_v1,
  - Paths used are get /dna/intent/api/v1/tag/count,
  - It should be noted that this module is an alias of tag_count_v1_info
"""
EXAMPLES = r"""
- name: Get all Tag Count Info
  cisco.catalystcenter.tag_count_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    name: string
    nameSpace: string
    attributeName: string
    size: string
    systemTag: string
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
      "response": 0
    }
"""
