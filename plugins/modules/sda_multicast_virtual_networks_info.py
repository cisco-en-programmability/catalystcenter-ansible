#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_multicast_virtual_networks_info
short_description: Information module for Sda Multicast Virtual Networks
description:
  - Get all Sda Multicast Virtual Networks.
  - Returns a list of multicast configurations for virtual networks that match the.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  fabricId:
    description:
      - FabricId query parameter. ID of the fabric site where multicast is configured.
    type: str
  virtualNetworkName:
    description:
      - VirtualNetworkName query parameter. Name of the virtual network associated to the multicast configuration.
    type: str
  offset:
    description:
      - Offset query parameter. Starting record for pagination.
    type: int
  limit:
    description:
      - >
        Limit query parameter. Maximum number of records to return. The maximum number of objects supported in a
        single request is 500.
    type: int
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for SDA GetMulticastVirtualNetworks
    description: Complete reference of the GetMulticastVirtualNetworks API.
    link: https://developer.cisco.com/docs/dna-center/#!get-multicast-virtual-networks
notes:
  - SDK Method used are
    sda.Sda.get_multicast_virtual_networks,
  - Paths used are
    get /dna/intent/api/v1/sda/multicast/virtualNetworks,
"""

EXAMPLES = r"""
---
- name: Get all Sda Multicast Virtual Networks
  cisco.catalystcenter.sda_multicast_virtual_networks_info:
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
    offset: 1
    limit: 500
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": {},
          "fabricId": {},
          "virtualNetworkName": {},
          "ipPoolName": {},
          "ipv4SsmRanges": {},
          "enableSsmForV6OnlyPool": {},
          "multicastRPs": [
            {
              "rpDeviceLocation": {},
              "ipv4Address": {},
              "ipv6Address": {},
              "isDefaultV4RP": {},
              "isDefaultV6RP": {},
              "networkDeviceIds": {},
              "ipv4AsmRanges": {},
              "ipv6AsmRanges": {}
            }
          ]
        }
      ],
      "version": "string"
    }
"""
