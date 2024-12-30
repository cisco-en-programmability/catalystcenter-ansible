#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: diagnostic_tasks_id_detail_v1_info
short_description: Information module for Diagnostic Tasks Id Detail V1
description:
- Get all Diagnostic Tasks Id Detail V1.
- This API retrieves the details of the diagnostic task identified by the specified `id`.
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
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Health and Performance RetrievesDiagnosticTaskDetailsByIDV1
  description: Complete reference of the RetrievesDiagnosticTaskDetailsByIDV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!retrieves-diagnostic-task-details-by-id
notes:
  - SDK Method used are
    health_and_performance.HealthAndPerformance.retrieves_diagnostic_task_details_by_id_v1,

  - Paths used are
    get /dna/intent/api/v1/diagnosticTasks/{id}/detail,

"""

EXAMPLES = r"""
- name: Get all Diagnostic Tasks Id Detail V1
  cisco.catalystcenter.diagnostic_tasks_id_detail_v1_info:
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
