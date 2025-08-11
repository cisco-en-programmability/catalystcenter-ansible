#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_settings_power_profiles_id_info
short_description: Information module for Wireless Settings
  Power Profiles Id
description:
  - Get Wireless Settings Power Profiles Id by id.
  - This API allows the user to get a Power Profile
    by Power Profile ID that captured in wireless settings
    design.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Power Profile ID.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless
      GetPowerProfileByID
    description: Complete reference of the GetPowerProfileByID
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-power-profile-by-id
notes:
  - SDK Method used are
    wireless.Wireless.get_power_profile_by_id,
  - Paths used are
    get /dna/intent/api/v1/wirelessSettings/powerProfiles/{id},
"""

EXAMPLES = r"""
---
- name: Get Wireless Settings Power Profiles Id by id
  cisco.catalystcenter.wireless_settings_power_profiles_id_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
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
        "id": "string",
        "profileName": "string",
        "description": "string",
        "rules": [
          {
            "sequence": 0,
            "interfaceType": "string",
            "interfaceId": "string",
            "parameterType": "string",
            "parameterValue": "string"
          }
        ]
      },
      "version": "string"
    }
"""
