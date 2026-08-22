#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: application_health_score_definitions
short_description: Resource module for Application Health Score Definitions
description:
  - Manage operation update of the resource Application Health Score Definitions.
  - Update application health score definition for the given id.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
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
  headers:
    description: Additional headers.
    type: dict
  id:
    description: Id path parameter. Application health score definition id.
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
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Applications UpdateApplicationHealthScoreDefinitionForTheGivenId
    description: Complete reference of the UpdateApplicationHealthScoreDefinitionForTheGivenId API.
    link: https://developer.cisco.com/docs/dna-center/#!update-application-health-score-definition-for-the-given-id
notes:
  - SDK Method used are
    applications.Applications.update_application_health_score_definition_for_the_given_id,
  - Paths used are
    put /dna/intent/api/v1/applicationHealthScoreDefinitions/{id},
"""

EXAMPLES = r"""
---
- name: Update by id
  cisco.catalystcenter.application_health_score_definitions:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    badValue: 10
    goodValue: 1
    greatValue: 0.1
    headers: '{{my_headers | from_json}}'
    id: string
    includeForHealthScore: true
    poorValue: 4
    weightValue: 10
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
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
      },
      "version": "string"
    }
"""
