#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: roles_v2_info
short_description: Information module for Roles V2
description:
  - Get all Roles V2.
  - Get Roles V2 by id. - > Get a role in the system v2-.This API is the successor to the v1 get role API GET /dna/system/api/v1/role/${id}.
    It can be used to get a role that exists in the system, regardless of whether it was created using the v1 Add role API
    POST /dna/system/api/v1/role or the v2 Add role API POST /dna/system/api/v2/roles . - > Get all roles in the system v2-.This
    API is the successor to the v1 Get roles API GET /dna/system/api/v1/role. It can be used to get all roles that exist in
    the system, regardless of whether it was created using the v1 Add role API POST /dna/system/api/v1/role or the v2 Add
    role API POST /dna/system/api/v2/roles .
version_added: '2.3.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Id of the role to look up.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for User and Roles GetRole
    description: Complete reference of the GetRole API.
    link: https://developer.cisco.com/docs/dna-center/#!get-role
  - name: Cisco Catalyst Center documentation for User and Roles GetRoles
    description: Complete reference of the GetRoles API.
    link: https://developer.cisco.com/docs/dna-center/#!get-roles
notes:
  - SDK Method used are
    user_and_roles.UserAndRoles.get_role,
    user_and_roles.UserAndRoles.get_roles,
  - Paths used are
    get /dna/system/api/v2/roles,
    get /dna/system/api/v2/roles/{id},
"""

EXAMPLES = r"""
---
- name: Get all Roles V2
  cisco.catalystcenter.roles_v2_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
- name: Get Roles V2 by id
  cisco.catalystcenter.roles_v2_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: application/json
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string",
      "name": "string",
      "description": "string",
      "permissions": [
        {
          "privilege": "string",
          "id": "string"
        }
      ],
      "type": "string",
      "version": "string",
      "meta": {
        "created": "string",
        "createdBy": "string",
        "lastModified": "string",
        "lastModifiedBy": "string"
      }
    }
"""
