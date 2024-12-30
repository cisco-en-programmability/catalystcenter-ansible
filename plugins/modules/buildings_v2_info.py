#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: buildings_v2_info
short_description: Information module for Buildings V2
description:
- Get Buildings V2 by id.
- Gets a building in the network hierarchy.
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
  - SDK Method used are
    site_design.SiteDesign.gets_a_building_v2,

  - Paths used are
    get /dna/intent/api/v2/buildings/{id},

"""

EXAMPLES = r"""
- name: Get Buildings V2 by id
  cisco.catalystcenter.buildings_v2_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
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
