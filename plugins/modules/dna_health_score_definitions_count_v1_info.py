#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: dna_health_score_definitions_count_v1_info
short_description: Information module for Dna Health Score Definitions Count V1
description:
  - Get all Dna Health Score Definitions Count V1.
  - >
    Get the count of health score definitions based on provided filters. Supported
    filters are id, name and overall
    health include status. For detailed information about the usage of the API, please
    refer to the Open API
    specification document - https //github.com/cisco-en-programmability/catalyst-center-api-
    specs/blob/main/Assurance/CE_Cat_Center_Org-issueAndHealthDefinitions-1.0.0-resolved.yaml.
version_added: '6.17.0'
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
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices GetTheCountOfHealthScoreDefinitionsBasedOnProvidedFiltersV1
    description: Complete reference of the GetTheCountOfHealthScoreDefinitionsBasedOnProvidedFiltersV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-the-count-of-health-score-definitions-based-on-provided-filters
notes:
  - SDK Method used are
    devices.Devices.get_the_count_of_health_score_definitions_based_on_provided_filters_v1,
  - Paths used are get /dna/intent/api/v1/healthScoreDefinitions/count,
"""
EXAMPLES = r"""
- name: Get all Dna Health Score Definitions Count V1
  cisco.catalystcenter.dna_health_score_definitions_count_v1_info:
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
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "count": 0
      },
      "version": "string"
    }
"""
