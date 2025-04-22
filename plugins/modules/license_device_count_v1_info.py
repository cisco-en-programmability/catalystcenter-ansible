#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: license_device_count_v1_info
short_description: Information module for License Device Count V1
description:
  - Get all License Device Count V1.
  - Get total number of managed devices.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  device_type:
    description:
      - Device_type query parameter. Type of device.
    type: str
  registration_status:
    description:
      - Registration_status query parameter. Smart license registration status of
        device.
    type: str
  dna_level:
    description:
      - Dna_level query parameter. Device Cisco DNA License Level.
    type: str
  virtual_account_name:
    description:
      - Virtual_account_name query parameter. Virtual account name.
    type: str
  smart_account_id:
    description:
      - Smart_account_id query parameter. Smart account id.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Licenses DeviceCountDetailsV1
    description: Complete reference of the DeviceCountDetailsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!device-count-details
notes:
  - SDK Method used are licenses.Licenses.device_count_details_v1,
  - Paths used are get /dna/intent/api/v1/licenses/device/count,
"""
EXAMPLES = r"""
- name: Get all License Device Count V1
  cisco.catalystcenter.license_device_count_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    device_type: string
    registration_status: string
    dna_level: string
    virtual_account_name: string
    smart_account_id: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": 0,
      "version": "string"
    }
"""
