#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: security_service_insertions_info
short_description: Information module for Security Service Insertions
description:
  - Get all Security Service Insertions.
  - Get Security Service Insertions by id.
  - Retrieves a list of all Security Service Insertions SSIs configured across.
  - Retrieves the details of a specific Security Service Insertion SSI by its ID.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. The unique identifier of the Security Service Insertion (SSI).
    type: str
  limit:
    description:
      - >
        Limit query parameter. Maximum number of records to return. Default value is 100, minimum value is 1 and
        maximum value is 100.
    type: int
  offset:
    description:
      - Offset query parameter. Starting record for pagination. The first record is numbered 1.
    type: int
  order:
    description:
      - >
        Order query parameter. The sorting order for the response can be specified as either ascending (asc) or
        descending (desc). The default order is ascending (asc).
    type: str
  fabricSiteName:
    description:
      - >
        FabricSiteName query parameter. Filter by fabric site name (supports partial search). For example,
        searching for "London" will match "London fabric site", etc.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for SDA SecurityServiceInsertionById
    description: Complete reference of the SecurityServiceInsertionById API.
    link: https://developer.cisco.com/docs/dna-center/#!security-service-insertion-by-id
  - name: Cisco Catalyst Center documentation for SDA SecurityServiceInsertions
    description: Complete reference of the SecurityServiceInsertions API.
    link: https://developer.cisco.com/docs/dna-center/#!security-service-insertions
notes:
  - SDK Method used are
    sda.Sda.security_service_insertion_by_id,
    sda.Sda.security_service_insertions,
  - Paths used are
    get /dna/intent/api/v1/securityServiceInsertions,
    get /dna/intent/api/v1/securityServiceInsertions/{id},
"""

EXAMPLES = r"""
---
- name: Get all Security Service Insertions
  cisco.catalystcenter.security_service_insertions_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    limit: 0
    offset: 0
    order: string
    fabricSiteName: string
  register: result
- name: Get Security Service Insertions by id
  cisco.catalystcenter.security_service_insertions_info:
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
      "response": {
        "id": "string",
        "siteId": "string",
        "fabricSiteName": "string",
        "virtualNetworks": [
          {
            "id": "string",
            "name": "string",
            "devices": [
              {
                "id": "string",
                "hostName": "string",
                "layer3Handoffs": [
                  {
                    "id": "string",
                    "firewallIpV4AddressWithMask": "string"
                  }
                ]
              }
            ]
          }
        ]
      },
      "version": "string"
    }
"""
