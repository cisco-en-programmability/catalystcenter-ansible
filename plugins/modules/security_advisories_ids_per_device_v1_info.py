#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: security_advisories_ids_per_device_v1_info
short_description: Information module for Security Advisories Ids Per Device V1
description:
  - Get Security Advisories Ids Per Device V1 by id.
  - Retrieves advisory device details for a device.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deviceId:
    description:
      - DeviceId path parameter. Device instance UUID.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Security Advisories GetAdvisoryDeviceDetailV1
    description: Complete reference of the GetAdvisoryDeviceDetailV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-advisory-device-detail
notes:
  - SDK Method used are security_advisories.SecurityAdvisories.get_advisory_device_detail_v1,
  - Paths used are get /dna/intent/api/v1/security-advisory/device/{deviceId},
"""
EXAMPLES = r"""
- name: Get Security Advisories Ids Per Device V1 by id
  cisco.catalystcenter.security_advisories_ids_per_device_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    deviceId: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "deviceId": "string",
        "advisoryIds": [
          "string"
        ],
        "hiddenAdvisoryCount": 0,
        "scanMode": "string",
        "scanStatus": "string",
        "comments": "string",
        "lastScanTime": 0
      },
      "version": "string"
    }
"""
