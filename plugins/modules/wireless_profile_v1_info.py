#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_profile_v1_info
short_description: Information module for Wireless Profile V1
description:
- Get all Wireless Profile V1.
- Gets either one or all the wireless network profiles if no name is provided for network-profile.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  profileName:
    description:
    - ProfileName query parameter. Wireless Network Profile Name.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless GetWirelessProfileV1
  description: Complete reference of the GetWirelessProfileV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-wireless-profile
notes:
  - SDK Method used are
    wireless.Wireless.get_wireless_profile_v1,

  - Paths used are
    get /dna/intent/api/v1/wireless/profile,

"""

EXAMPLES = r"""
- name: Get all Wireless Profile V1
  cisco.catalystcenter.wireless_profile_v1_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    profileName: string
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
        "profileDetails": {
          "name": "string",
          "sites": [
            "string"
          ],
          "ssidDetails": [
            {
              "name": "string",
              "type": "string",
              "enableFabric": true,
              "flexConnect": {
                "enableFlexConnect": true,
                "localToVlan": 0
              },
              "interfaceName": "string",
              "wlanProfileName": "string",
              "policyProfileName": "string"
            }
          ]
        }
      }
    ]
"""
