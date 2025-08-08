#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_supervisor_card_details_info
short_description: Information module for Network Device
  Supervisor Card Details
description:
  - Get all Network Device Supervisor Card Details.
  - Get supervisor card detail for a given deviceuuid.
    Response will contain serial no, part no, switch
    no and slot no.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deviceUuid:
    description:
      - DeviceUuid path parameter. Instanceuuid of device.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices
      GetSupervisorCardDetail
    description: Complete reference of the GetSupervisorCardDetail
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-supervisor-card-detail
notes:
  - SDK Method used are
    devices.Devices.get_supervisor_card_detail,
  - Paths used are
    get /dna/intent/api/v1/network-device/{deviceUuid}/supervisor-card,
"""

EXAMPLES = r"""
---
- name: Get all Network Device Supervisor Card Details
  cisco.catalystcenter.network_device_supervisor_card_details_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
    deviceUuid: string
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
          "serialno": "string",
          "partno": "string",
          "switchno": "string",
          "slotno": "string"
        }
      ],
      "version": "string"
    }
"""
