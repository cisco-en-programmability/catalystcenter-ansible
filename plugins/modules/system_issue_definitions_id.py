#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: system_issue_definitions_id
short_description: Resource module for System Issue
  Definitions Id
description:
  - Manage operation update of the resource System Issue
    Definitions Id.
  - Update issue trigger threshold, priority for the
    given id.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. Issue trigger definition
      id.
    type: str
  issueEnabled:
    description: Issue Enabled.
    type: bool
  priority:
    description: Priority.
    type: str
  synchronizeToHealthThreshold:
    description: Synchronize To Health Threshold.
    type: bool
  thresholdValue:
    description: Threshold Value.
    type: float
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Issues
      IssueTriggerDefinitionUpdate
    description: Complete reference of the IssueTriggerDefinitionUpdate
      API.
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
  cisco.catalystcenter.system_issue_definitions_id:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    state: present
    id: string
    issueEnabled: true
    priority: string
    synchronizeToHealthThreshold: true
    thresholdValue: 0
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
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
      },
      "version": "string"
    }
"""
