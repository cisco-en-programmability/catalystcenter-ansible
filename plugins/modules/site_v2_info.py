#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: site_v2_info
short_description: Information module for Site V2
description:
  - Get all Site V2.
  - >
    API to get sites by site-name-hierarchy or siteId or type. List all sites if these
    parameters are not given as an
    input.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  groupNameHierarchy:
    description:
      - GroupNameHierarchy query parameter. Site name hierarchy (E.g. Global/USA/CA).
    type: str
  id:
    description:
      - Id query parameter. Site Id.
    type: str
  type:
    description:
      - Type query parameter. Site type (Acceptable values area, building, floor).
    type: str
  offset:
    description:
      - Offset query parameter. Offset starting index for pagination.
    type: str
  limit:
    description:
      - Limit query parameter. Number of sites to be listed. Default and max supported
        value is 500.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sites GetSiteV2
    description: Complete reference of the GetSiteV2 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-site
notes:
  - SDK Method used are sites.Sites.get_site_v2,
  - Paths used are get /dna/intent/api/v2/site,
"""
EXAMPLES = r"""
- name: Get all Site V2
  cisco.catalystcenter.site_v2_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    groupNameHierarchy: string
    id: string
    type: string
    offset: string
    limit: string
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
        "groupTypeList": [
          "string"
        ],
        "groupHierarchy": "string",
        "additionalInfo": [
          {
            "nameSpace": "string",
            "attributes": {
              "addressInheritedFrom": "string",
              "type": "string",
              "country": "string",
              "address": "string",
              "latitude": "string",
              "longitude": "string"
            }
          }
        ],
        "groupNameHierarchy": "string",
        "name": "string",
        "instanceTenantId": "string",
        "id": "string"
      }
    ]
"""
