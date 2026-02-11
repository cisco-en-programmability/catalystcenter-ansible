#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_summary_info
short_description: Information module for Network Device Summary
description:
  - Get all Network Device Summary.
  - Returns brief summary of device info for the given device Id.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Device ID.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Devices GetDeviceSummary
    description: Complete reference of the GetDeviceSummary API.
    link: https://developer.cisco.com/docs/dna-center/#!get-device-summary
notes:
  - SDK Method used are
    devices.Devices.get_device_summary,
  - Paths used are
    get /dna/intent/api/v1/network-device/{id}/brief,
"""

EXAMPLES = r"""
---
- name: Get all Network Device Summary
  cisco.catalystcenter.network_device_summary_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "id": "string",
        "role": "string",
        "roleSource": "string"
      },
      "version": "string"
    }
"""
