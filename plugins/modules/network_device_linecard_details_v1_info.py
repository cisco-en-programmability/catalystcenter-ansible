#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_device_linecard_details_v1_info
short_description: Information module for Network Device Linecard Details V1
description:
  - Get all Network Device Linecard Details V1.
  - Get line card detail for a given deviceuuid. Response will contain serial no,
    part no, switch no and slot no.
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
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices GetLinecardDetailsV1
    description: Complete reference of the GetLinecardDetailsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-linecard-details
notes:
  - SDK Method used are devices.Devices.get_linecard_details_v1,
  - Paths used are get /dna/intent/api/v1/network-device/{deviceUuid}/line-card,
"""
EXAMPLES = r"""
- name: Get all Network Device Linecard Details V1
  cisco.catalystcenter.network_device_linecard_details_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    deviceUuid: string
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
          "serialno": "string",
          "partno": "string",
          "switchno": "string",
          "slotno": "string"
        }
      ],
      "version": "string"
    }
"""
