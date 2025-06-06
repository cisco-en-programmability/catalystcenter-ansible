#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: assurance_tasks_id_info
short_description: Information module for Assurance Tasks Id Info
description:
  - This module represents an alias of the module assurance_tasks_id_v1_info
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Unique task id.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Task RetrieveASpecificAssuranceTaskByIdV1
    description: Complete reference of the RetrieveASpecificAssuranceTaskByIdV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!retrieve-a-specific-assurance-task-by-id
notes:
  - SDK Method used are task.Task.retrieve_a_specific_assurance_task_by_id_v1,
  - Paths used are get /dna/data/api/v1/assuranceTasks/{id},
  - It should be noted that this module is an alias of assurance_tasks_id_v1_info
"""
EXAMPLES = r"""
- name: Get Assurance Tasks Id Info by id
  cisco.catalystcenter.assurance_tasks_id_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
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
        "id": "string",
        "status": "string",
        "startTime": 0,
        "endTime": 0,
        "updateTime": 0,
        "progress": "string",
        "failureReason": "string",
        "errorCode": "string",
        "requestType": "string",
        "data": {},
        "resultUrl": "string"
      },
      "version": "string"
    }
"""
