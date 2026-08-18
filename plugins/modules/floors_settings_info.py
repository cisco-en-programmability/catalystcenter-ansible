#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: floors_settings_info
short_description: Information module for Floors Settings
description:
  - Get all Floors Settings.
  - Gets UI user preference for floor unit system.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Site Design GetFloorSettings
    description: Complete reference of the GetFloorSettings API.
    link: https://developer.cisco.com/docs/dna-center/#!get-floor-settings
notes:
  - SDK Method used are
    site_design.SiteDesign.get_floor_settings,
  - Paths used are
    get /dna/intent/api/v2/floors/settings,
"""

EXAMPLES = r"""
---
- name: Get all Floors Settings
  cisco.catalystcenter.floors_settings_info:
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
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "unitsOfMeasure": "string"
      },
      "version": "string"
    }
"""
