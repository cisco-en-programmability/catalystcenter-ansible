#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: field_notices_results_network_devices_count_info
short_description: Information module for Field Notices Results Network Devices Count
description:
  - Get all Field Notices Results Network Devices Count.
  - Get count of field notice network devices.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  networkDeviceId:
    description:
      - NetworkDeviceId query parameter. Id of the network device.
    type: str
  scanStatus:
    description:
      - >
        ScanStatus query parameter. Status of the scan on the network device. Available values NOT_SCANNED,
        IN_PROGRESS, SUCCESS, FAILED.
    type: str
  noticeCount:
    description:
      - NoticeCount query parameter. Return network devices with noticeCount greater than this noticeCount.
    type: float
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Compliance GetCountOfFieldNoticeNetworkDevices
    description: Complete reference of the GetCountOfFieldNoticeNetworkDevices API.
    link: https://developer.cisco.com/docs/dna-center/#!get-count-of-field-notice-network-devices
notes:
  - SDK Method used are
    compliance.Compliance.get_count_of_field_notice_network_devices,
  - Paths used are
    get /dna/intent/api/v1/fieldNotices/results/networkDevices/count,
"""

EXAMPLES = r"""
---
- name: Get all Field Notices Results Network Devices Count
  cisco.catalystcenter.field_notices_results_network_devices_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    networkDeviceId: string
    scanStatus: string
    noticeCount: 0
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": {
        "count": 0
      }
    }
"""
