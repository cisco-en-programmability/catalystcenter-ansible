#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: users_external_authentication_info
short_description: Information module for Users External Authentication Info
description:
- This module represents an alias of the module users_external_authentication_v1_info
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for User and Roles GetExternalAuthenticationSettingAPIV1
  description: Complete reference of the GetExternalAuthenticationSettingAPIV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-external-authentication-setting-api
notes:
  - SDK Method used are
    user_and_roles.UserandRoles.get_external_authentication_setting_api_v1,

  - Paths used are
    get /dna/system/api/v1/users/external-authentication,
  - It should be noted that this module is an alias of users_external_authentication_v1_info

"""

EXAMPLES = r"""
- name: Get all Users External Authentication Info
  cisco.catalystcenter.users_external_authentication_info:
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
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "external-authentication-flag": [
        {
          "enabled": true
        }
      ]
    }
"""
