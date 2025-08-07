#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: security_service_insertions_id_info
short_description: Information module for Security Service
  Insertions Id
description:
  - Get Security Service Insertions Id by id.
  - Retrieves the details of a specific Security Service
    Insertion SSI by its ID.
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. The unique identifier of
        the Security Service Insertion (SSI).
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA SecurityServiceInsertionById
    description: Complete reference of the SecurityServiceInsertionById
      API.
    link: https://developer.cisco.com/docs/dna-center/#!security-service-insertion-by-id
notes:
  - SDK Method used are
    sda.Sda.security_service_insertion_by_id,
  - Paths used are
    get /dna/intent/api/v1/securityServiceInsertions/{id},
"""

EXAMPLES = r"""
---
- name: Get Security Service Insertions Id by id
  cisco.catalystcenter.security_service_insertions_id_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
