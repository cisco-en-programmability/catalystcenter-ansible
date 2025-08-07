#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: diagnostic_tasks_id_detail_info
short_description: Information module for Diagnostic
  Tasks Id Detail
description:
  - Get all Diagnostic Tasks Id Detail.
  - This API retrieves the details of the diagnostic
    task identified by the specified `id`.
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
      - Id path parameter. The `id` of the diagnostic
        task to be retrieved.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Health
      and Performance RetrievesDiagnosticTaskDetailsByID
    description: Complete reference of the RetrievesDiagnosticTaskDetailsByID
      API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-diagnostic-task-details-by-id
notes:
  - SDK Method used are
    health_and_performance.HealthAndPerformance.retrieves_diagnostic_task_details_by_id,
  - Paths used are
    get /dna/intent/api/v1/diagnosticTasks/{id}/detail,
"""

EXAMPLES = r"""
---
- name: Get all Diagnostic Tasks Id Detail
  cisco.catalystcenter.diagnostic_tasks_id_detail_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
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
