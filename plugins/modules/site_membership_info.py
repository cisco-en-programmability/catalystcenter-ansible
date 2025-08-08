#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: site_membership_info
short_description: Information module for Site Membership
description:
  - Get Site Membership by id.
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
      - SiteId path parameter. Site id to retrieve device
        associated with the site.
    type: str
  offset:
    description:
      - Offset query parameter. Offset/starting row.
    type: float
  limit:
    description:
      - Limit query parameter. Number of sites to be
        retrieved.
    type: float
  deviceFamily:
    description:
      - DeviceFamily query parameter. Device family
        name.
    type: str
  serialNumber:
    description:
      - SerialNumber query parameter. Device serial
        number.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sites GetMembership
    description: Complete reference of the GetMembership
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-membership
notes:
  - SDK Method used are
    sites.Sites.get_membership,
  - Paths used are
    get /dna/intent/api/v1/membership/{siteId},
"""

EXAMPLES = r"""
---
- name: Get Site Membership by id
  cisco.catalystcenter.site_membership_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
    offset: 0
    limit: 0
    deviceFamily: string
    serialNumber: string
    siteId: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
