#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: wireless_settings_dot11be_profiles_info
short_description: Information module for Wireless Settings Dot11Be Profiles Info
description:
  - This module represents an alias of the module wireless_settings_dot11be_profiles_v1_info
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
      - >
        Limit query parameter. The number of records to show for this page. Default
        is 500 if not specified. Maximum
        allowed limit is 500.
    type: float
  offset:
    description:
      - Offset query parameter. The first record to show for this page, the first
        record is numbered 1.
    type: float
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
      - IsOfDmaUpLink query parameter. OFDMA Uplink.
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
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless Get80211beProfileByIDV1
    description: Complete reference of the Get80211beProfileByIDV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-80-21-1be-profile-by-id
  - name: Cisco DNA Center documentation for Wireless Get80211beProfilesV1
    description: Complete reference of the Get80211beProfilesV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-80-21-1be-profiles
notes:
  - SDK Method used are wireless.Wireless.get80211be_profile_by_id_v1, wireless.Wireless.get80211be_profiles_v1,
  - Paths used are get /dna/intent/api/v1/wirelessSettings/dot11beProfiles, get /dna/intent/api/v1/wirelessSettings/dot11beProfiles/{id},
  - It should be noted that this module is an alias of wireless_settings_dot11be_profiles_v1_info
"""
EXAMPLES = r"""
- name: Get all Wireless Settings Dot11Be Profiles Info
  cisco.catalystcenter.wireless_settings_dot11be_profiles_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    limit: 0
    offset: 0
    profileName: string
    isOfDmaDownLink: true
    isOfDmaUpLink: true
    isMuMimoUpLink: true
    isMuMimoDownLink: true
    isOfDmaMultiRu: true
  register: result
- name: Get Wireless Settings Dot11Be Profiles Info by id
  cisco.catalystcenter.wireless_settings_dot11be_profiles_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    id: string
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
