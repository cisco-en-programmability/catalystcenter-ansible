#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: users_external_authentication
short_description: Resource module for Users External Authentication
description:
- Manage operation create of the resource Users External Authentication.
- Enable or disable external authentication on Cisco CATALYST Center System.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  enable:
    description: Enable/disable External Authentication.
    type: bool
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for User and Roles ManageExternalAuthenticationSettingAPIV1
  description: Complete reference of the ManageExternalAuthenticationSettingAPIV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!manage-external-authentication-setting-api-v-1
notes:
  - SDK Method used are
    user_and_roles.UserandRoles.manage_external_authentication_setting_api_v1,

  - Paths used are
    post /dna/system/api/v1/users/external-authentication,

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.users_external_authentication:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    enable: true

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "message": "string"
    }
"""
