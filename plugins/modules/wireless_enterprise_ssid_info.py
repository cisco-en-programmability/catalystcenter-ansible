#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: wireless_enterprise_ssid_info
short_description: Information module for Wireless Enterprise Ssid Info
description:
- This module represents an alias of the module wireless_enterprise_ssid_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  ssidName:
    description:
    - >
      SsidName query parameter. Enter the enterprise SSID name that needs to be retrieved. If not entered, all the
      enterprise SSIDs will be retrieved.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless GetEnterpriseSSIDV1
  description: Complete reference of the GetEnterpriseSSIDV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-enterprise-ssid
notes:
  - SDK Method used are
    wireless.Wireless.get_enterprise_ssid_v1,

  - Paths used are
    get /dna/intent/api/v1/enterprise-ssid,
  - It should be noted that this module is an alias of wireless_enterprise_ssid_v1_info

"""

EXAMPLES = r"""
- name: Get all Wireless Enterprise Ssid Info
  cisco.catalystcenter.wireless_enterprise_ssid_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    ssidName: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "instanceUuid": "string",
        "version": 0,
        "ssidDetails": [
          {
            "name": "string",
            "wlanType": "string",
            "enableFastLane": true,
            "securityLevel": "string",
            "authServer": "string",
            "passphrase": "string",
            "trafficType": "string",
            "enableMACFiltering": true,
            "isEnabled": true,
            "isFabric": true,
            "fastTransition": "string",
            "radioPolicy": "string",
            "enableBroadcastSSID": true,
            "nasOptions": [
              "string"
            ],
            "aaaOverride": true,
            "coverageHoleDetectionEnable": true,
            "protectedManagementFrame": "string",
            "multiPSKSettings": [
              {
                "priority": 0,
                "passphraseType": "string",
                "passphrase": "string"
              }
            ],
            "clientRateLimit": 0,
            "enableSessionTimeOut": true,
            "sessionTimeOut": 0,
            "enableClientExclusion": true,
            "clientExclusionTimeout": 0,
            "enableBasicServiceSetMaxIdle": true,
            "basicServiceSetClientIdleTimeout": 0,
            "enableDirectedMulticastService": true,
            "enableNeighborList": true,
            "mfpClientProtection": "string"
          }
        ],
        "groupUuid": "string",
        "inheritedGroupUuid": "string",
        "inheritedGroupName": "string"
      }
    ]
"""
