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
  - Get Roles V2 by id.
  - Get a role in the system v2-.
  - Get all roles in the system v2-.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Id of the role to look up.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for User and Roles GetRoleV2
    description: Complete reference of the GetRoleV2 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-role-v-2
  - name: Cisco DNA Center documentation for User and Roles GetRolesV2
    description: Complete reference of the GetRolesV2 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-roles-v-2
notes:
  - SDK Method used are
    userand_roles.UserandRoles.get_role_v2,
    userand_roles.UserandRoles.get_roles_v2,
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
    id: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
