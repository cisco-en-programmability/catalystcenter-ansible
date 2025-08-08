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
version_added: '6.15.0'
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
  - name: Cisco DNA Center documentation for Site Design
      GetFloorSettingsV2
    description: Complete reference of the GetFloorSettingsV2
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-floor-settings-v-2
notes:
  - SDK Method used are
    site_design.SiteDesign.get_floor_settings_v2,
  - Paths used are
    get /dna/intent/api/v2/floors/settings,
"""

EXAMPLES = r"""
---
- name: Get all Floors Settings
  cisco.catalystcenter.floors_settings_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
