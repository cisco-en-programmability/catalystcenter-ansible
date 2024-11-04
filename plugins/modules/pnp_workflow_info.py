#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pnp_workflow_info
short_description: Information module for Pnp Workflow
description:
- Get all Pnp Workflow.
- Get Pnp Workflow by id.
- Returns a workflow specified by id.
- >
   Returns the list of workflows based on filter criteria. If a limit is not specified, it will default to return 50
   workflows. Pagination and sorting are also supported by this endpoint.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  limit:
    description:
    - Limit query parameter. Limits number of results.
    type: int
  offset:
    description:
    - Offset query parameter. Index of first result.
    type: int
  sort:
    description:
    - Sort query parameter. Comma seperated lost of fields to sort on. 
    elements: str
    type: list
  sortOrder:
    description:
    - SortOrder query parameter. Sort Order Ascending (asc) or Descending (des).
    type: str
  type:
    description:
    - Type query parameter. Workflow Type. 
    elements: str
    type: list
  name:
    description:
    - Name query parameter. Workflow Name. 
    elements: dict
    type: list
  id:
    description:
    - Id path parameter.
    type: str
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Device Onboarding (PnP) GetWorkflowByIdV1
  description: Complete reference of the GetWorkflowByIdV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-workflow-by-id-v-1
- name: Cisco CATALYST Center documentation for Device Onboarding (PnP) GetWorkflowsV1
  description: Complete reference of the GetWorkflowsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-workflows-v-1
notes:
  - SDK Method used are
    device_onboarding_pnp.DeviceOnboardingPnp.get_workflow_by_id_v1,
    device_onboarding_pnp.DeviceOnboardingPnp.get_workflows_v1,

  - Paths used are
    get /dna/intent/api/v1/onboarding/pnp-workflow,
    get /dna/intent/api/v1/onboarding/pnp-workflow/{id},

"""

EXAMPLES = r"""
- name: Get all Pnp Workflow
  cisco.catalystcenter.pnp_workflow_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    limit: 0
    offset: 0
    sort: []
    sortOrder: string
    type: []
    name: []
  register: result

- name: Get Pnp Workflow by id
  cisco.catalystcenter.pnp_workflow_info:
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
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "_id": "string",
      "state": "string",
      "type": "string",
      "description": "string",
      "lastupdateOn": 0,
      "imageId": "string",
      "currTaskIdx": 0,
      "addedOn": 0,
      "tasks": [
        {
          "state": "string",
          "type": "string",
          "currWorkItemIdx": 0,
          "taskSeqNo": 0,
          "endTime": 0,
          "startTime": 0,
          "workItemList": [
            {
              "state": "string",
              "command": "string",
              "outputStr": "string",
              "endTime": 0,
              "startTime": 0,
              "timeTaken": 0
            }
          ],
          "timeTaken": 0,
          "name": "string"
        }
      ],
      "addToInventory": true,
      "instanceType": "string",
      "endTime": 0,
      "execTime": 0,
      "startTime": 0,
      "useState": "string",
      "configId": "string",
      "name": "string",
      "version": 0,
      "tenantId": "string"
    }
"""
