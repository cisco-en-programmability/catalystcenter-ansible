#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: field_notices_results_notices_id_network_devices_count_v1_info
short_description: Information module for Field Notices Results Notices Id Network
  Devices Count V1
description:
  - Get all Field Notices Results Notices Id Network Devices Count V1.
  - Get count of field notice network devices for the notice.
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
      - NetworkDeviceId query parameter. Id of the network device.
    type: str
  scanStatus:
    description:
      - >
        ScanStatus query parameter. Status of the scan on the network device. Available
        values NOT_SCANNED,
        IN_PROGRESS, SUCCESS, FAILED.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Compliance GetCountOfFieldNoticeNetworkDevicesForTheNoticeV1
    description: Complete reference of the GetCountOfFieldNoticeNetworkDevicesForTheNoticeV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-count-of-field-notice-network-devices-for-the-notice
notes:
  - SDK Method used are
    compliance.Compliance.get_count_of_field_notice_network_devices_for_the_notice_v1,
  - Paths used are get /dna/intent/api/v1/fieldNotices/results/notices/{id}/networkDevices/count,
"""
EXAMPLES = r"""
- name: Get all Field Notices Results Notices Id Network Devices Count V1
  cisco.catalystcenter.field_notices_results_notices_id_network_devices_count_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    networkDeviceId: string
    scanStatus: string
    id: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
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
