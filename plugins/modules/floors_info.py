#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: floors_info
short_description: Information module for Floors
description:
  - Get Floors by id.
  - Gets a floor in the network hierarchy.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Floor Id.
    type: str
  _unitsOfMeasure:
    description:
      - _unitsOfMeasure query parameter.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Site Design GetsAFloor
    description: Complete reference of the GetsAFloor API.
    link: https://developer.cisco.com/docs/dna-center/#!gets-a-floor
notes:
  - SDK Method used are
    site_design.SiteDesign.gets_a_floor,
  - Paths used are
    get /dna/intent/api/v2/floors/{id},
"""

EXAMPLES = r"""
---
- name: Get Floors by id
  cisco.catalystcenter.floors_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    _unitsOfMeasure: str
    id: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {},
      "version": "string"
    }
"""
