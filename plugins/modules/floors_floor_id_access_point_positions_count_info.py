#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: floors_floor_id_access_point_positions_count_info
short_description: Information module for Floors Floor Id Access Point Positions Count Info
description:
- This module represents an alias of the module floors_floor_id_access_point_positions_count_v2_info
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  floorId:
    description:
    - FloorId path parameter. Floor Id.
    type: str
  name:
    description:
    - Name query parameter. Access Point name.
    type: str
  macAddress:
    description:
    - MacAddress query parameter. Access Point mac address.
    type: str
  type:
    description:
    - Type query parameter. Access Point type.
    type: str
  model:
    description:
    - Model query parameter. Access Point model.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Site Design GetAccessPointsPositionsCountV2
  description: Complete reference of the GetAccessPointsPositionsCountV2 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-access-points-positions-count
notes:
  - SDK Method used are
    site_design.SiteDesign.get_access_points_positions_count_v2,

  - Paths used are
    get /dna/intent/api/v2/floors/{floorId}/accessPointPositions/count,
  - It should be noted that this module is an alias of floors_floor_id_access_point_positions_count_v2_info

"""

EXAMPLES = r"""
- name: Get all Floors Floor Id Access Point Positions Count Info
  cisco.catalystcenter.floors_floor_id_access_point_positions_count_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    name: string
    macAddress: string
    type: string
    model: string
    floorId: string
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
