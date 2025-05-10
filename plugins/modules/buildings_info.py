#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: buildings_info
short_description: Information module for Buildings Info
description:
  - This module represents an alias of the module buildings_v2_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Building Id.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Site Design GetsABuildingV2
    description: Complete reference of the GetsABuildingV2 API.
    link: https://developer.cisco.com/docs/dna-center/#!gets-a-building
notes:
  - SDK Method used are site_design.SiteDesign.gets_a_building_v2,
  - Paths used are get /dna/intent/api/v2/buildings/{id},
  - It should be noted that this module is an alias of buildings_v2_info
"""
EXAMPLES = r"""
- name: Get Buildings Info by id
  cisco.catalystcenter.buildings_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    id: string
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
        "parentId": "string",
        "name": "string",
        "latitude": 0,
        "longitude": 0,
        "address": "string",
        "country": "string",
        "type": "string"
      }
    }
"""
