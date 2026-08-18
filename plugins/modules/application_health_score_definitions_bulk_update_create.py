#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: application_health_score_definitions_bulk_update_create
short_description: Resource module for Application Health Score Definitions Bulk Update Create
description:
  - Manage operation create of the resource Application Health Score Definitions Bulk Update Create. - > Caller ID is used
    to trace the origin of API calls and their associated queries executed on the database. It's an optional header parameter
    that can be added to an API request.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  payload:
    description: Application Health Score Definitions Bulk Update Create's payload.
    elements: dict
    suboptions:
      badDefaultValue:
        description: The default upper threshold value of the KPI for poor (1-3) health score.
        type: float
      badMaxValue:
        description: Maximum value allowed for upper threshold value of the KPI for poor (1-3) health score.
        type: float
      badMinValue:
        description: Minimum value allowed for upper threshold value of the KPI for poor (1-3) health score.
        type: float
      badValue:
        description: The upper threshold value of the KPI for poor (1-3) health score.
        type: float
      definitionType:
        description: Definition type to indicate whether the health score definition has been customized or not.
        type: str
      goodDefaultValue:
        description: The default lower threshold value of the KPI for fair (4-7) health score.
        type: float
      goodMaxValue:
        description: Maximum value allowed for lower threshold value of the KPI for fair (4-7) health score.
        type: float
      goodMinValue:
        description: Minimum value allowed for lower threshold value of the KPI for fair (4-7) health score.
        type: float
      goodValue:
        description: The lower threshold value of the KPI for fair (4-7) health score. This would be same as the upper threshold
          value of the KPI for good (8-10) health score.
        type: float
      greatDefaultValue:
        description: The default lower threshold value of the KPI for good (8-10) health score.
        type: float
      greatMaxValue:
        description: Maximum value allowed for the lower threshold value of the KPI for good (8-10) health score.
        type: float
      greatMinValue:
        description: Minimum value allowed for the lower threshold value of the KPI for good (8-10) health score.
        type: float
      greatValue:
        description: The lower threshold value of the KPI for good (8-10) health score.
        type: float
      id:
        description: Application health score definition id.
        type: str
      includeForHealthScore:
        description: Flag to indicate whether the KPI is included for the application health score calulation or not.
        type: bool
      includeForHealthScoreDefault:
        description: Default flag to indicate whether the KPI is included for application health calulation or not.
        type: bool
      kpiName:
        description: Application health KPI name.
        type: str
      lastModified:
        description: Last modification time in milliseconds since UNIX epoch. This is applicable only for modified thresholds.
        type: int
      poorDefaultValue:
        description: The default lower threshold value of the KPI for poor (1-3) health score.
        type: float
      poorMaxValue:
        description: Maximum value allowed for lower threshold value of the KPI for poor (1-3) health score.
        type: float
      poorMinValue:
        description: Minimum value allowed for lower threshold value of the KPI for poor (1-3) health score.
        type: float
      poorValue:
        description: The lower threshold value of the KPI for poor (1-3) health score. This would be same as the upper threshold
          value of the KPI for fair (4-7) health score.
        type: float
      trafficClass:
        description: Traffic class for application health score definition.
        type: str
      unit:
        description: Application Health score definition unit.
        type: str
      weightDefaultValue:
        description: The default weightage of the KPI used for application health score calculation.
        type: int
      weightValue:
        description: The weightage of the KPI used for application health score calculation.
        type: int
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Applications BulkUpdateApplicationHealthScoreDefinitions
    description: Complete reference of the BulkUpdateApplicationHealthScoreDefinitions API.
    link: https://developer.cisco.com/docs/dna-center/#!bulk-update-application-health-score-definitions
notes:
  - SDK Method used are
    applications.Applications.bulk_update_application_health_score_definitions,
  - Paths used are
    post /dna/intent/api/v1/applicationHealthScoreDefinitions/bulkUpdate,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.application_health_score_definitions_bulk_update_create:
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
          "kpiName": "string",
          "trafficClass": "string",
          "includeForHealthScore": true,
          "includeForHealthScoreDefault": true,
          "definitionType": "string",
          "unit": "string",
          "weightValue": 0,
          "weightDefaultValue": 0,
          "badValue": 0,
          "badDefaultValue": 0,
          "badMinValue": 0,
          "badMaxValue": 0,
          "poorValue": 0,
          "poorDefaultValue": 0,
          "poorMinValue": 0,
          "poorMaxValue": 0,
          "goodValue": 0,
          "goodDefaultValue": 0,
          "goodMinValue": 0,
          "goodMaxValue": 0,
          "greatValue": 0,
          "greatDefaultValue": 0,
          "greatMinValue": 0,
          "greatMaxValue": 0,
          "lastModified": 0
        }
      ],
      "version": "string"
    }
"""
