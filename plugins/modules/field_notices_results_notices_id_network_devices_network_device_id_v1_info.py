#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: field_notices_results_notices_id_network_devices_network_device_id_v1_info
short_description: Information module for Field Notices Results Notices Id Network
  Devices Network Device Id V1
description:
  - Get Field Notices Results Notices Id Network Devices Network Device Id V1 by id.
  - Get field notice network device for the notice by network device id.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Id of the field notice.
    type: str
  networkDeviceId:
    description:
      - NetworkDeviceId path parameter. Id of the network device.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Compliance GetFieldNoticeNetworkDeviceForTheNoticeByNetworkDeviceIdV1
    description: Complete reference of the GetFieldNoticeNetworkDeviceForTheNoticeByNetworkDeviceIdV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-field-notice-network-device-for-the-notice-by-network-device-id
notes:
  - SDK Method used are
    compliance.Compliance.get_field_notice_network_device_for_the_notice_by_network_device_id_v1,
  - Paths used are get
    /dna/intent/api/v1/fieldNotices/results/notices/{id}/networkDevices/{networkDeviceId},
"""
EXAMPLES = r"""
- name: Get Field Notices Results Notices Id Network Devices Network Device Id V1
    by id
  cisco.catalystcenter.field_notices_results_notices_id_network_devices_network_device_id_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    id: string
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
