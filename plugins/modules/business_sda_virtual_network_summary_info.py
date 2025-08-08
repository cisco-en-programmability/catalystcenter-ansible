#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: business_sda_virtual_network_summary_info
short_description: Information module for Business Sda
  Virtual Network Summary
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
      - SiteNameHierarchy query parameter. Complete
        fabric siteNameHierarchy Path.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA GetVirtualNetworkSummary
    description: Complete reference of the GetVirtualNetworkSummary
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-virtual-network-summary
notes:
  - SDK Method used are
    sda.Sda.get_virtual_network_summary,
  - Paths used are
    get /dna/intent/api/v1/business/sda/virtual-network/summary,
"""

EXAMPLES = r"""
---
- name: Get all Business Sda Virtual Network Summary
  cisco.catalystcenter.business_sda_virtual_network_summary_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
    siteNameHierarchy: string
  register: result
"""
RETURN = r"""
dnac_response:
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
