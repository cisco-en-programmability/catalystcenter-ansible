#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sda_layer3_virtual_networks_count_info
short_description: Information module for Sda Layer3 Virtual Networks Count Info
description:
- This module represents an alias of the module sda_layer3_virtual_networks_count_v1_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  fabricId:
    description:
    - FabricId query parameter. ID of the fabric the layer 3 virtual network is assigned to.
    type: str
  anchoredSiteId:
    description:
    - AnchoredSiteId query parameter. Fabric ID of the fabric site the layer 3 virtual network is anchored at.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for SDA GetLayer3VirtualNetworksCountV1
  description: Complete reference of the GetLayer3VirtualNetworksCountV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-layer-3-virtual-networks-count
notes:
  - SDK Method used are
    sda.Sda.get_layer3_virtual_networks_count_v1,

  - Paths used are
    get /dna/intent/api/v1/sda/layer3VirtualNetworks/count,
  - It should be noted that this module is an alias of sda_layer3_virtual_networks_count_v1_info

"""

EXAMPLES = r"""
- name: Get all Sda Layer3 Virtual Networks Count Info
  cisco.catalystcenter.sda_layer3_virtual_networks_count_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    fabricId: string
    anchoredSiteId: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
