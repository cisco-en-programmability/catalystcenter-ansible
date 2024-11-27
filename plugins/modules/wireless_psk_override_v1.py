#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_psk_override_v1
short_description: Resource module for Wireless Psk Override V1
description:
- Manage operation create of the resource Wireless Psk Override V1.
- Update/Override passphrase of SSID.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Wireless Psk Override's payload.
    elements: dict
    suboptions:
      passPhrase:
        description: Pass phrase (create/update).
        type: str
      site:
        description: Site name hierarchy (ex Global/aaa/zzz/...).
        type: str
      ssid:
        description: Enterprise ssid name(already created/present).
        type: str
      wlanProfileName:
        description: WLAN Profile Name.
        type: str
    type: list
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless PSKOverrideV1
  description: Complete reference of the PSKOverrideV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!p-sk-override
notes:
  - SDK Method used are
    wireless.Wireless.psk_override,

  - Paths used are
    post /dna/intent/api/v1/wireless/psk-override,

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.wireless_psk_override_v1:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    payload:
    - passPhrase: string
      site: string
      ssid: string
      wlanProfileName: string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }
"""
