#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: application_health_score_definitions_info
short_description: Information module for Application Health Score Definitions
description:
  - Get all Application Health Score Definitions.
  - Get Application Health Score Definitions by id.
  - Get all application health score definitions for given filter. - > Get application health score definition for the given
    id. By default all supported attributes are listed in the response.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Application health score definition id.
    type: str
  attribute:
    description:
      - >
        Attribute query parameter. These are the attributes supported in application health score definitions
        response. By default, all properties are sent in response.
    type: str
  trafficClass:
    description:
      - >
        TrafficClass query parameter. The traffic class for the application health score definition. If this is
        not provided then all traffic class application health score definitions will be included.
    type: str
  includeForHealthScore:
    description:
      - >
        IncludeForHealthScore query parameter. The inclusion of application health score definition, either true
        or false. True indicates that particular application health metric is included in in the application
        health score computation, otherwise false.
    type: bool
  offset:
    description:
      - >
        Offset query parameter. Specifies the starting point within all records returned by the API. It's one
        based offset. The starting value is 1.
    type: int
  limit:
    description:
      - Limit query parameter. Maximum number of records to return.
    type: int
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Applications GetAllApplicationHealthScoreDefinitions
    description: Complete reference of the GetAllApplicationHealthScoreDefinitions API.
    link: https://developer.cisco.com/docs/dna-center/#!get-all-application-health-score-definitions
  - name: Cisco Catalyst Center documentation for Applications GetApplicationHealthScoreDefinitionForTheGivenId
    description: Complete reference of the GetApplicationHealthScoreDefinitionForTheGivenId API.
    link: https://developer.cisco.com/docs/dna-center/#!get-application-health-score-definition-for-the-given-id
notes:
  - SDK Method used are
    applications.Applications.get_all_application_health_score_definitions,
    applications.Applications.get_application_health_score_definition_for_the_given_id,
  - Paths used are
    get /dna/intent/api/v1/applicationHealthScoreDefinitions,
    get /dna/intent/api/v1/applicationHealthScoreDefinitions/{id},
"""

EXAMPLES = r"""
---
- name: Get all Application Health Score Definitions
  cisco.catalystcenter.application_health_score_definitions_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    trafficClass: string
    includeForHealthScore: True
    attribute: string
    offset: 1
    limit: 100
  register: result
- name: Get Application Health Score Definitions by id
  cisco.catalystcenter.application_health_score_definitions_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    attribute: string
    id: string
  register: result
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
