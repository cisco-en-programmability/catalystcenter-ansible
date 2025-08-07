#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_mesh_ap_neighbours_count_info
short_description: Information module for Wireless Controllers
  Mesh Ap Neighbours Count
description:
  - Get all Wireless Controllers Mesh Ap Neighbours
    Count.
  - This API returns the total number of mesh Ap Neighbours
    available.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless
      GetMeshApNeighboursCount
    description: Complete reference of the GetMeshApNeighboursCount
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-mesh-ap-neighbours-count
notes:
  - SDK Method used are
    wireless.Wireless.get_mesh_ap_neighbours_count,
  - Paths used are
    get /dna/intent/api/v1/wirelessControllers/meshApNeighbours/count,
"""

EXAMPLES = r"""
---
- name: Get all Wireless Controllers Mesh Ap Neighbours
    Count
  cisco.catalystcenter.wireless_controllers_mesh_ap_neighbours_count_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
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
