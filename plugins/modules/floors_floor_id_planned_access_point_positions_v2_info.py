#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: floors_floor_id_planned_access_point_positions_v2_info
short_description: Information module for Floors Floor Id Planned Access Point Positions V2
description:
- Get all Floors Floor Id Planned Access Point Positions V2.
- Retrieve all Planned Access Points Positions designated for a specific floor.
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
    - Name query parameter. Planned Access Point name.
    type: str
  macAddress:
    description:
    - MacAddress query parameter. Planned Access Point mac address.
    type: str
  type:
    description:
    - Type query parameter. Planned Access Point type.
    type: str
  offset:
    description:
    - Offset query parameter. The first record to show for this page; the first record is numbered 1. Minimum 1.
    type: float
  limit:
    description:
    - Limit query parameter. The number of records to show for this page;The minimum is 1, and the maximum is 500.
    type: float
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Site Design GetPlannedAccessPointsPositionsV2
  description: Complete reference of the GetPlannedAccessPointsPositionsV2 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-planned-access-points-positions
notes:
  - SDK Method used are
    site_design.SiteDesign.get_planned_access_points_positions_v2,

  - Paths used are
    get /dna/intent/api/v2/floors/{floorId}/plannedAccessPointPositions,

"""

EXAMPLES = r"""
- name: Get all Floors Floor Id Planned Access Point Positions V2
  cisco.catalystcenter.floors_floor_id_planned_access_point_positions_v2_info:
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
    offset: 0
    limit: 0
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
      "response": [
        {
          "name": "string",
          "macAddress": "string",
          "type": "string",
          "position": {
            "x": 0,
            "y": 0,
            "z": 0
          },
          "radios": [
            {
              "bands": [
                0
              ],
              "channel": 0,
              "txPower": 0,
              "antenna": {
                "name": "string",
                "azimuth": 0,
                "elevation": 0
              },
              "id": "string"
            }
          ],
          "id": "string"
        }
      ],
      "version": "string"
    }
"""
