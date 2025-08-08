#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_anycast_gateways_count_info
short_description: Information module for Sda Anycast
  Gateways Count
description:
  - Get all Sda Anycast Gateways Count.
  - Returns the count of anycast gateways that match
    the provided query parameters.
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
      - FabricId query parameter. ID of the fabric the
        anycast gateway is assigned to.
    type: str
  virtualNetworkName:
    description:
      - VirtualNetworkName query parameter. Name of
        the virtual network associated with the anycast
        gateways.
    type: str
  ipPoolName:
    description:
      - IpPoolName query parameter. Name of the IP pool
        associated with the anycast gateways.
    type: str
  vlanName:
    description:
      - VlanName query parameter. VLAN name of the anycast
        gateways.
    type: str
  vlanId:
    description:
      - >
        VlanId query parameter. VLAN ID of the anycast
        gateways. The allowed range for vlanId is 2-4093
        except for reserved VLANs 1002-1005, 2046, and
        4094.
    type: float
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA GetAnycastGatewayCount
    description: Complete reference of the GetAnycastGatewayCount
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-anycast-gateway-count
notes:
  - SDK Method used are
    sda.Sda.get_anycast_gateway_count,
  - Paths used are
    get /dna/intent/api/v1/sda/anycastGateways/count,
"""

EXAMPLES = r"""
---
- name: Get all Sda Anycast Gateways Count
  cisco.catalystcenter.sda_anycast_gateways_count_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
    fabricId: string
    virtualNetworkName: string
    ipPoolName: string
    vlanName: string
    vlanId: 0
  register: result
"""
RETURN = r"""
dnac_response:
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
