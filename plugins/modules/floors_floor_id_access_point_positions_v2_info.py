#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: floors_floor_id_access_point_positions_v2_info
short_description: Information module for Floors Floor Id Access Point Positions V2
description:
  - Get all Floors Floor Id Access Point Positions V2.
  - Retrieve all Access Points positions assigned for a specific floor.
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
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first
        record is numbered 1. Minimum 1.
    type: float
  limit:
    description:
      - Limit query parameter. The number of records to show for this page;The minimum
        is 1, and the maximum is 500.
    type: float
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Site Design GetAccessPointsPositionsV2
    description: Complete reference of the GetAccessPointsPositionsV2 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-access-points-positions
notes:
  - SDK Method used are site_design.SiteDesign.get_access_points_positions_v2,
  - Paths used are get /dna/intent/api/v2/floors/{floorId}/accessPointPositions,
"""
EXAMPLES = r"""
- name: Get all Floors Floor Id Access Point Positions V2
  cisco.catalystcenter.floors_floor_id_access_point_positions_v2_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    name: string
    macAddress: string
    type: string
    model: string
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
          "id": "string",
          "macAddress": "string",
          "model": "string",
          "name": "string",
          "type": "string",
          "position": {
            "x": 0,
            "y": 0,
            "z": 0
          },
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
                "elevation": 0
              }
            }
          ]
        }
      ],
      "version": "string"
    }
"""
