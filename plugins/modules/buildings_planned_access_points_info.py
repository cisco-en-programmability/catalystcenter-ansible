#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: buildings_planned_access_points_info
short_description: Information module for Buildings Planned Access Points
description:
  - Get all Buildings Planned Access Points.
  - Provides a list of Planned Access Points for the Building it is requested for.
version_added: '6.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  buildingId:
    description:
      - BuildingId path parameter. The instance UUID of the building hierarchy element.
    type: str
  limit:
    description:
      - Limit query parameter. The number of records to show for this page;The minimum is 1, and the maximum is 500.
    type: int
  offset:
    description:
      - >
        Offset query parameter. The page offset for the response. E.g. If limit=100, offset=0 will return first
        100 records, offset=1 will return next 100 records, etc.
    type: int
  radios:
    description:
      - Radios query parameter. Whether to include the planned radio details of the planned access points.
    type: bool
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Devices GetPlannedAccessPointsForBuilding
    description: Complete reference of the GetPlannedAccessPointsForBuilding API.
    link: https://developer.cisco.com/docs/dna-center/#!get-planned-access-points-for-building
notes:
  - SDK Method used are
    devices.Devices.get_planned_access_points_for_building,
  - Paths used are
    get /dna/intent/api/v1/buildings/{buildingId}/planned-access-points,
"""

EXAMPLES = r"""
---
- name: Get all Buildings Planned Access Points
  cisco.catalystcenter.buildings_planned_access_points_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    limit: 0
    offset: 0
    radios: true
    buildingId: string
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
        {
          "attributes": {
            "createDate": 0,
            "domain": "string",
            "heirarchyName": "string",
            "id": 0,
            "instanceUuid": "string",
            "macAddress": "string",
            "name": "string",
            "source": "string",
            "typeString": "string"
          },
          "location": {
            "altitude": 0,
            "lattitude": 0,
            "longtitude": 0
          },
          "position": {
            "x": 0,
            "y": 0,
            "z": 0
          },
          "radioCount": 0,
          "radios": [
            {
              "antenna": {
                "azimuthAngle": 0,
                "elevationAngle": 0,
                "gain": 0,
                "mode": "string",
                "name": "string",
                "type": "string"
              },
              "attributes": {
                "channel": 0,
                "channelString": "string",
                "id": 0,
                "ifMode": "string",
                "ifTypeString": "string",
                "ifTypeSubband": "string",
                "instanceUuid": "string",
                "slotId": 0,
                "txPowerLevel": 0
              },
              "isSensor": true
            }
          ],
          "isSensor": true
        }
      ],
      "version": 0,
      "total": 0
    }
"""
