#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: event_config_connector_types_info
short_description: Information module for Event Config Connector Types Info
description:
  - This module represents an alias of the module event_config_connector_types_v1_info
version_added: '6.0.0'
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
  - name: Cisco DNA Center documentation for Event Management GetConnectorTypesV1
    description: Complete reference of the GetConnectorTypesV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-connector-types
notes:
  - SDK Method used are event_management.EventManagement.get_connector_types_v1,
  - Paths used are get /dna/system/api/v1/event/config/connector-types,
  - It should be noted that this module is an alias of event_config_connector_types_v1_info
"""
EXAMPLES = r"""
- name: Get all Event Config Connector Types Info
  cisco.catalystcenter.event_config_connector_types_info:
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
  type: list
  elements: dict
  sample: >
    [
      {
        "connectorType": "string",
        "displayName": "string",
        "isDefaultSupported": true,
        "isCustomConnector": true
      }
    ]
"""
