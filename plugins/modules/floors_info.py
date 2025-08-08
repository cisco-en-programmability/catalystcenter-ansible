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
      - Id path parameter. Floor Id.
    type: str
  _unitsOfMeasure:
    description:
      - _unitsOfMeasure query parameter. Floor units
        of measure.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Site Design
      GetsAFloorV2
    description: Complete reference of the GetsAFloorV2
      API.
    link: https://developer.cisco.com/docs/dna-center/#!gets-a-floor-v-2
notes:
  - SDK Method used are
    site_design.SiteDesign.gets_a_floor_v2,
  - Paths used are
    get /dna/intent/api/v2/floors/{id},
"""

EXAMPLES = r"""
---
- name: Get Floors by id
  cisco.catalystcenter.floors_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
    _unitsOfMeasure: string
    id: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "parentId": "string",
        "name": "string",
        "floorNumber": 0,
        "rfModel": "string",
        "width": 0,
        "length": 0,
        "height": 0,
        "unitsOfMeasure": "string",
        "type": "string",
        "id": "string",
        "nameHierarchy": "string",
        "siteHierarchyId": "string"
      }
    }
"""
