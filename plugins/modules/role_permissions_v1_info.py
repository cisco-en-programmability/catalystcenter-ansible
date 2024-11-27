#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: role_permissions_v1_info
short_description: Information module for Role Permissions V1
description:
- Get all Role Permissions V1.
- Get permissions for a role from Cisco DNA Center System.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for User and Roles GetPermissionsAPIV1
  description: Complete reference of the GetPermissionsAPIV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-permissions-api
notes:
  - SDK Method used are
    user_and_roles.UserandRoles.get_permissions_api_v1,

  - Paths used are
    get /dna/system/api/v1/role/permissions,

"""

EXAMPLES = r"""
- name: Get all Role Permissions V1
  cisco.catalystcenter.role_permissions_v1_info:
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
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
