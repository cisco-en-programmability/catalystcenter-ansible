#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: users_external_servers_v1_info
short_description: Information module for Users External Servers V1
description:
  - Get all Users External Servers V1.
  - Get external users authentication servers.
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
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for User and Roles GetExternalAuthenticationServersAPIV1
    description: Complete reference of the GetExternalAuthenticationServersAPIV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-external-authentication-servers-api
notes:
  - SDK Method used are user_and_roles.UserandRoles.get_external_authentication_servers_api_v1,
  - Paths used are get /dna/system/api/v1/users/external-servers,
"""
EXAMPLES = r"""
- name: Get all Users External Servers V1
  cisco.catalystcenter.users_external_servers_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    invokeSource: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "aaa-servers": [
        {
          "accountingPort": 0,
          "retries": 0,
          "protocol": "string",
          "socketTimeout": 0,
          "serverIp": "string",
          "sharedSecret": "string",
          "serverId": "string",
          "authenticationPort": 0,
          "aaaAttribute": "string",
          "role": "string"
        }
      ]
    }
"""
