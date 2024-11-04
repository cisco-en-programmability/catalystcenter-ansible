#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: task_operation_info
short_description: Information module for Task Operation
description:
- Get Task Operation by id.
- Returns root tasks associated with an Operationid.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  operationId:
    description:
    - OperationId path parameter.
    type: str
  offset:
    description:
    - Offset path parameter. Index, minimum value is 0.
    type: int
  limit:
    description:
    - >
      Limit path parameter. The maximum value of {limit} supported is 500. Base 1 indexing for {limit}, minimum
      value is 1.
    type: int
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Task GetTaskByOperationIdV1
  description: Complete reference of the GetTaskByOperationIdV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-task-by-operation-id-v-1
notes:
  - SDK Method used are
    task.Task.get_task_by_operationid,

  - Paths used are
    get /dna/intent/api/v1/task/operation/{operationId}/{offset}/{limit},

"""

EXAMPLES = r"""
- name: Get Task Operation by id
  cisco.catalystcenter.task_operation_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    operationId: string
    offset: 0
    limit: 0
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "additionalStatusURL": "string",
          "data": "string",
          "endTime": 0,
          "errorCode": "string",
          "errorKey": "string",
          "failureReason": "string",
          "id": "string",
          "instanceTenantId": "string",
          "isError": true,
          "lastUpdate": 0,
          "operationIdList": [
            "string"
          ],
          "parentId": "string",
          "progress": "string",
          "rootId": "string",
          "serviceType": "string",
          "startTime": 0,
          "username": "string",
          "version": 0
        }
      ],
      "version": "string"
    }
"""
