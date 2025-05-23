#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: business_sda_virtual_network_summary_info
short_description: Information module for Business Sda Virtual Network Summary Info
description:
  - This module represents an alias of the module business_sda_virtual_network_summary_v1_info
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
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA GetVirtualNetworkSummaryV1
    description: Complete reference of the GetVirtualNetworkSummaryV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-virtual-network-summary
notes:
  - SDK Method used are sda.Sda.get_virtual_network_summary_v1,
  - Paths used are get /dna/intent/api/v1/business/sda/virtual-network/summary,
  - It should be noted that this module is an alias of business_sda_virtual_network_summary_v1_info
"""
EXAMPLES = r"""
- name: Get all Business Sda Virtual Network Summary Info
  cisco.catalystcenter.business_sda_virtual_network_summary_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    siteNameHierarchy: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
