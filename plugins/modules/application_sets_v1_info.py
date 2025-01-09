#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: application_sets_v1_info
short_description: Information module for Application Sets V1
description:
- Get all Application Sets V1.
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
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Application Policy GetApplicationSetsV1
  description: Complete reference of the GetApplicationSetsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-application-sets
notes:
  - SDK Method used are
    application_policy.ApplicationPolicy.get_application_sets_v1,

  - Paths used are
    get /dna/intent/api/v1/application-policy-application-set,

"""

EXAMPLES = r"""
- name: Get all Application Sets V1
  cisco.catalystcenter.application_sets_v1_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    offset: 0
    limit: 0
    name: string
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
        "id": "string",
        "identitySource": {
          "id": "string",
          "type": "string"
        },
        "name": "string"
      }
    ]
"""
