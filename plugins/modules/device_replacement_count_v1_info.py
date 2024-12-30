#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_replacement_count_v1_info
short_description: Information module for Device Replacement Count V1
description:
- Get all Device Replacement Count V1.
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
    - >
      ReplacementStatus query parameter. Device Replacement status listREADY-FOR-REPLACEMENT, REPLACEMENT-IN-
      PROGRESS, REPLACEMENT-SCHEDULED, REPLACED, ERROR.
    elements: str
    type: list
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Device Replacement ReturnReplacementDevicesCountV1
  description: Complete reference of the ReturnReplacementDevicesCountV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!return-replacement-devices-count
notes:
  - SDK Method used are
    device_replacement.DeviceReplacement.return_replacement_devices_count_v1,

  - Paths used are
    get /dna/intent/api/v1/device-replacement/count,

"""

EXAMPLES = r"""
- name: Get all Device Replacement Count V1
  cisco.catalystcenter.device_replacement_count_v1_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    replacementStatus: []
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
