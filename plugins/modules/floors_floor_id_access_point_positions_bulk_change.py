#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: floors_floor_id_access_point_positions_bulk_change
short_description: Resource module for Floors Floor Id Access Point Positions Bulk Change
description:
  - Manage operation create of the resource Floors Floor Id Access Point Positions Bulk Change.
  - Position or reposition the Access Points on the map.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  floorId:
    description: FloorId path parameter. Floor Id.
    type: str
  payload:
    description: Floors Floor Id Access Point Positions Bulk Change's payload.
    elements: dict
    type: list
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Site Design EditTheAccessPointsPositions
    description: Complete reference of the EditTheAccessPointsPositions API.
    link: https://developer.cisco.com/docs/dna-center/#!edit-the-access-points-positions
notes:
  - SDK Method used are
    site_design.SiteDesign.edit_the_access_points_positions,
  - Paths used are
    post /dna/intent/api/v2/floors/{floorId}/accessPointPositions/bulkChange,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.floors_floor_id_access_point_positions_bulk_change:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    floorId: string
    payload:
      - {}
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
