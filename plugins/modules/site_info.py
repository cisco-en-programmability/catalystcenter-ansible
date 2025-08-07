#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: site_info
short_description: Information module for Site
description:
  - Get all Site.
  - Get sites by site-name-hierarchy or siteId or type.
    List all sites if these parameters are not given
    as an input.
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
      - Name query parameter. Site name hierarchy (E.g
        Global/USA/CA).
    type: str
  siteId:
    description:
      - SiteId query parameter. Site Id.
    type: str
  type:
    description:
      - Type query parameter. Site type (Ex area, building,
        floor).
    type: str
  offset:
    description:
      - Offset query parameter. Offset/starting index
        for pagination. Indexed from 1.
    type: int
  limit:
    description:
      - Limit query parameter. Number of sites to be
        listed.
    type: int
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sites GetSite
    description: Complete reference of the GetSite API.
    link: https://developer.cisco.com/docs/dna-center/#!get-site
notes:
  - SDK Method used are
    sites.Sites.get_site,
  - Paths used are
    get /dna/intent/api/v1/site,
"""

EXAMPLES = r"""
---
- name: Get all Site
  cisco.catalystcenter.site_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
    name: string
    siteId: string
    type: string
    offset: 0
    limit: 0
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
