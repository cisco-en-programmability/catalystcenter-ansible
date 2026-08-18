#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sites_info
short_description: Information module for Sites
description:
  - Get all Sites.
  - Get Sites by id.
  - Get a site.
  - Get sites.
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
      - >
        Id path parameter. Site Id. Represents a unique identifier that corresponds to one of the following -
        Global Id, Area Id, Building Id, Floor Id.
    type: str
  name:
    description:
      - Name query parameter. Site name.
    type: str
  nameHierarchy:
    description:
      - NameHierarchy query parameter. Site name hierarchy.
    type: str
  type:
    description:
      - Type query parameter. Site type.
    type: str
  _unitsOfMeasure:
    description:
      - _unitsOfMeasure query parameter.
    type: str
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: int
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Site Design GetASite
    description: Complete reference of the GetASite API.
    link: https://developer.cisco.com/docs/dna-center/#!get-a-site
  - name: Cisco Catalyst Center documentation for Site Design GetSites
    description: Complete reference of the GetSites API.
    link: https://developer.cisco.com/docs/dna-center/#!get-sites
notes:
  - SDK Method used are
    site_design.SiteDesign.get_a_site,
    site_design.SiteDesign.get_sites,
  - Paths used are
    get /dna/intent/api/v1/sites,
    get /dna/intent/api/v1/sites/{id},
"""

EXAMPLES = r"""
---
- name: Get all Sites
  cisco.catalystcenter.sites_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    name: string
    nameHierarchy: string
    type: string
    _unitsOfMeasure: str
    offset: 1
    limit: 0
  register: result
- name: Get Sites by id
  cisco.catalystcenter.sites_info:
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
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {},
      "version": "string"
    }
"""
