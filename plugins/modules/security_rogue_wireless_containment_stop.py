#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: security_rogue_wireless-containment_stop
short_description: Resource module for Security Rogue Wireless-Containment Stop
description:
- Manage operation create of the resource Security Rogue Wireless-Containment Stop.
- >
   Intent API to stop the wireless rogue access point containment. This API will stop the containment through single
   WLC. The response includes the details like WLC and BSSID on which the stop containment has been initiated.
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
  wlcIp:
    description: Wlc Ip.
    type: str
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Devices StopWirelessRogueAPContainmentV1
  description: Complete reference of the StopWirelessRogueAPContainmentV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!stop-wireless-rogue-ap-containment-v-1
notes:
  - SDK Method used are
    devices.Devices.stop_wireless_rogue_ap_containment_v1,

  - Paths used are
    post /dna/intent/api/v1/security/rogue/wireless-containment/stop,

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.security_rogue_wireless-containment_stop:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    macAddress: string
    type: 0
    wlcIp: string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
