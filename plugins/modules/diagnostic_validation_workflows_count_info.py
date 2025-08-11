#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: diagnostic_validation_workflows_count_info
short_description: Information module for Diagnostic
  Validation Workflows Count
description:
  - Get all Diagnostic Validation Workflows Count.
  - Retrieves the count of workflows that have been
    successfully submitted and are currently available.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  startTime:
    description:
      - StartTime query parameter. Workflows started
        after the given time (as milliseconds since
        UNIX epoch).
    type: float
  endTime:
    description:
      - EndTime query parameter. Workflows started before
        the given time (as milliseconds since UNIX epoch).
    type: float
  runStatus:
    description:
      - >
        RunStatus query parameter. Execution status
        of the workflow. If the workflow is successfully
        submitted, runStatus is `PENDING`. If the workflow
        execution has started, runStatus is `IN_PROGRESS`.
        If the workflow executed is completed with all
        validations executed, runStatus is `COMPLETED`.
        If the workflow execution fails while running
        validations, runStatus is `FAILED`.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Health
      and Performance RetrievesTheCountOfValidationWorkflows
    description: Complete reference of the RetrievesTheCountOfValidationWorkflows
      API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-count-of-validation-workflows
notes:
  - SDK Method used are
    health_and_performance.HealthAndPerformance.retrieves_the_count_of_validation_workflows,
  - Paths used are
    get /dna/intent/api/v1/diagnosticValidationWorkflows/count,
"""

EXAMPLES = r"""
---
- name: Get all Diagnostic Validation Workflows Count
  cisco.catalystcenter.diagnostic_validation_workflows_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    startTime: 0
    endTime: 0
    runStatus: string
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
        "count": 0
      },
      "version": "string"
    }
"""
