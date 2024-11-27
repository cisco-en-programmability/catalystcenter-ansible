#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: endpoint_analytics_anc_policies_info
short_description: Information module for Endpoint Analytics Anc Policies Info
description:
- This module represents an alias of the module endpoint_analytics_anc_policies_v1_info
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for AI Endpoint Analytics GetANCPoliciesV1
  description: Complete reference of the GetANCPoliciesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-anc-policies
notes:
  - SDK Method used are
    ai_endpoint_analytics.AIEndpointAnalytics.get_anc_policies_v1,

  - Paths used are
    get /dna/intent/api/v1/endpoint-analytics/anc-policies,
  - It should be noted that this module is an alias of endpoint_analytics_anc_policies_v1_info

"""

EXAMPLES = r"""
- name: Get all Endpoint Analytics Anc Policies Info
  cisco.catalystcenter.endpoint_analytics_anc_policies_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
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
        "name": "string"
      }
    ]
"""
