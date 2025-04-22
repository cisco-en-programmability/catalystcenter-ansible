#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: floors_settings_v2_info
short_description: Information module for Floors Settings V2
description:
  - Get all Floors Settings V2.
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
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Site Design GetFloorSettingsV2
    description: Complete reference of the GetFloorSettingsV2 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-floor-settings
notes:
  - SDK Method used are site_design.SiteDesign.get_floor_settings_v2,
  - Paths used are get /dna/intent/api/v2/floors/settings,
"""
EXAMPLES = r"""
- name: Get all Floors Settings V2
  cisco.catalystcenter.floors_settings_v2_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
