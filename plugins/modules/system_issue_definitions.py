#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: system_issue_definitions
short_description: Resource module for System Issue Definitions
description:
  - Manage operation update of the resource System Issue Definitions.
  - Update issue trigger threshold, priority for the given id. Also enable or.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description: Id path parameter. Issue trigger definition id.
    type: str
  issueEnabled:
    description: IssueEnabled flag.
    type: bool
  priority:
    description: System Issue Definitions's priority.
    type: str
  synchronizeToHealthThreshold:
    description: SynchronizeToHealthThreshold flag.
    type: bool
  thresholdValue:
    description: System Issue Definitions's thresholdValue.
    type: float
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Issues IssueTriggerDefinitionUpdate
    description: Complete reference of the IssueTriggerDefinitionUpdate API.
    link: https://developer.cisco.com/docs/dna-center/#!issue-trigger-definition-update
notes:
  - SDK Method used are
    issues.Issues.issue_trigger_definition_update,
  - Paths used are
    put /dna/intent/api/v1/systemIssueDefinitions/{id},
"""

EXAMPLES = r"""
---
- name: Update by id
  cisco.catalystcenter.system_issue_definitions:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    headers: '{{my_headers | from_json}}'
    id: string
    issueEnabled: true
    priority: string
    synchronizeToHealthThreshold: true
    thresholdValue: 0
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string",
      "name": "string",
      "displayName": "string",
      "description": "string",
      "priority": "string",
      "defaultPriority": "string",
      "deviceType": "string",
      "issueEnabled": true,
      "profileId": "string",
      "definitionStatus": "string",
      "categoryName": "string",
      "synchronizeToHealthThreshold": true,
      "thresholdValue": 0,
      "lastModified": "string"
    }
"""
