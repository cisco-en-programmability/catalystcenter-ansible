#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: users_external_servers_aaa_attribute_info
short_description: Information module for Users External Servers Aaa Attribute Info
description:
  - This module represents an alias of the module users_external_servers_aaa_attribute_v1_info
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
  - name: Cisco DNA Center documentation for User and Roles GetAAAAttributeAPIV1
    description: Complete reference of the GetAAAAttributeAPIV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-aaa-attribute-api
notes:
  - SDK Method used are user_and_roles.UserandRoles.get_aaa_attribute_api_v1,
  - Paths used are get /dna/system/api/v1/users/external-servers/aaa-attribute,
  - It should be noted that this module is an alias of users_external_servers_aaa_attribute_v1_info
"""
EXAMPLES = r"""
- name: Get all Users External Servers Aaa Attribute Info
  cisco.catalystcenter.users_external_servers_aaa_attribute_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
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
      "aaa-attributes": [
        {
          "attributeName": "string"
        }
      ]
    }
"""
