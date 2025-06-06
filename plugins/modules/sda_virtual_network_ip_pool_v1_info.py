#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: sda_virtual_network_ip_pool_v1_info
short_description: Information module for Sda Virtual Network Ip Pool V1
description:
  - Get all Sda Virtual Network Ip Pool V1.
  - Get IP Pool from SDA Virtual Network.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  siteNameHierarchy:
    version_added: "4.0.0"
    description:
      - SiteNameHierarchy query parameter.
    type: str
  virtualNetworkName:
    description:
      - VirtualNetworkName query parameter.
    type: str
  ipPoolName:
    version_added: "4.0.0"
    description:
      - >
        IpPoolName query parameter. IpPoolName. Note Use vlanName as a value for this
        parameter if same ip pool is
        assigned to multiple virtual networks (e.g.. IpPoolName=vlan1021).
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA GetIPPoolFromSDAVirtualNetworkV1
    description: Complete reference of the GetIPPoolFromSDAVirtualNetworkV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-ip-pool-from-sda-virtual-network
notes:
  - SDK Method used are sda.Sda.get_ip_pool_from_sda_virtual_network_v1,
  - Paths used are get /dna/intent/api/v1/business/sda/virtualnetwork/ippool,
"""
EXAMPLES = r"""
- name: Get all Sda Virtual Network Ip Pool V1
  cisco.catalystcenter.sda_virtual_network_ip_pool_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    siteNameHierarchy: string
    virtualNetworkName: string
    ipPoolName: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "status": "string",
      "description": "string",
      "virtualNetworkName": "string",
      "ipPoolName": "string",
      "authenticationPolicyName": "string",
      "trafficType": "string",
      "scalableGroupName": "string",
      "isL2FloodingEnabled": true,
      "isThisCriticalPool": true
    }
"""
