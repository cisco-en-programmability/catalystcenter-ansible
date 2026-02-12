#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: diagnostic_tasks_id_info
short_description: Information module for Diagnostic Tasks Id
description:
  - Get Diagnostic Tasks Id by id.
  - This API retrieves the diagnostic task identified by the specified `id`.
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
      - Id path parameter. The `id` of the diagnostic task to be retrieved.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Health and Performance RetrievesDiagnosticTaskByID
    description: Complete reference of the RetrievesDiagnosticTaskByID API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-diagnostic-task-by-id
notes:
  - SDK Method used are
    health_and_performance.HealthAndPerformance.retrieves_diagnostic_task_by_id,
  - Paths used are
    get /dna/intent/api/v1/diagnosticTasks/{id},
"""

EXAMPLES = r"""
---
- name: Get Diagnostic Tasks Id by id
  cisco.catalystcenter.diagnostic_tasks_id_info:
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
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "id": "string",
        "rootId": "string",
        "parentId": "string",
        "startTime": 0,
        "resultLocation": "string",
        "status": "string",
        "updatedTime": 0,
        "endTime": 0
      },
      "version": "string"
    }
"""
