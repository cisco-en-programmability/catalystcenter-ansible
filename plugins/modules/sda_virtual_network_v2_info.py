#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_virtual_network_v2_info
short_description: Information module for Sda Virtual Network V2
description:
- Get all Sda Virtual Network V2.
- Get virtual network with scalable groups.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  virtualNetworkName:
    description:
    - VirtualNetworkName query parameter.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for SDA GetVirtualNetworkWithScalableGroupsV1
  description: Complete reference of the GetVirtualNetworkWithScalableGroupsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-virtual-network-with-scalable-groups
notes:
  - SDK Method used are
    sda.Sda.get_virtual_network_with_scalable_groups_v1,

  - Paths used are
    get /dna/intent/api/v1/virtual-network,

"""

EXAMPLES = r"""
- name: Get all Sda Virtual Network V2
  cisco.catalystcenter.sda_virtual_network_v2_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    virtualNetworkName: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "virtualNetworkName": "string",
      "isGuestVirtualNetwork": true,
      "scalableGroupNames": [
        "string"
      ],
      "vManageVpnId": "string",
      "virtualNetworkContextId": "string",
      "status": "string",
      "description": "string",
      "executionId": "string"
    }
"""
