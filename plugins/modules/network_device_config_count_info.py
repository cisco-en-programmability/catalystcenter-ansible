#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_device_config_count_info
short_description: Information module for Network Device Config Count Info
description:
  - This module represents an alias of the module network_device_config_count_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices GetDeviceConfigCountV1
    description: Complete reference of the GetDeviceConfigCountV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-device-config-count
notes:
  - SDK Method used are devices.Devices.get_device_config_count_v1,
  - Paths used are get /dna/intent/api/v1/network-device/config/count,
  - It should be noted that this module is an alias of network_device_config_count_v1_info
"""
EXAMPLES = r"""
- name: Get all Network Device Config Count Info
  cisco.catalystcenter.network_device_config_count_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
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
