#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: wireless_controllers_mesh_ap_neighbours_info
short_description: Information module for Wireless Controllers Mesh Ap Neighbours
  Info
description:
  - This module represents an alias of the module wireless_controllers_mesh_ap_neighbours_v1_info
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  wlcIpAddress:
    description:
      - >
        WlcIpAddress query parameter. Employ this query parameter to obtain the details
        of the Access points
        corresponding to the provided WLC IP address.
    type: str
  apName:
    description:
      - >
        ApName query parameter. Employ this query parameter to obtain the details
        of the Access points corresponding
        to the provided ap name.
    type: str
  ethernetMacAddress:
    description:
      - >
        EthernetMacAddress query parameter. Employ this query parameter to obtain
        the details of the Access points
        corresponding to the provided EthernetMacAddress.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless GetMeshApNeighboursV1
    description: Complete reference of the GetMeshApNeighboursV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-mesh-ap-neighbours
notes:
  - SDK Method used are wireless.Wireless.get_mesh_ap_neighbours_v1,
  - Paths used are get /dna/intent/api/v1/wirelessControllers/meshApNeighbours,
  - It should be noted that this module is an alias of wireless_controllers_mesh_ap_neighbours_v1_info
"""
EXAMPLES = r"""
- name: Get all Wireless Controllers Mesh Ap Neighbours Info
  cisco.catalystcenter.wireless_controllers_mesh_ap_neighbours_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    wlcIpAddress: string
    apName: string
    ethernetMacAddress: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string",
      "apName": "string",
      "ethernetMacAddress": "string",
      "neighbourMacAddress": "string",
      "wlcIpAddress": "string",
      "neighbourType": "string",
      "meshRole": "string"
    }
"""
