#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: catalystcenteraap_management_execution_status_info
short_description: Information module for catalystcenteraap Management Execution Status
description:
- Get catalystcenteraap Management Execution Status by id.
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
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Task GetBusinessAPIExecutionDetailsV1
  description: Complete reference of the GetBusinessAPIExecutionDetailsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-business-api-execution-details-v-1
notes:
  - SDK Method used are
    task.Task.get_business_api_execution_details_v1,

  - Paths used are
    get /dna/intent/api/v1/catalystcenteraap/management/execution-status/{executionId},

"""

EXAMPLES = r"""
- name: Get catalystcenteraap Management Execution Status by id
  cisco.catalystcenter.catalystcenteraap_management_execution_status_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    executionId: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
      "runtimeInstanceId": "string",
      "bapiError": "string"
    }
"""
