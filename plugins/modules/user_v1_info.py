#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: user_v1_info
short_description: Information module for User V1
description:
  - Get all User V1.
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
        InvokeSource query parameter. The source that invokes this API. The value
        of this query parameter must be
        set to "external".
    type: str
  authSource:
    description:
      - >
        AuthSource query parameter. The source that authenticates the user. The value
        of this query parameter can be
        set to "internal" or "external". If not provided, then all users will be returned
        in the response.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for User and Roles GetUsersAPIV1
    description: Complete reference of the GetUsersAPIV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-users-api
notes:
  - SDK Method used are user_and_roles.UserandRoles.get_users_api_v1,
  - Paths used are get /dna/system/api/v1/user,
"""
EXAMPLES = r"""
- name: Get all User V1
  cisco.catalystcenter.user_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    invokeSource: string
    authSource: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
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
          "username": "string"
        }
      ]
    }
"""
