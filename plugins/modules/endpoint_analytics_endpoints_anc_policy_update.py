#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: endpoint-analytics_endpoints_anc-policy_update
short_description: Resource module for Endpoint-Analytics Endpoints Anc-Policy Update
description:
- Manage operation update of the resource Endpoint-Analytics Endpoints Anc-Policy Update.
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
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for AI Endpoint Analytics ApplyANCPolicyV1
  description: Complete reference of the ApplyANCPolicyV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!apply-anc-policy-v-1
notes:
  - SDK Method used are
    a_i_endpoint_analytics.AIEndpointAnalytics.apply_anc_policy_v1,

  - Paths used are
    put /dna/intent/api/v1/endpoint-analytics/endpoints/{epId}/anc-policy,

"""

EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.endpoint-analytics_endpoints_anc-policy_update:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    ancPolicy: string
    epId: string
    granularAncPolicy:
    - name: string
      nasIpAddress: string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
