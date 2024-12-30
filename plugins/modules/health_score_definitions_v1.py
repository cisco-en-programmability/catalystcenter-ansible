#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: health_score_definitions_v1
short_description: Resource module for Health Score Definitions V1
description:
- Manage operation update of the resource Health Score Definitions V1.
- Update health threshold, include status of overall health status.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. Health score definition id.
    type: str
  includeForOverallHealth:
    description: Include For Overall Health.
    type: bool
  synchronizeToIssueThreshold:
    description: Synchronize To Issue Threshold.
    type: bool
  thresholdValue:
    description: Thresehold Value.
    type: float
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices UpdateHealthScoreDefinitionForTheGivenIdV1
  description: Complete reference of the UpdateHealthScoreDefinitionForTheGivenIdV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!update-health-score-definition-for-the-given-id
notes:
  - SDK Method used are
    devices.Devices.update_health_score_definition_for_the_given_id_v1,

  - Paths used are
    put /dna/intent/api/v1/healthScoreDefinitions/{id},

"""

EXAMPLES = r"""
- name: Update by id
  cisco.catalystcenter.health_score_definitions_v1:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    id: string
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
"""
