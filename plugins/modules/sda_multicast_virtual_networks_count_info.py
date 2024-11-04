#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_multicast_virtualNetworks_count_info
short_description: Information module for Sda Multicast Virtualnetworks Count
description:
- Get all Sda Multicast Virtualnetworks Count.
- Returns the count of multicast configurations associated to virtual networks that match the provided query parameters.
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
    - FabricId query parameter. ID of the fabric site the multicast configuration is associated with.
    type: str
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for SDA GetMulticastVirtualNetworkCountV1
  description: Complete reference of the GetMulticastVirtualNetworkCountV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-multicast-virtual-network-count-v-1
notes:
  - SDK Method used are
    sda.Sda.get_multicast_virtual_network_count_v1,

  - Paths used are
    get /dna/intent/api/v1/sda/multicast/virtualNetworks/count,

"""

EXAMPLES = r"""
- name: Get all Sda Multicast Virtualnetworks Count
  cisco.catalystcenter.sda_multicast_virtualNetworks_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    fabricId: string
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
