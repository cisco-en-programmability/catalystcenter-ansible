#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: auth_token_create_v1
short_description: Resource module for Auth Token Create V1
description:
- Manage operation create of the resource Auth Token Create V1.
- >
   API to obtain an access token, which remains valid for 1 hour. The token obtained using this API is required to be
   set as value to the X-Auth-Token HTTP Header for all API calls to Cisco DNA Center.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options: {}
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Authentication AuthenticationAPIV1
  description: Complete reference of the AuthenticationAPIV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!authentication-api
notes:
  - SDK Method used are
    authentication.Authentication.authentication_api_v1,

  - Paths used are
    post /dna/system/api/v1/auth/token,

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.auth_token_create_v1:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "Token": "string"
    }
"""
