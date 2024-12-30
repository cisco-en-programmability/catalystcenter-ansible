#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: health_score_definitions_bulk_update
short_description: Resource module for Health Score Definitions Bulk Update
description:
- This module represents an alias of the module health_score_definitions_bulk_update_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  payload:
    description: Health Score Definitions Bulk Update's payload.
    elements: dict
    suboptions:
      id:
        description: Id.
        type: str
      includeForOverallHealth:
        description: Include For Overall Health.
        type: bool
      synchronizeToIssueThreshold:
        description: Synchronize To Issue Threshold.
        type: bool
      thresholdValue:
        description: Threshold Value.
        type: float
    type: list
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices UpdateHealthScoreDefinitionsV1
  description: Complete reference of the UpdateHealthScoreDefinitionsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!update-health-score-definitions
notes:
  - SDK Method used are
    devices.Devices.update_health_score_definitions_v1,

  - Paths used are
    post /dna/intent/api/v1/healthScoreDefinitions/bulkUpdate,
  - It should be noted that this module is an alias of health_score_definitions_bulk_update_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.health_score_definitions_bulk_update:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: '{{my_headers | from_json}}'
    payload:
    - id: string
      includeForOverallHealth: true
      synchronizeToIssueThreshold: true
      thresholdValue: 0

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "name": "string",
          "displayName": "string",
          "deviceFamily": "string",
          "description": "string",
          "includeForOverallHealth": true,
          "definitionStatus": "string",
          "thresholdValue": 0,
          "synchronizeToIssueThreshold": true,
          "lastModified": "string"
        }
      ],
      "version": "string"
    }
"""
