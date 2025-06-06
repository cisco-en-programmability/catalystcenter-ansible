#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: dnacaap_management_execution_status_v1_info
short_description: Information module for Dnacaap Management Execution Status V1
description:
  - Get Dnacaap Management Execution Status V1 by id.
  - Retrieves the execution details of a Business API.
version_added: '4.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  executionId:
    description:
      - ExecutionId path parameter. Execution Id of API.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Task GetBusinessAPIExecutionDetailsV1
    description: Complete reference of the GetBusinessAPIExecutionDetailsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-business-api-execution-details
notes:
  - SDK Method used are task.Task.get_business_api_execution_details_v1,
  - Paths used are get /dna/intent/api/v1/dnacaap/management/execution-status/{executionId},
"""
EXAMPLES = r"""
- name: Get Dnacaap Management Execution Status V1 by id
  cisco.catalystcenter.dnacaap_management_execution_status_v1_info:
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
      "bapiKey": "string",
      "bapiName": "string",
      "bapiExecutionId": "string",
      "startTime": "string",
      "startTimeEpoch": 0,
      "endTime": "string",
      "endTimeEpoch": 0,
      "timeDuration": 0,
      "status": "string",
      "bapiSyncResponse": "string",
      "bapiSyncResponseJson": {},
      "runtimeInstanceId": "string",
      "bapiError": "string"
    }
"""
