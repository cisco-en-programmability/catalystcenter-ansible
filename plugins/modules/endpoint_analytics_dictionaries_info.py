#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: endpoint-analytics_dictionaries_info
short_description: Information module for Endpoint-Analytics Dictionaries
description:
- Get all Endpoint-Analytics Dictionaries.
- Fetches the list of attribute dictionaries.
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  includeAttributes:
    description:
    - >
      IncludeAttributes query parameter. Flag to indicate whether attribute list for each dictionary should be
      included in response.
    type: bool
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for AI Endpoint Analytics GetAIEndpointAnalyticsAttributeDictionariesV1
  description: Complete reference of the GetAIEndpointAnalyticsAttributeDictionariesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-ai-endpoint-analytics-attribute-dictionaries-v-1
notes:
  - SDK Method used are
    a_i_endpoint_analytics.AIEndpointAnalytics.get_a_i_endpoint_analytics_attribute_dictionaries_v1,

  - Paths used are
    get /dna/intent/api/v1/endpoint-analytics/dictionaries,

"""

EXAMPLES = r"""
- name: Get all Endpoint-Analytics Dictionaries
  cisco.catalystcenter.endpoint-analytics_dictionaries_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    includeAttributes: True
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "name": "string",
        "description": "string",
        "attributes": [
          {
            "name": "string",
            "description": "string"
          }
        ]
      }
    ]
"""
