#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: application_health_score_definitions_count_info
short_description: Information module for Application Health Score Definitions Count
description:
  - Get all Application Health Score Definitions Count.
  - Get the count of application health score definitions based on provided filters.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
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
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Applications GetTheCountOfApplicationHealthScoreDefinitions
    description: Complete reference of the GetTheCountOfApplicationHealthScoreDefinitions API.
    link: https://developer.cisco.com/docs/dna-center/#!get-the-count-of-application-health-score-definitions
notes:
  - SDK Method used are
    applications.Applications.get_the_count_of_application_health_score_definitions,
  - Paths used are
    get /dna/intent/api/v1/applicationHealthScoreDefinitions/count,
"""

EXAMPLES = r"""
---
- name: Get all Application Health Score Definitions Count
  cisco.catalystcenter.application_health_score_definitions_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    trafficClass: string
    includeForHealthScore: true
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
        "count": 0
      },
      "version": "string"
    }
"""
