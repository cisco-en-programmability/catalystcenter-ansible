#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_profiles_info
short_description: Information module for Wireless Profiles
description:
  - Get all Wireless Profiles.
  - Get Wireless Profiles by id.
  - This API allows the user to get a Wireless Network Profile by ID.
  - This API allows the user to get all Wireless Network Profiles.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Wireless Profile ID.
    type: str
  limit:
    description:
      - Limit query parameter.
    type: int
  offset:
    description:
      - Offset query parameter.
    type: int
  wirelessProfileName:
    description:
      - WirelessProfileName query parameter. Wireless Profile Name.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless GetWirelessProfileByID
    description: Complete reference of the GetWirelessProfileByID API.
    link: https://developer.cisco.com/docs/dna-center/#!get-wireless-profile-by-id
  - name: Cisco Catalyst Center documentation for Wireless GetWirelessProfiles
    description: Complete reference of the GetWirelessProfiles API.
    link: https://developer.cisco.com/docs/dna-center/#!get-wireless-profiles
notes:
  - SDK Method used are
    wireless.Wireless.get_wireless_profile_by_id,
    wireless.Wireless.get_wireless_profiles,
  - Paths used are
    get /dna/intent/api/v1/wirelessProfiles,
    get /dna/intent/api/v1/wirelessProfiles/{id},
"""

EXAMPLES = r"""
---
- name: Get all Wireless Profiles
  cisco.catalystcenter.wireless_profiles_info:
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
    wirelessProfileName: sample-profile
  register: result
- name: Get Wireless Profiles by id
  cisco.catalystcenter.wireless_profiles_info:
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
        "wirelessProfileName": "string",
        "ssidDetails": [
          {
            "ssidName": "string",
            "enableFabric": true,
            "flexConnect": {
              "enableFlexConnect": true,
              "localToVlan": 0
            },
            "interfaceName": "string",
            "wlanProfileName": "string",
            "policyProfileName": "string",
            "dot11beProfileId": "string",
            "vlanGroupName": "string",
            "anchorGroupName": "string"
          }
        ],
        "apZones": [
          {
            "apZoneName": "string",
            "rfProfileName": "string",
            "ssids": [
              "string"
            ]
          }
        ],
        "additionalInterfaces": [
          "string"
        ],
        "featureTemplates": [
          {
            "id": "string",
            "ssids": [
              "string"
            ]
          }
        ],
        "id": "string"
      },
      "version": "string"
    }
"""
