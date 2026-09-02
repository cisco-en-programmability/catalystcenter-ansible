#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_settings_ap_profiles_info
short_description: Information module for Wireless Settings Ap Profiles
description:
  - Get all Wireless Settings Ap Profiles.
  - Get Wireless Settings Ap Profiles by id.
  - This API allows the user to get a AP Profile by AP Profile ID that captured in wireless settings design.
  - This API allows the user to get all AP Profiles that captured in wireless settings design.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  apProfileName:
    description:
      - ApProfileName query parameter. AP Profiles.
    type: str
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: int
  id:
    description:
      - Id path parameter. AP Profile ID.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless GetApProfileByID
    description: Complete reference of the GetApProfileByID API.
    link: https://developer.cisco.com/docs/dna-center/#!get-ap-profile-by-id
  - name: Cisco Catalyst Center documentation for Wireless GetApProfiles
    description: Complete reference of the GetApProfiles API.
    link: https://developer.cisco.com/docs/dna-center/#!get-ap-profiles
notes:
  - SDK Method used are
    wireless.Wireless.get_ap_profile_by_id,
    wireless.Wireless.get_ap_profiles,
  - Paths used are
    get /dna/intent/api/v1/wirelessSettings/apProfiles,
    get /dna/intent/api/v1/wirelessSettings/apProfiles/{id},
"""

EXAMPLES = r"""
---
- name: Get all Wireless Settings Ap Profiles
  cisco.catalystcenter.wireless_settings_ap_profiles_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    apProfileName: string
    offset: 1
    limit: 0
  register: result
- name: Get Wireless Settings Ap Profiles by id
  cisco.catalystcenter.wireless_settings_ap_profiles_info:
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
      "profile": {
        "id": "string",
        "apProfileName": "string",
        "description": "string",
        "remoteWorkerEnabled": true,
        "managementSetting": {
          "authType": "string",
          "dot1xUsername": "string",
          "dot1xPassword": "string",
          "sshEnabled": true,
          "telnetEnabled": true,
          "managementUserName": "string",
          "managementPassword": "string",
          "managementEnablePassword": "string",
          "cdpState": true
        },
        "awipsEnabled": true,
        "awipsForensicEnabled": true,
        "rogueDetectionSetting": {
          "rogueDetection": true,
          "rogueDetectionMinRssi": 0,
          "rogueDetectionTransientInterval": 0,
          "rogueDetectionReportInterval": 0
        },
        "pmfDenialEnabled": true,
        "meshEnabled": true,
        "meshSetting": {
          "bridgeGroupName": "string",
          "backhaulClientAccess": true,
          "range": 0,
          "ghz5BackhaulDataRates": "string",
          "ghz24BackhaulDataRates": "string",
          "rapDownlinkBackhaul": "string"
        },
        "apPowerProfileName": "string",
        "calendarPowerProfiles": [
          {
            "calendarProfileName": "string",
            "apPowerProfileName": "string",
            "schedulerType": "string",
            "duration": {
              "schedulerStartTime": "string",
              "schedulerEndTime": "string",
              "schedulerDay": [
                "string"
              ],
              "schedulerDate": [
                "string"
              ]
            }
          }
        ],
        "countryCode": "string",
        "timeZone": "string",
        "timeZoneOffsetHour": 0,
        "timeZoneOffsetMinutes": 0,
        "clientLimit": 0
      },
      "version": "string"
    }
"""
