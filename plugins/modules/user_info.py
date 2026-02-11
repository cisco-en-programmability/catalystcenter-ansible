#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: user_info
short_description: Information module for User
description:
  - Get all User.
  - Get all users in the system.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  authSource:
    description:
      - >
        AuthSource query parameter. The source that authenticates the user. The value of this query parameter
        can be set to "internal" or "external". If not provided, then all users will be returned in the
        response.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for User and Roles GetUsers
    description: Complete reference of the GetUsers API.
    link: https://developer.cisco.com/docs/dna-center/#!get-users
notes:
  - SDK Method used are
    userand_roles.UserandRoles.get_users,
  - Paths used are
    get /dna/system/api/v1/user,
"""

EXAMPLES = r"""
---
- name: Get all User
  cisco.catalystcenter.user_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    authSource: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "users": [
        {
          "firstName": "string",
          "lastName": "string",
          "authSource": "string",
          "passphraseUpdateTime": "string",
          "roleList": [
            "string"
          ],
          "userId": "string",
          "email": "string",
          "username": "string",
          "rds": [
            "string"
          ]
        }
      ]
    }
"""
