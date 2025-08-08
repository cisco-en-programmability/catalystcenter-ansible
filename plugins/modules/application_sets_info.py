#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: application_sets_info
short_description: Information module for Application
  Sets
description:
  - Get all Application Sets.
  - Get appllication-sets by offset/limit or by name.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  offset:
    description:
      - Offset query parameter.
    type: float
  limit:
    description:
      - Limit query parameter.
    type: float
  name:
    description:
      - Name query parameter.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Application
      Policy GetApplicationSets
    description: Complete reference of the GetApplicationSets
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-application-sets
notes:
  - SDK Method used are
    application_policy.ApplicationPolicy.get_application_sets,
  - Paths used are
    get /dna/intent/api/v1/application-policy-application-set,
"""

EXAMPLES = r"""
---
- name: Get all Application Sets
  cisco.catalystcenter.application_sets_info:
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
    name: string
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
        "id": "string",
        "identitySource": {
          "id": "string",
          "type": "string"
        },
        "name": "string"
      }
    ]
"""
