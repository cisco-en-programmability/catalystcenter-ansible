#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_profile_info
short_description: Information module for Wireless Profile
description:
- Get all Wireless Profile.
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
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Wireless GetWirelessProfileV1
  description: Complete reference of the GetWirelessProfileV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-wireless-profile-v-1
notes:
  - SDK Method used are
    wireless.Wireless.get_wireless_profile_v1,

  - Paths used are
    get /dna/intent/api/v1/wireless/profile,

"""

EXAMPLES = r"""
- name: Get all Wireless Profile
  cisco.catalystcenter.wireless_profile_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    profileName: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
              "interfaceName": "string"
            }
          ]
        }
      }
    ]
"""
