#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_extranetPolicies_info
short_description: Information module for Sda Extranetpolicies
description:
- Get all Sda Extranetpolicies.
- Returns a list of extranet policies that match the provided query parameters.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  extranetPolicyName:
    description:
    - ExtranetPolicyName query parameter. Name of the extranet policy.
    type: str
  offset:
    description:
    - Offset query parameter. Starting record for pagination.
    type: float
  limit:
    description:
    - Limit query parameter. Maximum number of records to return.
    type: float
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for SDA GetExtranetPoliciesV1
  description: Complete reference of the GetExtranetPoliciesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-extranet-policies-v-1
notes:
  - SDK Method used are
    sda.Sda.get_extranet_policies_v1,

  - Paths used are
    get /dna/intent/api/v1/sda/extranetPolicies,

"""

EXAMPLES = r"""
- name: Get all Sda Extranetpolicies
  cisco.catalystcenter.sda_extranetPolicies_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    extranetPolicyName: string
    offset: 0
    limit: 0
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "extranetPolicyName": "string",
          "fabricIds": [
            "string"
          ],
          "providerVirtualNetworkName": "string",
          "subscriberVirtualNetworkNames": [
            "string"
          ]
        }
      ],
      "version": "string"
    }
"""
