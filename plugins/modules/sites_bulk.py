#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sites_bulk
short_description: Resource module for Sites Bulk
description:
  - Manage operation create of the resource Sites Bulk. - > Create area/building/floor together in bulk. If site already exist,
    then that will be ignored. Sites in the request payload need not to be ordered.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  payload:
    description: Sites Bulk's payload.
    elements: dict
    suboptions:
      country:
        description: Country name.
        type: str
      floorNumber:
        description: Floor number.
        type: int
      height:
        description: Floor height.
        type: float
      length:
        description: Floor length.
        type: float
      name:
        description: Floor name.
        type: str
      parentNameHierarchy:
        description: Parent hierarchical name.
        type: str
      rfModel:
        description: RF Model.
        type: str
      type:
        description: Site Type.
        type: str
      unitsOfMeasure:
        description: Unit of measure for length, width, and height.
        type: str
      width:
        description: Floor width.
        type: float
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Site Design CreateSites
    description: Complete reference of the CreateSites API.
    link: https://developer.cisco.com/docs/dna-center/#!create-sites
notes:
  - SDK Method used are
    site_design.SiteDesign.create_sites,
  - Paths used are
    post /dna/intent/api/v1/sites/bulk,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.sites_bulk:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    payload:
      - country: string
        floorNumber: 0
        height: 0
        length: 0
        name: string
        parentNameHierarchy: string
        rfModel: string
        type: string
        unitsOfMeasure: {}
        width: 0
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
