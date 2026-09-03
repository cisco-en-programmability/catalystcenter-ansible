#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: role_permissions_info
short_description: Information module for Role Permissions
description:
  - Get all Role Permissions.
  - Get permissions for a role in the system.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for User and Roles GetPermissionsAPI
    description: Complete reference of the GetPermissionsAPI API.
    link: https://developer.cisco.com/docs/dna-center/#!get-permissions-api
notes:
  - SDK Method used are
    user_and_roles.UserAndRoles.get_permissions_api,
  - Paths used are
    get /dna/system/api/v1/role/permissions,
"""

EXAMPLES = r"""
---
- name: Get all Role Permissions
  cisco.catalystcenter.role_permissions_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "resource-types": [
        {
          "type": "string",
          "displayName": "string",
          "description": "string",
          "defaultPermission": "string"
        }
      ]
    }
"""
