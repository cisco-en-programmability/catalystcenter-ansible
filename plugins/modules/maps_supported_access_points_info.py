#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: maps_supported_access_points_info
short_description: Information module for Maps Supported Access Points Info
description:
- This module represents an alias of the module maps_supported_access_points_v1_info
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- catalystcentersdk >= 2.3.7.6
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Sites MapsSupportedAccessPointsV1
  description: Complete reference of the MapsSupportedAccessPointsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!maps-supported-access-points
notes:
  - SDK Method used are
    sites.Sites.maps_supported_access_points_v1,

  - Paths used are
    get /dna/intent/api/v1/maps/supported-access-points,
  - It should be noted that this module is an alias of maps_supported_access_points_v1_info

"""

EXAMPLES = r"""
- name: Get all Maps Supported Access Points Info
  cisco.catalystcenter.maps_supported_access_points_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "antennaPatterns": [
          {
            "band": "string",
            "names": [
              "string"
            ]
          }
        ],
        "apType": "string"
      }
    ]
"""
