#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: license_device_license_details_v1_info
short_description: Information module for License Device License Details V1
description:
  - Get all License Device License Details V1.
  - Get detailed license information of a device.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  device_uuid:
    description:
      - Device_uuid path parameter. Id of device.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Licenses DeviceLicenseDetailsV1
    description: Complete reference of the DeviceLicenseDetailsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!device-license-details
notes:
  - SDK Method used are licenses.Licenses.device_license_details_v1,
  - Paths used are get /dna/intent/api/v1/licenses/device/{device_uuid}/details,
"""
EXAMPLES = r"""
- name: Get all License Device License Details V1
  cisco.catalystcenter.license_device_license_details_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    device_uuid: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "device_uuid": "string",
      "site": "string",
      "model": "string",
      "license_mode": "string",
      "is_license_expired": true,
      "software_version": "string",
      "network_license": "string",
      "evaluation_license_expiry": "string",
      "device_name": "string",
      "device_type": "string",
      "dna_level": "string",
      "virtual_account_name": "string",
      "ip_address": "string",
      "mac_address": "string",
      "sntc_status": "string",
      "feature_license": [
        "string"
      ],
      "has_sup_cards": true,
      "udi": "string",
      "stacked_devices": [
        {
          "mac_address": "string",
          "id": 0,
          "role": "string",
          "serial_number": "string"
        }
      ],
      "is_stacked_device": true,
      "access_points": [
        {
          "ap_type": "string",
          "count": "string"
        }
      ],
      "chassis_details": {
        "board_serial_number": "string",
        "modules": [
          {
            "module_type": "string",
            "module_name": "string",
            "serial_number": "string",
            "id": 0
          }
        ],
        "supervisor_cards": [
          {
            "serial_number": "string",
            "supervisor_card_type": "string",
            "status": "string"
          }
        ],
        "port": 0
      }
    }
"""
