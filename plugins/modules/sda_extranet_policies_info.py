#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sda_extranet_policies_info
short_description: Information module for Sda Extranet Policies Info
description:
- This module represents an alias of the module sda_extranet_policies_v1_info
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
    - >
      Limit query parameter. Maximum number of records to return. The maximum number of objects supported in a
      single request is 500.
    type: float
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for SDA GetExtranetPoliciesV1
  description: Complete reference of the GetExtranetPoliciesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-extranet-policies
notes:
  - SDK Method used are
    sda.Sda.get_extranet_policies_v1,

  - Paths used are
    get /dna/intent/api/v1/sda/extranetPolicies,
  - It should be noted that this module is an alias of sda_extranet_policies_v1_info

"""

EXAMPLES = r"""
- name: Get all Sda Extranet Policies Info
  cisco.catalystcenter.sda_extranet_policies_info:
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
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
