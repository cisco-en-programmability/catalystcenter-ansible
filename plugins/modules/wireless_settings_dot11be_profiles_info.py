#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wirelessSettings_dot11beProfiles_info
short_description: Information module for Wirelesssettings Dot11beprofiles
description:
- Get all Wirelesssettings Dot11beprofiles.
- Get Wirelesssettings Dot11beprofiles by id.
- This API allows the user to get 802.11be Profile by ID.
- This API allows the user to get all 802.11be Profiles configured under Wireless Settings.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  limit:
    description:
    - Limit query parameter.
    type: float
  offset:
    description:
    - Offset query parameter.
    type: float
  id:
    description:
    - Id path parameter. 802.11be Profile ID.
    type: str
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Wireless Get80211beProfileByIDV1
  description: Complete reference of the Get80211beProfileByIDV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-80-21-1be-profile-by-id-v-1
- name: Cisco CATALYST Center documentation for Wireless GetAll80211beProfilesV1
  description: Complete reference of the GetAll80211beProfilesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-all-80-21-1be-profiles-v-1
notes:
  - SDK Method used are
    wireless.Wireless.get80211be_profile_by_id_v1,
    wireless.Wireless.get_all80211be_profiles_v1,

  - Paths used are
    get /dna/intent/api/v1/wirelessSettings/dot11beProfiles,
    get /dna/intent/api/v1/wirelessSettings/dot11beProfiles/{id},

"""

EXAMPLES = r"""
- name: Get all Wirelesssettings Dot11beprofiles
  cisco.catalystcenter.wirelessSettings_dot11beProfiles_info:
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
  register: result

- name: Get Wirelesssettings Dot11beprofiles by id
  cisco.catalystcenter.wirelessSettings_dot11beProfiles_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "id": "string",
        "profileName": "string",
        "ofdmaDownLink": true,
        "ofdmaUpLink": true,
        "muMimoDownLink": true,
        "muMimoUpLink": true,
        "ofdmaMultiRu": true,
        "default": true
      },
      "version": "string"
    }
"""
