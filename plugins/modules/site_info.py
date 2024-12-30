#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: site_info
short_description: Information module for Site Info
description:
- This module represents an alias of the module site_v1_info
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
    - Name query parameter. Site name hierarchy (E.g Global/USA/CA).
    type: str
  siteId:
    description:
    - SiteId query parameter. Site Id.
    type: str
  type:
    description:
    - Type query parameter. Site type (Ex area, building, floor).
    type: str
  offset:
    description:
    - Offset query parameter. Offset starting index for pagination. Indexed from 1.
    type: int
  limit:
    description:
    - Limit query parameter. Number of sites to be listed.
    type: int
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Sites GetSiteV1
  description: Complete reference of the GetSiteV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-site
notes:
  - SDK Method used are
    sites.Sites.get_site_v1,

  - Paths used are
    get /dna/intent/api/v1/site,
  - It should be noted that this module is an alias of site_v1_info

"""

EXAMPLES = r"""
- name: Get all Site Info
  cisco.catalystcenter.site_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    name: string
    siteId: string
    type: string
    offset: 0
    limit: 0
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "parentId": "string",
        "name": "string",
        "additionalInfo": [
          "string"
        ],
        "siteHierarchy": "string",
        "siteNameHierarchy": "string",
        "instanceTenantId": "string",
        "id": "string"
      }
    ]
"""
