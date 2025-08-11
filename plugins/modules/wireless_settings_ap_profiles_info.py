#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_settings_ap_profiles_info
short_description: Information module for Wireless Settings
  Ap Profiles
description:
  - Get all Wireless Settings Ap Profiles.
  - This API allows the user to get AP Profiles that
    captured in wireless settings design.
version_added: '6.17.0'
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
        Limit query parameter. The number of records
        to show for this page. Default is 500 if not
        specified. Maximum allowed limit is 500.
    type: str
  offset:
    description:
      - Offset query parameter. The first record to
        show for this page, the first record is numbered
        1.
    type: str
  apProfileName:
    description:
      - >
        ApProfileName query parameter. Employ this query
        parameter to obtain the details of the apProfiles
        corresponding to the provided apProfileName.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless
      GetAPProfiles
    description: Complete reference of the GetAPProfiles
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-ap-profiles
notes:
  - SDK Method used are
    wireless.Wireless.get_ap_profiles,
  - Paths used are
    get /dna/intent/api/v1/wirelessSettings/apProfiles,
"""

EXAMPLES = r"""
---
- name: Get all Wireless Settings Ap Profiles
  cisco.catalystcenter.wireless_settings_ap_profiles_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    limit: string
    offset: string
    apProfileName: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
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
          "calendarPowerProfiles": {
            "powerProfileName": "string",
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
          },
          "countryCode": "string",
          "timeZone": "string",
          "timeZoneOffsetHour": 0,
          "timeZoneOffsetMinutes": 0,
          "clientLimit": 0
        }
      ],
      "version": "string"
    }
"""
