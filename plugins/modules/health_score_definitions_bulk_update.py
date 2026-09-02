#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: health_score_definitions_bulk_update
short_description: Resource module for Health Score Definitions Bulk Update
description:
  - Manage operation create of the resource Health Score Definitions Bulk Update.
  - Update health thresholds, include status of overall health status for each.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  payload:
    description: Health Score Definitions Bulk Update's payload.
    elements: dict
    suboptions:
      id:
        description: Health Score Definitions Bulk Update's id.
        type: str
      includeForOverallHealth:
        description: IncludeForOverallHealth flag.
        type: bool
      synchronizeToIssueThreshold:
        description: SynchronizeToIssueThreshold flag.
        type: bool
      thresholdValue:
        description: Health Score Definitions Bulk Update's thresholdValue.
        type: float
    type: list
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices UpdateHealthScoreDefinitions
    description: Complete reference of the UpdateHealthScoreDefinitions API.
    link: https://developer.cisco.com/docs/dna-center/#!update-health-score-definitions
notes:
  - SDK Method used are
    devices.Devices.update_health_score_definitions,
  - Paths used are
    post /dna/intent/api/v1/healthScoreDefinitions/bulkUpdate,
"""

EXAMPLES = r"""
---
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
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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
