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
  invokeSource:
    description:
      - >
        InvokeSource query parameter. The source that
        invokes this API. The value of this query parameter
        must be set to "external".
    type: str
  authSource:
    description:
      - >
        AuthSource query parameter. The source that
        authenticates the user. The value of this query
        parameter can be set to "internal" or "external".
        If not provided, then all users will be returned
        in the response.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for User and
      Roles GetUsersAPI
    description: Complete reference of the GetUsersAPI
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-users-api
notes:
  - SDK Method used are
    userand_roles.UserandRoles.get_users_api,
  - Paths used are
    get /dna/system/api/v1/user,
"""

EXAMPLES = r"""
---
- name: Get all User
  cisco.catalystcenter.user_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
    invokeSource: string
    authSource: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
          "username": "string"
        }
      ]
    }
"""
