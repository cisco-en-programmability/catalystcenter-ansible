#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: task_tree_v1_info
short_description: Information module for Task Tree V1
description:
- Get all Task Tree V1.
- Returns a task with its children tasks by based on their id.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  taskId:
    description:
    - TaskId path parameter. UUID of the Task.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Task GetTaskTreeV1
  description: Complete reference of the GetTaskTreeV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-task-tree
notes:
  - SDK Method used are
    task.Task.get_task_tree_v1,

  - Paths used are
    get /dna/intent/api/v1/task/{taskId}/tree,

"""

EXAMPLES = r"""
- name: Get all Task Tree V1
  cisco.catalystcenter.task_tree_v1_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    taskId: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
