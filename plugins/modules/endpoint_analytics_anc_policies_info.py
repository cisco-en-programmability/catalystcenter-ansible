#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: endpoint_analytics_anc_policies_info
short_description: Information module for Endpoint Analytics
  Anc Policies
description:
  - Get all Endpoint Analytics Anc Policies.
  - Fetches the list of ANC policies available in ISE.
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for AI Endpoint
      Analytics GetANCPolicies
    description: Complete reference of the GetANCPolicies
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-anc-policies
notes:
  - SDK Method used are
    ai_endpoint_analytics.AiEndpointAnalytics.get_anc_policies,
  - Paths used are
    get /dna/intent/api/v1/endpoint-analytics/anc-policies,
"""

EXAMPLES = r"""
---
- name: Get all Endpoint Analytics Anc Policies
  cisco.catalystcenter.endpoint_analytics_anc_policies_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "name": "string"
      }
    ]
"""
