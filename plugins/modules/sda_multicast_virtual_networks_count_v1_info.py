#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: sda_multicast_virtual_networks_count_v1_info
short_description: Information module for Sda Multicast Virtual Networks Count V1
description:
  - Get all Sda Multicast Virtual Networks Count V1.
  - Returns the count of multicast configurations associated to virtual networks that
    match the provided query parameters.
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
      - FabricId query parameter. ID of the fabric site the multicast configuration
        is associated with.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA GetMulticastVirtualNetworkCountV1
    description: Complete reference of the GetMulticastVirtualNetworkCountV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-multicast-virtual-network-count
notes:
  - SDK Method used are sda.Sda.get_multicast_virtual_network_count_v1,
  - Paths used are get /dna/intent/api/v1/sda/multicast/virtualNetworks/count,
"""
EXAMPLES = r"""
- name: Get all Sda Multicast Virtual Networks Count V1
  cisco.catalystcenter.sda_multicast_virtual_networks_count_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    fabricId: string
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
