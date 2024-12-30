#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: floors_v2_info
short_description: Information module for Floors V2
description:
- Get Floors V2 by id.
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
    - _unitsOfMeasure query parameter. Floor units of measure.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Site Design GetsAFloorV2
  description: Complete reference of the GetsAFloorV2 API.
  link: https://developer.cisco.com/docs/dna-center/#!gets-a-floor
notes:
  - SDK Method used are
    site_design.SiteDesign.gets_a_floor_v2,

  - Paths used are
    get /dna/intent/api/v2/floors/{id},

"""

EXAMPLES = r"""
- name: Get Floors V2 by id
  cisco.catalystcenter.floors_v2_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    _unitsOfMeasure: string
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
        "floorNumber": 0,
        "rfModel": "string",
        "width": 0,
        "length": 0,
        "height": 0,
        "unitsOfMeasure": "string",
        "type": "string",
        "id": "string",
        "nameHierarchy": "string"
      }
    }
"""
