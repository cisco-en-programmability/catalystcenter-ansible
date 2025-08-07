#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: maps_supported_access_points_info
short_description: Information module for Maps Supported
  Access Points
description:
  - Get all Maps Supported Access Points.
  - Gets the list of supported access point types as
    well as valid antenna pattern names that can be
    used for each.
version_added: '6.14.0'
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
  - name: Cisco DNA Center documentation for Sites MapsSupportedAccessPoints
    description: Complete reference of the MapsSupportedAccessPoints
      API.
    link: https://developer.cisco.com/docs/dna-center/#!maps-supported-access-points
notes:
  - SDK Method used are
    sites.Sites.maps_supported_access_points,
  - Paths used are
    get /dna/intent/api/v1/maps/supported-access-points,
"""

EXAMPLES = r"""
---
- name: Get all Maps Supported Access Points
  cisco.catalystcenter.maps_supported_access_points_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
