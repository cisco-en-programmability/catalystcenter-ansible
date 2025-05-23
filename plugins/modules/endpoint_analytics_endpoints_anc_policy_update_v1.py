#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: endpoint_analytics_endpoints_anc_policy_update_v1
short_description: Resource module for Endpoint Analytics Endpoints Anc Policy Update
  V1
description:
  - Manage operation update of the resource Endpoint Analytics Endpoints Anc Policy
    Update V1.
  - Applies given ANC policy to the endpoint.
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  ancPolicy:
    description: ANC policy name.
    type: str
  epId:
    description: EpId path parameter. Unique identifier for the endpoint.
    type: str
  granularAncPolicy:
    description: Endpoint Analytics Endpoints Anc Policy Update's granularAncPolicy.
    elements: dict
    suboptions:
      name:
        description: Name of the granular ANC policy.
        type: str
      nasIpAddress:
        description: IP address of the network device where endpoint is attached.
        type: str
    type: list
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for AI Endpoint Analytics ApplyANCPolicyV1
    description: Complete reference of the ApplyANCPolicyV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!apply-anc-policy
notes:
  - SDK Method used are a_i_endpoint_analytics.AIEndpointAnalytics.apply_anc_policy_v1,
  - Paths used are put /dna/intent/api/v1/endpoint-analytics/endpoints/{epId}/anc-policy,
"""
EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.endpoint_analytics_endpoints_anc_policy_update_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    ancPolicy: string
    epId: string
    granularAncPolicy:
      - name: string
        nasIpAddress: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
