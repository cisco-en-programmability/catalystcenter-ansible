#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_config_connector_types_info
short_description: Information module for Event Config Connector Types
description:
  - Get all Event Config Connector Types.
  - Get the list of connector types.
version_added: '6.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Event Management GetConnectorTypes
    description: Complete reference of the GetConnectorTypes API.
    link: https://developer.cisco.com/docs/dna-center/#!get-connector-types
notes:
  - SDK Method used are
    event_management.EventManagement.get_connector_types,
  - Paths used are
    get /dna/system/api/v1/event/config/connector-types,
"""

EXAMPLES = r"""
---
- name: Get all Event Config Connector Types
  cisco.catalystcenter.event_config_connector_types_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
dnac_response:
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
