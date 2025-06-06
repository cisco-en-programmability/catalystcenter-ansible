#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: security_rogue_wireless_containment_start_v1
short_description: Resource module for Security Rogue Wireless Containment Start V1
description:
  - Manage operation create of the resource Security Rogue Wireless Containment Start
    V1.
  - >
    Intent API to start the wireless rogue access point containment. This API will
    initiate the containment operation
    on the strongest detecting WLC for the given Rogue AP. This is a resource intensive
    operation which has legal
    implications since the rogue access point on whom it is triggered, might be a
    valid neighbor access point.
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
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices StartWirelessRogueAPContainmentV1
    description: Complete reference of the StartWirelessRogueAPContainmentV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!start-wireless-rogue-ap-containment
notes:
  - SDK Method used are devices.Devices.start_wireless_rogue_ap_containment_v1,
  - Paths used are post /dna/intent/api/v1/security/rogue/wireless-containment/start,
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.security_rogue_wireless_containment_start_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
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
