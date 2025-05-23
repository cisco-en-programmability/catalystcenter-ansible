#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: site_membership_v1_info
short_description: Information module for Site Membership V1
description:
  - Get Site Membership V1 by id.
  - Getting the site children details and device details.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  siteId:
    description:
      - SiteId path parameter. Site id to retrieve device associated with the site.
    type: str
  offset:
    description:
      - Offset query parameter. Offset starting row.
    type: float
  limit:
    description:
      - Limit query parameter. Number of sites to be retrieved.
    type: float
  deviceFamily:
    description:
      - DeviceFamily query parameter. Device family name.
    type: str
  serialNumber:
    description:
      - SerialNumber query parameter. Device serial number.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sites GetMembershipV1
    description: Complete reference of the GetMembershipV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-membership
notes:
  - SDK Method used are sites.Sites.get_membership_v1,
  - Paths used are get /dna/intent/api/v1/membership/{siteId},
"""
EXAMPLES = r"""
- name: Get Site Membership V1 by id
  cisco.catalystcenter.site_membership_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    offset: 0
    limit: 0
    deviceFamily: string
    serialNumber: string
    siteId: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "site": {
        "response": [
          {}
        ],
        "version": "string"
      },
      "device": [
        {
          "response": [
            {}
          ],
          "version": "string",
          "siteId": "string"
        }
      ]
    }
"""
