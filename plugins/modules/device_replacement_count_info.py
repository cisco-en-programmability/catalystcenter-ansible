#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_replacement_count_info
short_description: Information module for Device Replacement
  Count
description:
  - Get all Device Replacement Count.
  - Get replacement devices count.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  replacementStatus:
    description:
      - "ReplacementStatus query parameter. Device Replacement
        status listREADY-FOR-REPLACEMENT, REPLACEMENT-IN-
        PROGRESS, REPLACEMENT-SCHEDULED, REPLACED, ERROR.
        \n"
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Device
      Replacement ReturnReplacementDevicesCount
    description: Complete reference of the ReturnReplacementDevicesCount
      API.
    link: https://developer.cisco.com/docs/dna-center/#!return-replacement-devices-count
notes:
  - SDK Method used are
    device_replacement.DeviceReplacement.return_replacement_devices_count,
  - Paths used are
    get /dna/intent/api/v1/device-replacement/count,
"""

EXAMPLES = r"""
---
- name: Get all Device Replacement Count
  cisco.catalystcenter.device_replacement_count_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
    replacementStatus: []
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": 0,
      "version": "string"
    }
"""
