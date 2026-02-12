#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: endpoint_analytics_profiling_rules_count_info
short_description: Information module for Endpoint Analytics Profiling-Rules Count
description:
  - Get all Endpoint Analytics Profiling-Rules Count. - > This API fetches the count of profiling rules based on the filter
    values provided in the query parameters. The filter parameters are same as that of 'GET /profiling-rules' API, excluding
    the pagination and sort parameters.
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  ruleType:
    description:
      - RuleType query parameter. Use comma-separated list of rule types to filter the data. Defaults to 'Custom Rule'.
    type: str
  includeDeleted:
    description:
      - IncludeDeleted query parameter. Flag to indicate whether deleted rules should be part of the records fetched.
    type: bool
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
notes:
  - SDK Method used are
    ai_endpoint_analytics.AiEndpointAnalytics.get_count_of_profiling_rules,
  - Paths used are
    get /dna/intent/api/v1/endpoint-analytics/profiling-rules/count,
"""

EXAMPLES = r"""
---
- name: Get all Endpoint Analytics Profiling-Rules Count
  cisco.catalystcenter.endpoint_analytics_profiling_rules_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    ruleType: string
    includeDeleted: true
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "count": 0
    }
"""
