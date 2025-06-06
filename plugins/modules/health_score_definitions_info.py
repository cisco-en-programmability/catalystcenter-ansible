#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: health_score_definitions_info
short_description: Information module for Health Score Definitions Info
description:
  - This module represents an alias of the module health_score_definitions_v1_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deviceType:
    description:
      - >
        DeviceType query parameter. These are the device families supported for health
        score definitions. If no
        input is made on device family, all device families are considered.
    type: str
  id:
    description:
      - >
        Id query parameter. The definition identifier. Examples id=015d9cba-4f53-4087-8317-7e49e5ffef46
        (single
        entity id request) id=015d9cba-4f53-4087-8317-7e49e5ffef46&id=015d9cba-4f53-4087-8317-7e49e5ffef47
        (multiple
        ids in the query param).
    type: str
  includeForOverallHealth:
    description:
      - >
        IncludeForOverallHealth query parameter. The inclusion status of the issue
        definition, either true or false.
        True indicates that particular health metric is included in overall health
        computation, otherwise false. By
        default it's set to true.
    type: bool
  attribute:
    description:
      - >
        Attribute query parameter. These are the attributes supported in health score
        definitions response. By
        default, all properties are sent in response.
    type: str
  offset:
    description:
      - >
        Offset query parameter. Specifies the starting point within all records returned
        by the API. It's one based
        offset. The starting value is 1.
    type: float
  limit:
    description:
      - Limit query parameter. Maximum number of records to return.
    type: float
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices GetAllHealthScoreDefinitionsForGivenFiltersV1
    description: Complete reference of the GetAllHealthScoreDefinitionsForGivenFiltersV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-all-health-score-definitions-for-given-filters
  - name: Cisco DNA Center documentation for Devices GetHealthScoreDefinitionForTheGivenIdV1
    description: Complete reference of the GetHealthScoreDefinitionForTheGivenIdV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-health-score-definition-for-the-given-id
notes:
  - SDK Method used are devices.Devices.get_all_health_score_definitions_for_given_filters_v1,
    devices.Devices.get_health_score_definition_for_the_given_id_v1,
  - Paths used are get /dna/intent/api/v1/healthScoreDefinitions, get /dna/intent/api/v1/healthScoreDefinitions/{id},
  - It should be noted that this module is an alias of health_score_definitions_v1_info
"""
EXAMPLES = r"""
- name: Get all Health Score Definitions Info
  cisco.catalystcenter.health_score_definitions_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    deviceType: string
    id: string
    includeForOverallHealth: true
    attribute: string
    offset: 0
    limit: 0
  register: result
- name: Get Health Score Definitions Info by id
  cisco.catalystcenter.health_score_definitions_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
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
      ]
    }
"""
