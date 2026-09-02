#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: floors_floor_id_access_point_positions_info
short_description: Information module for Floors Floor Id Access Point Positions
description:
  - Get all Floors Floor Id Access Point Positions.
  - Retrieve all Access Points positions assigned for a specific floor.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
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
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: int
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Site Design GetAccessPointsPositions
    description: Complete reference of the GetAccessPointsPositions API.
    link: https://developer.cisco.com/docs/dna-center/#!get-access-points-positions
notes:
  - SDK Method used are
    site_design.SiteDesign.get_access_points_positions,
  - Paths used are
    get /dna/intent/api/v2/floors/{floorId}/accessPointPositions,
"""

EXAMPLES = r"""
---
- name: Get all Floors Floor Id Access Point Positions
  cisco.catalystcenter.floors_floor_id_access_point_positions_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    name: string
    macAddress: 00:00:0C:15:C0:00
    type: string
    model: string
    offset: 1
    limit: 0
    floorId: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "name": "string",
          "macAddress": "string",
          "type": "string",
          "model": "string",
          "radios": [
            {
              "id": "string",
              "bands": [
                0
              ],
              "channel": 0,
              "txPower": 0,
              "antenna": {
                "name": "string",
                "azimuth": 0,
                "elevation": 0,
                "elevationAccelerometer": true
              }
            }
          ],
          "position": {
            "x": 0,
            "y": 0,
            "z": 0
          }
        }
      ],
      "version": "string"
    }
"""
