#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: connection_modesetting_info
short_description: Information module for Connection Modesetting Info
description:
  - This module represents an alias of the module connection_modesetting_v1_info
version_added: '6.17.0'
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
  - name: Cisco DNA Center documentation for Licenses RetrievesCSSMConnectionModeV1
    description: Complete reference of the RetrievesCSSMConnectionModeV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-cssm-connection-mode
notes:
  - SDK Method used are licenses.Licenses.retrieves_c_s_s_m_connection_mode_v1,
  - Paths used are get /dna/intent/api/v1/connectionModeSetting,
  - It should be noted that this module is an alias of connection_modesetting_v1_info
"""
EXAMPLES = r"""
- name: Get all Connection Modesetting Info
  cisco.catalystcenter.connection_modesetting_info:
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
