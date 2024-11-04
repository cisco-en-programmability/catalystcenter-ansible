#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: business_sda_virtual_network_summary_info
short_description: Information module for Business Sda Virtual Network Summary
description:
- Get all Business Sda Virtual Network Summary.
- Get Virtual Network Summary.
version_added: '6.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  siteNameHierarchy:
    description:
    - SiteNameHierarchy query parameter. Complete fabric siteNameHierarchy Path.
    type: str
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for SDA GetVirtualNetworkSummaryV1
  description: Complete reference of the GetVirtualNetworkSummaryV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-virtual-network-summary-v-1
notes:
  - SDK Method used are
    sda.Sda.get_virtual_network_summary_v1,

  - Paths used are
    get /dna/intent/api/v1/business/sda/virtual-network/summary,

"""

EXAMPLES = r"""
- name: Get all Business Sda Virtual Network Summary
  cisco.catalystcenter.business_sda_virtual_network_summary_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    siteNameHierarchy: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "virtualNetworkCount": 0,
      "virtualNetworkSummary": [
        {
          "virtualNetworkContextId": "string",
          "virtualNetworkId": "string",
          "siteNameHierarchy": "string",
          "virtualNetworkName": "string",
          "layer3Instance": 0,
          "virtualNetworkStatus": "string"
        }
      ],
      "status": "string",
      "description": "string",
      "executionId": "string"
    }
"""
