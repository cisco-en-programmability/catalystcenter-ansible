#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: endpoint_analytics_dictionaries_info
short_description: Information module for Endpoint Analytics Dictionaries Info
description:
- This module represents an alias of the module endpoint_analytics_dictionaries_v1_info
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
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for AI Endpoint Analytics GetAIEndpointAnalyticsAttributeDictionariesV1
  description: Complete reference of the GetAIEndpointAnalyticsAttributeDictionariesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-ai-endpoint-analytics-attribute-dictionaries
notes:
  - SDK Method used are
    a_i_endpoint_analytics.AIEndpointAnalytics.get_a_i_endpoint_analytics_attribute_dictionaries_v1,

  - Paths used are
    get /dna/intent/api/v1/endpoint-analytics/dictionaries,
  - It should be noted that this module is an alias of endpoint_analytics_dictionaries_v1_info

"""

EXAMPLES = r"""
- name: Get all Endpoint Analytics Dictionaries Info
  cisco.catalystcenter.endpoint_analytics_dictionaries_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    includeAttributes: True
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
