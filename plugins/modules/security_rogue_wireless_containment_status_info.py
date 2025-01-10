#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: security_rogue_wireless_containment_status_info
short_description: Information module for Security Rogue Wireless Containment Status Info
description:
- This module represents an alias of the module security_rogue_wireless_containment_status_v1_info
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  macAddress:
    description:
    - MacAddress path parameter. MAC Address of the Wireless Rogue AP.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices WirelessRogueAPContainmentStatusV1
  description: Complete reference of the WirelessRogueAPContainmentStatusV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!wireless-rogue-ap-containment-status
notes:
  - SDK Method used are
    devices.Devices.wireless_rogue_ap_containment_status_v1,

  - Paths used are
    get /dna/intent/api/v1/security/rogue/wireless-containment/status/{macAddress},
  - It should be noted that this module is an alias of security_rogue_wireless_containment_status_v1_info

"""

EXAMPLES = r"""
- name: Get Security Rogue Wireless Containment Status Info by id
  cisco.catalystcenter.security_rogue_wireless_containment_status_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    macAddress: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "macAddress": "string",
          "type": 0,
          "classification": "string",
          "containmentStatus": "string",
          "containedByWlcIp": [
            "string"
          ],
          "lastSeen": 0,
          "strongestDetectingWlcIp": "string",
          "lastTaskDetail": {
            "taskId": "string",
            "taskType": "string",
            "taskState": "string",
            "taskStartTime": 0,
            "initiatedOnWlcIp": "string",
            "initiatedOnBssid": [
              "string"
            ]
          },
          "bssidContainmentStatus": [
            {
              "bssid": "string",
              "ssid": "string",
              "radioType": "string",
              "containmentStatus": "string",
              "containedByWlcIp": "string",
              "isAdhoc": true
            }
          ]
        }
      ],
      "version": "string"
    }
"""
