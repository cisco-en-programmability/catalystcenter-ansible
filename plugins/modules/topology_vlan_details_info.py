#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: topology_vlan_details_info
short_description: Information module for Topology Vlan Details
description:
  - Get all Topology Vlan Details.
  - Returns the list of VLAN names that are involved in a loop as identified by the Spanning Tree Protocol.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Topology GetVLANDetails
    description: Complete reference of the GetVLANDetails API.
    link: https://developer.cisco.com/docs/dna-center/#!get-vlan-details
notes:
  - SDK Method used are
    topology.Topology.get_vlan_details,
  - Paths used are
    get /dna/intent/api/v1/topology/vlan/vlan-names,
"""

EXAMPLES = r"""
---
- name: Get all Topology Vlan Details
  cisco.catalystcenter.topology_vlan_details_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
dnac_response:
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
