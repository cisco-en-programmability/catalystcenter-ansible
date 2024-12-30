#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: floors_settings
short_description: Resource module for Floors Settings
description:
- This module represents an alias of the module floors_settings_v2
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  unitsOfMeasure:
    description: Floor units of measure.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Site Design UpdatesFloorSettingsV2
  description: Complete reference of the UpdatesFloorSettingsV2 API.
  link: https://developer.cisco.com/docs/dna-center/#!updates-floor-settings
notes:
  - SDK Method used are
    site_design.SiteDesign.updates_floor_settings_v2,

  - Paths used are
    put /dna/intent/api/v2/floors/settings,
  - It should be noted that this module is an alias of floors_settings_v2

"""

EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.floors_settings:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    unitsOfMeasure: string

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
