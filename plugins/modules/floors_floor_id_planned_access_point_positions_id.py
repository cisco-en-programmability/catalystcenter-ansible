#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: floors_floor_id_planned_access_point_positions_id
short_description: Resource module for Floors Floor Id Planned Access Point Positions Id
description:
- This module represents an alias of the module floors_floor_id_planned_access_point_positions_id_v2
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  floorId:
    description: FloorId path parameter. Floor Id.
    type: str
  id:
    description: Id path parameter. Planned Access Point Id.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Site Design DeletePlannedAccessPointsPositionV2
  description: Complete reference of the DeletePlannedAccessPointsPositionV2 API.
  link: https://developer.cisco.com/docs/dna-center/#!delete-planned-access-points-position
notes:
  - SDK Method used are
    site_design.SiteDesign.delete_planned_access_points_position_v2,

  - Paths used are
    delete /dna/intent/api/v2/floors/{floorId}/plannedAccessPointPositions/{id},
  - It should be noted that this module is an alias of floors_floor_id_planned_access_point_positions_id_v2

"""

EXAMPLES = r"""
- name: Delete by id
  cisco.catalystcenter.floors_floor_id_planned_access_point_positions_id:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    floorId: string
    id: string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": {
        "url": "string",
        "taskId": "string"
      }
    }
"""
