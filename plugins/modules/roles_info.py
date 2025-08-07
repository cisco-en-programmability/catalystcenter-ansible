#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: roles_info
short_description: Information module for Roles
description:
  - Get all Roles.
  - Get all roles in the system.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for User and
      Roles GetRolesAPI
    description: Complete reference of the GetRolesAPI
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-roles-api
notes:
  - SDK Method used are
    userand_roles.UserandRoles.get_roles_api,
  - Paths used are
    get /dna/system/api/v1/roles,
"""

EXAMPLES = r"""
---
- name: Get all Roles
  cisco.catalystcenter.roles_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "roles": [
        {
          "resourceTypes": [
            {
              "operations": [
                "string"
              ],
              "type": "string"
            }
          ],
          "meta": {
            "createdBy": "string",
            "created": "string",
            "lastModified": "string"
          },
          "roleId": "string",
          "name": "string",
          "description": "string",
          "type": "string"
        }
      ]
    }
"""
