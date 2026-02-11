#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_mesh_ap_neighbours_info
short_description: Information module for Wireless Controllers Mesh Ap Neighbours
description:
  - Get all Wireless Controllers Mesh Ap Neighbours. - > Retrieves all mesh access point neighbour details, including Child,
    Parent, Neighbour, Tentative Parent, and Blocklisted statuses.
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
        WlcIpAddress query parameter. Employ this query parameter to obtain the details of the access points
        corresponding to the provided WLC IP address.
    type: str
  apName:
    description:
      - >
        ApName query parameter. Employ this query parameter to obtain the details of the access points
        corresponding to the provided access point name.
    type: str
  ethernetMacAddress:
    description:
      - >
        EthernetMacAddress query parameter. Employ this query parameter to obtain the details of the access
        points corresponding to the provided ethernet MAC address.
    type: str
  meshRole:
    description:
      - >
        MeshRole query parameter. Employ this query parameter to obtain the details of the access points
        corresponding to the provided mesh role. Allowed values are RAP or MAP.
    type: str
  neighbourType:
    description:
      - >
        NeighbourType query parameter. Employ this query parameter to obtain the details of the access points
        corresponding to the provided mesh neighbour type. Allowed values are Child, Parent, Neigh, Tentative
        Parent, Blocklisted.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Wireless GetMeshApNeighbours
    description: Complete reference of the GetMeshApNeighbours API.
    link: https://developer.cisco.com/docs/dna-center/#!get-mesh-ap-neighbours
notes:
  - SDK Method used are
    wireless.Wireless.get_mesh_ap_neighbours,
  - Paths used are
    get /dna/intent/api/v1/wirelessControllers/meshApNeighbours,
"""

EXAMPLES = r"""
---
- name: Get all Wireless Controllers Mesh Ap Neighbours
  cisco.catalystcenter.wireless_controllers_mesh_ap_neighbours_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    wlcIpAddress: string
    apName: string
    ethernetMacAddress: string
    meshRole: string
    neighbourType: string
  register: result
"""
RETURN = r"""
dnac_response:
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
      "meshRole": "string",
      "neighbourApName": "string"
    }
"""
