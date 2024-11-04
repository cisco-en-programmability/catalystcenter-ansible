#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: diagnosticValidationWorkflows
short_description: Resource module for Diagnosticvalidationworkflows
description:
- Manage operations create and delete of the resource Diagnosticvalidationworkflows.
- Submits the workflow for executing the validations for the given validation specifications.
- Deletes the workflow for the given id.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  description:
    description: Description of the workflow to run.
    type: str
  id:
    description: Id path parameter. Workflow id.
    type: str
  name:
    description: Name of the workflow to run. It must be unique.
    type: str
  validationSetIds:
    description: List of validation set ids.
    elements: str
    type: list
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Health and Performance SubmitsTheWorkflowForExecutingValidationsV1
  description: Complete reference of the SubmitsTheWorkflowForExecutingValidationsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!submits-the-workflow-for-executing-validations-v-1
- name: Cisco CATALYST Center documentation for Health and Performance DeletesAValidationWorkflowV1
  description: Complete reference of the DeletesAValidationWorkflowV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!deletes-a-validation-workflow-v-1
notes:
  - SDK Method used are
    health_and_performance.HealthAndPerformance.deletes_a_validation_workflow_v1,
    health_and_performance.HealthAndPerformance.submits_the_workflow_for_executing_validations_v1,

  - Paths used are
    post /dna/intent/api/v1/diagnosticValidationWorkflows,
    delete /dna/intent/api/v1/diagnosticValidationWorkflows/{id},

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.diagnosticValidationWorkflows:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    description: string
    name: string
    validationSetIds:
    - string

- name: Delete by id
  cisco.catalystcenter.diagnosticValidationWorkflows:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "id": "string"
      },
      "version": "string"
    }
"""
