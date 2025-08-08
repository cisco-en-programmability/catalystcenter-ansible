#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: connection_modesetting_info
short_description: Information module for Connection
  Mode Setting
description:
  - Get all Connection Mode Setting.
  - Retrieves Cisco Smart Software Manager CSSM connection
    mode setting.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Licenses
      RetrievesCSSMConnectionMode
    description: Complete reference of the RetrievesCSSMConnectionMode
      API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-cssm-connection-mode
notes:
  - SDK Method used are
    licenses.Licenses.retrieves_c_s_s_m_connection_mode,
  - Paths used are
    get /dna/intent/api/v1/connectionModeSetting,
"""

EXAMPLES = r"""
---
- name: Get all Connection Mode Setting
  cisco.catalystcenter.connection_mode_setting_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "connectionMode": "string",
        "parameters": {
          "onPremiseHost": "string",
          "smartAccountName": "string",
          "clientId": "string"
        }
      },
      "version": "string"
    }
"""
