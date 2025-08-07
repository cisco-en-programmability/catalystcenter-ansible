#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: security_rogue_wireless_containment_stop
short_description: Resource module for Security Rogue
  Wireless-Containment Stop
description:
  - Manage operation create of the resource Security
    Rogue Wireless-Containment Stop. - > Intent API
    to stop the wireless rogue access point containment.
    This API will stop the containment through single
    WLC. The response includes the details like WLC
    and BSSID on which the stop containment has been
    initiated.
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
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices
      StopWirelessRogueAPContainment
    description: Complete reference of the StopWirelessRogueAPContainment
      API.
    link: https://developer.cisco.com/docs/dna-center/#!stop-wireless-rogue-ap-containment
notes:
  - SDK Method used are
    devices.Devices.stop_wireless_rogue_ap_containment,
  - Paths used are
    post /dna/intent/api/v1/security/rogue/wireless-containment/stop,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.security_rogue_wireless-containment_stop:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    macAddress: string
    type: 0
    wlcIp: string
"""
RETURN = r"""
dnac_response:
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
