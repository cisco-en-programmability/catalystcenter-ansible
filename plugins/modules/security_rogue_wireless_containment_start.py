#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: security_rogue_wireless_containment_start
short_description: Resource module for Security Rogue Wireless Containment Start
description:
- This module represents an alias of the module security_rogue_wireless_containment_start_v1
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  macAddress:
    description: Mac Address.
    type: str
  type:
    description: Type.
    type: int
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices StartWirelessRogueAPContainmentV1
  description: Complete reference of the StartWirelessRogueAPContainmentV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!start-wireless-rogue-ap-containment
notes:
  - SDK Method used are
    devices.Devices.start_wireless_rogue_ap_containment_v1,

  - Paths used are
    post /dna/intent/api/v1/security/rogue/wireless-containment/start,
  - It should be noted that this module is an alias of security_rogue_wireless_containment_start_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.security_rogue_wireless_containment_start:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    macAddress: string
    type: 0

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "macAddress": "string",
        "type": 0,
        "initiatedOnWlcIp": "string",
        "taskId": "string",
        "taskType": "string",
        "initiatedOnBssid": [
          "string"
        ]
      },
      "version": "string"
    }
"""
