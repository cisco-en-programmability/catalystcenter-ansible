#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: topology_vlan_details_v1_info
short_description: Information module for Topology Vlan Details V1
description:
  - Get all Topology Vlan Details V1.
  - Returns the list of VLAN names that are involved in a loop as identified by the
    Spanning Tree Protocol.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Topology GetVLANDetailsV1
    description: Complete reference of the GetVLANDetailsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-vlan-details
notes:
  - SDK Method used are topology.Topology.get_vlan_details_v1,
  - Paths used are get /dna/intent/api/v1/topology/vlan/vlan-names,
"""
EXAMPLES = r"""
- name: Get all Topology Vlan Details V1
  cisco.catalystcenter.topology_vlan_details_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        "string"
      ],
      "version": "string"
    }
"""
