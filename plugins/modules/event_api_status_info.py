#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_api_status_info
short_description: Information module for Event Api
  Status
description:
  - Get Event Api Status by id.
  - Get the Status of events API calls with provided
    executionId as mandatory path parameter.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  executionId:
    description:
      - ExecutionId path parameter. Execution ID.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Event Management
      GetStatusAPIForEvents
    description: Complete reference of the GetStatusAPIForEvents
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-status-api-for-events
notes:
  - SDK Method used are
    event_management.EventManagement.get_status_api_for_events,
  - Paths used are
    get /dna/intent/api/v1/event/api-status/{executionId},
"""

EXAMPLES = r"""
---
- name: Get Event Api Status by id
  cisco.catalystcenter.event_api_status_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
    executionId: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "errorMessage": {},
      "apiStatus": "string",
      "statusMessage": "string"
    }
"""
