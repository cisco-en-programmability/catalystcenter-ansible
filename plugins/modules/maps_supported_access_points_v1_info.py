#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: maps_supported_access_points_v1_info
short_description: Information module for Maps Supported Access Points V1
description:
- Get all Maps Supported Access Points V1.
- Gets the list of supported access point types as well as valid antenna pattern names that can be used for each.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- catalystcentersdk >= 2.3.7.9
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

"""

EXAMPLES = r"""
- name: Get all Maps Supported Access Points V1
  cisco.catalystcenter.maps_supported_access_points_v1_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
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
