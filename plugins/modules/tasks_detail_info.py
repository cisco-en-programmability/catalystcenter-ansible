#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: tasks_detail_info
short_description: Information module for Tasks Detail
description:
  - Get all Tasks Detail.
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
      - Id path parameter. The `id` of the task to retrieve
        details for.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Task GetTaskDetailsByID
    description: Complete reference of the GetTaskDetailsByID
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-task-details-by-id
notes:
  - SDK Method used are
    task.Task.get_task_details_by_id,
  - Paths used are
    get /dna/intent/api/v1/tasks/{id}/detail,
"""

EXAMPLES = r"""
---
- name: Get all Tasks Detail
  cisco.catalystcenter.tasks_detail_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
