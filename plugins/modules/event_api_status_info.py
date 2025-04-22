#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: event_api_status_info
short_description: Information module for Event Api Status Info
description:
  - This module represents an alias of the module event_api_status_v1_info
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
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Event Management GetStatusAPIForEventsV1
    description: Complete reference of the GetStatusAPIForEventsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-status-api-for-events
notes:
  - SDK Method used are event_management.EventManagement.get_status_api_for_events_v1,
  - Paths used are get /dna/intent/api/v1/event/api-status/{executionId},
  - It should be noted that this module is an alias of event_api_status_v1_info
"""
EXAMPLES = r"""
- name: Get Event Api Status Info by id
  cisco.catalystcenter.event_api_status_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    executionId: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "errorMessage": {},
      "apiStatus": "string",
      "statusMessage": "string"
    }
"""
