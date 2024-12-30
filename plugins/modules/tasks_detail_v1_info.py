#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: tasks_detail_v1_info
short_description: Information module for Tasks Detail V1
description:
- Get all Tasks Detail V1.
- Returns the task details for the given task ID.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
    - Id path parameter. The `id` of the task to retrieve details for.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Task GetTaskDetailsByIDV1
  description: Complete reference of the GetTaskDetailsByIDV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-task-details-by-id
notes:
  - SDK Method used are
    task.Task.get_task_details_by_id_v1,

  - Paths used are
    get /dna/intent/api/v1/tasks/{id}/detail,

"""

EXAMPLES = r"""
- name: Get all Tasks Detail V1
  cisco.catalystcenter.tasks_detail_v1_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "data": "string",
        "progress": "string",
        "errorCode": "string",
        "failureReason": "string"
      },
      "version": "string"
    }
"""
