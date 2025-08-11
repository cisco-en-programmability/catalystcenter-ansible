#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_syslog_config_info
short_description: Information module for Event Syslog
  Config
description:
  - Get all Event Syslog Config.
  - Get Syslog Destination.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  configId:
    description:
      - ConfigId query parameter. Config id of syslog
        server.
    type: str
  name:
    description:
      - Name query parameter. Name of syslog server.
    type: str
  protocol:
    description:
      - Protocol query parameter. Protocol of syslog
        server.
    type: str
  offset:
    description:
      - Offset query parameter. The number of syslog
        configuration's to offset in the resultset whose
        default value 0.
    type: float
  limit:
    description:
      - Limit query parameter. The number of syslog
        configuration's to limit in the resultset whose
        default value 10.
    type: float
  sortBy:
    description:
      - SortBy query parameter. SortBy field name.
    type: str
  order:
    description:
      - Order query parameter.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Event Management
      GetSyslogDestination
    description: Complete reference of the GetSyslogDestination
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-syslog-destination
notes:
  - SDK Method used are
    event_management.EventManagement.get_syslog_destination,
  - Paths used are
    get /dna/intent/api/v1/event/syslog-config,
"""

EXAMPLES = r"""
---
- name: Get all Event Syslog Config
  cisco.catalystcenter.event_syslog_config_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    configId: string
    name: string
    protocol: string
    offset: 0
    limit: 0
    sortBy: string
    order: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "errorMessage": {
        "errors": [
          "string"
        ]
      },
      "apiStatus": "string",
      "statusMessage": [
        {
          "version": "string",
          "tenantId": "string",
          "configId": "string",
          "name": "string",
          "description": "string",
          "host": "string",
          "port": 0,
          "protocol": "string"
        }
      ]
    }
"""
