#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_settings_dot11be_profiles_info
short_description: Information module for Wireless Settings Dot11be Profiles
description:
  - Get all Wireless Settings Dot11be Profiles.
  - Get Wireless Settings Dot11be Profiles by id.
  - This API allows the user to get 802.11be Profile by ID.
  - This API allows the user to get all 802.11be Profiles configured under Wireless Settings.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  limit:
    description:
      - Limit query parameter.
    type: int
  offset:
    description:
      - Offset query parameter.
    type: int
  profileName:
    description:
      - ProfileName query parameter. Profile Name.
    type: str
  isOfDmaDownLink:
    description:
      - IsOfDmaDownLink query parameter. OFDMA Downlink.
    type: bool
  isOfDmaUpLink:
    description:
      - IsOfDmaUpLink query parameter. OFDMA Downlink.
    type: bool
  isMuMimoUpLink:
    description:
      - IsMuMimoUpLink query parameter. MU-MIMO Uplink.
    type: bool
  isMuMimoDownLink:
    description:
      - IsMuMimoDownLink query parameter. MU-MIMO Downlink.
    type: bool
  isOfDmaMultiRu:
    description:
      - IsOfDmaMultiRu query parameter. OFDMA Multi-RU.
    type: bool
  id:
    description:
      - Id path parameter. 802.11be Profile ID.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless Get80211beProfilesByID
    description: Complete reference of the Get80211beProfilesByID API.
    link: https://developer.cisco.com/docs/dna-center/#!get-80-21-1be-profiles-by-id
  - name: Cisco Catalyst Center documentation for Wireless GetAll80211beProfiles
    description: Complete reference of the GetAll80211beProfiles API.
    link: https://developer.cisco.com/docs/dna-center/#!get-all-80-21-1be-profiles
notes:
  - SDK Method used are
    wireless.Wireless.get80211be_profiles_by_id,
    wireless.Wireless.get_all80211be_profiles,
  - Paths used are
    get /dna/intent/api/v1/wirelessSettings/dot11beProfiles,
    get /dna/intent/api/v1/wirelessSettings/dot11beProfiles/{id},
"""

EXAMPLES = r"""
---
- name: Get all Wireless Settings Dot11be Profiles
  cisco.catalystcenter.wireless_settings_dot11be_profiles_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    limit: 500
    offset: 1
    profileName: string
    isOfDmaDownLink: true
    isOfDmaUpLink: true
    isMuMimoUpLink: true
    isMuMimoDownLink: true
    isOfDmaMultiRu: true
  register: result
- name: Get Wireless Settings Dot11be Profiles by id
  cisco.catalystcenter.wireless_settings_dot11be_profiles_info:
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
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "id": "string",
        "profileName": "string",
        "description": "string",
        "ofdmaDownLink": true,
        "ofdmaUpLink": true,
        "muMimoUpLink": true,
        "muMimoDownLink": true,
        "ofdmaMultiRu": true,
        "default": true,
        "mloGroup": {
          "primary24GhzEnable": true,
          "primary5GhzEnable": true,
          "secondary5GhzEnable": true,
          "primary6GhzEnable": true
        }
      },
      "version": "string"
    }
"""
