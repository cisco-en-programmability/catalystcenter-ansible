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
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for AI Endpoint Analytics GetANCPoliciesV1
    description: Complete reference of the GetANCPoliciesV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-anc-policies
notes:
  - SDK Method used are a_i_endpoint_analytics.AIEndpointAnalytics.get_anc_policies_v1,
  - Paths used are get /dna/intent/api/v1/endpoint-analytics/anc-policies,
  - It should be noted that this module is an alias of endpoint_analytics_anc_policies_v1_info
"""
EXAMPLES = r"""
- name: Get all Endpoint Analytics Anc Policies Info
  cisco.catalystcenter.endpoint_analytics_anc_policies_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
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
