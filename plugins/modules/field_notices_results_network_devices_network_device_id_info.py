#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: field_notices_results_network_devices_network_device_id_info
short_description: Information module for Field Notices Results Network Devices Network Device Id Info
description:
- This module represents an alias of the module field_notices_results_network_devices_network_device_id_v1_info
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
    - NetworkDeviceId path parameter. Id of the network device.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Compliance GetFieldNoticeNetworkDeviceByDeviceIdV1
  description: Complete reference of the GetFieldNoticeNetworkDeviceByDeviceIdV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-field-notice-network-device-by-device-id
notes:
  - SDK Method used are
    compliance.Compliance.get_field_notice_network_device_by_device_id_v1,

  - Paths used are
    get /dna/intent/api/v1/fieldNotices/results/networkDevices/{networkDeviceId},
  - It should be noted that this module is an alias of field_notices_results_network_devices_network_device_id_v1_info

"""

EXAMPLES = r"""
- name: Get Field Notices Results Network Devices Network Device Id Info by id
  cisco.catalystcenter.field_notices_results_network_devices_network_device_id_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    networkDeviceId: string
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
        "networkDeviceId": "string",
        "noticeCount": 0,
        "potentialNoticeCount": 0,
        "scanStatus": "string",
        "comments": "string",
        "lastScanTime": 0
      },
      "version": "string"
    }
"""
