#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: endpoint-analytics_tasks_info
short_description: Information module for Endpoint-Analytics Tasks
description:
- Get Endpoint-Analytics Tasks by id.
- >
   Fetches the details of backend task. Task is typically created by making call to some other API that takes longer
   time to execute.
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  taskId:
    description:
    - TaskId path parameter. Unique identifier for the task.
    type: str
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for AI Endpoint Analytics GetTaskDetailsV1
  description: Complete reference of the GetTaskDetailsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-task-details-v-1
notes:
  - SDK Method used are
    a_i_endpoint_analytics.AIEndpointAnalytics.get_task_details_v1,

  - Paths used are
    get /dna/intent/api/v1/endpoint-analytics/tasks/{taskId},

"""

EXAMPLES = r"""
- name: Get Endpoint-Analytics Tasks by id
  cisco.catalystcenter.endpoint-analytics_tasks_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    taskId: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string",
      "name": "string",
      "status": "string",
      "errors": [
        {
          "index": 0,
          "code": 0,
          "message": "string",
          "details": "string"
        }
      ],
      "additionalInfo": {},
      "createdBy": "string",
      "createdOn": 0,
      "lastUpdatedOn": 0
    }
"""
