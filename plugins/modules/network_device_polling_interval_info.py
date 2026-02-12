#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_polling_interval_info
short_description: Information module for Network Device Polling Interval
description:
  - Get all Network Device Polling Interval.
  - Returns polling interval by device id.
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
  - name: Cisco DNA Center documentation for Devices GetPollingIntervalById
    description: Complete reference of the GetPollingIntervalById API.
    link: https://developer.cisco.com/docs/dna-center/#!get-polling-interval-by-id
notes:
  - SDK Method used are
    devices.Devices.get_polling_interval_by_id,
  - Paths used are
    get /dna/intent/api/v1/network-device/{id}/collection-schedule,
"""

EXAMPLES = r"""
---
- name: Get all Network Device Polling Interval
  cisco.catalystcenter.network_device_polling_interval_info:
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
      "response": 0,
      "version": "string"
    }
"""
