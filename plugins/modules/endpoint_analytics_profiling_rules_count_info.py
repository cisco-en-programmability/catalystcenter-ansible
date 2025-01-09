#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: endpoint_analytics_profiling_rules_count_info
short_description: Information module for Endpoint Analytics Profiling Rules Count Info
description:
- This module represents an alias of the module endpoint_analytics_profiling_rules_count_v1_info
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
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
notes:
  - SDK Method used are
    a_i_endpoint_analytics.AIEndpointAnalytics.get_count_of_profiling_rules_v1,

  - Paths used are
    get /dna/intent/api/v1/endpoint-analytics/profiling-rules/count,
  - It should be noted that this module is an alias of endpoint_analytics_profiling_rules_count_v1_info

"""

EXAMPLES = r"""
- name: Get all Endpoint Analytics Profiling Rules Count Info
  cisco.catalystcenter.endpoint_analytics_profiling_rules_count_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    ruleType: string
    includeDeleted: True
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "count": 0
    }
"""
