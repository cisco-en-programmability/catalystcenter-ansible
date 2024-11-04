#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_anycastGateways_count_info
short_description: Information module for Sda Anycastgateways Count
description:
- Get all Sda Anycastgateways Count.
- Returns the count of anycast gateways that match the provided query parameters.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  fabricId:
    description:
    - FabricId query parameter. ID of the fabric the anycast gateway is assigned to.
    type: str
  virtualNetworkName:
    description:
    - VirtualNetworkName query parameter. Name of the virtual network associated with the anycast gateways.
    type: str
  ipPoolName:
    description:
    - IpPoolName query parameter. Name of the IP pool associated with the anycast gateways.
    type: str
  vlanName:
    description:
    - VlanName query parameter. VLAN name of the anycast gateways.
    type: str
  vlanId:
    description:
    - >
      VlanId query parameter. VLAN ID of the anycast gateways. The allowed range for vlanId is 2-4093 except for
      reserved VLANs 1002-1005, 2046, and 4094.
    type: float
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for SDA GetAnycastGatewayCountV1
  description: Complete reference of the GetAnycastGatewayCountV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-anycast-gateway-count-v-1
notes:
  - SDK Method used are
    sda.Sda.get_anycast_gateway_count_v1,

  - Paths used are
    get /dna/intent/api/v1/sda/anycastGateways/count,

"""

EXAMPLES = r"""
- name: Get all Sda Anycastgateways Count
  cisco.catalystcenter.sda_anycastGateways_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    fabricId: string
    virtualNetworkName: string
    ipPoolName: string
    vlanName: string
    vlanId: 0
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "count": 0
      },
      "version": "string"
    }
"""
