#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_v2_info
short_description: Information module for Network V2
description:
  - Get all Network V2.
  - API to get SNMP, NTP, Network AAA, Client and Endpoint AAA, and/or DNS center
    server settings.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  siteId:
    description:
      - SiteId query parameter. Site Id to get the network settings associated with
        the site.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Network Settings GetNetworkV2
    description: Complete reference of the GetNetworkV2 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-network
notes:
  - SDK Method used are network_settings.NetworkSettings.get_network_v2,
  - Paths used are get /dna/intent/api/v2/network,
"""
EXAMPLES = r"""
- name: Get all Network V2
  cisco.catalystcenter.network_v2_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    siteId: string
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
        "instanceType": "string",
        "instanceUuid": "string",
        "namespace": "string",
        "type": "string",
        "key": "string",
        "version": 0,
        "value": [
          "string"
        ],
        "groupUuid": "string",
        "inheritedGroupUuid": "string",
        "inheritedGroupName": "string"
      }
    ]
"""
