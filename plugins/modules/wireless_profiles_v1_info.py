#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_profiles_v1_info
short_description: Information module for Wireless Profiles V1
description:
- Get all Wireless Profiles V1.
- Get Wireless Profiles V1 by id.
- This API allows the user to get a Wireless Network Profile by ID.
- This API allows the user to get all Wireless Network Profiles.
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
      Limit query parameter. The number of records to show for this page. Default is 500 if not specified. Maximum
      allowed limit is 500.
    type: float
  offset:
    description:
    - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: float
  wirelessProfileName:
    description:
    - WirelessProfileName query parameter. Wireless Profile Name.
    type: str
  id:
    description:
    - Id path parameter. Wireless Profile Id.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless GetWirelessProfileByIDV1
  description: Complete reference of the GetWirelessProfileByIDV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-wireless-profile-by-id
- name: Cisco DNA Center documentation for Wireless GetWirelessProfilesV1
  description: Complete reference of the GetWirelessProfilesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-wireless-profiles
notes:
  - SDK Method used are
    wireless.Wireless.get_wireless_profile_by_id_v1,
    wireless.Wireless.get_wireless_profiles_v1,

  - Paths used are
    get /dna/intent/api/v1/wirelessProfiles,
    get /dna/intent/api/v1/wirelessProfiles/{id},

"""

EXAMPLES = r"""
- name: Get all Wireless Profiles V1
  cisco.catalystcenter.wireless_profiles_v1_info:
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
    wirelessProfileName: string
  register: result

- name: Get Wireless Profiles V1 by id
  cisco.catalystcenter.wireless_profiles_v1_info:
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
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "wirelessProfileName": "string",
        "ssidDetails": [
          {
            "ssidName": "string",
            "flexConnect": {
              "enableFlexConnect": true,
              "localToVlan": 0
            },
            "enableFabric": true,
            "wlanProfileName": "string",
            "interfaceName": "string",
            "policyProfileName": "string",
            "dot11beProfileId": "string",
            "anchorGroupName": "string",
            "vlanGroupName": "string"
          }
        ],
        "id": "string",
        "additionalInterfaces": [
          "string"
        ],
        "apZones": [
          {
            "apZoneName": "string",
            "rfProfileName": "string",
            "ssids": [
              "string"
            ]
          }
        ]
      },
      "version": "string"
    }
"""
