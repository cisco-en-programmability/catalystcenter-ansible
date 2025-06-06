#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: field_notices_trigger_scan_v1
short_description: Resource module for Field Notices Trigger Scan V1
description:
  - Manage operation create of the resource Field Notices Trigger Scan V1.
  - Triggers a field notices scan for the supported network devices. The supported.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  failedDevicesOnly:
    description: FailedDevicesOnly query parameter. Used to specify if the scan should
      run only for the network devices that failed during the previous scan. If not
      specified, this parameter defaults to false.
    type: bool
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Compliance TriggersAFieldNoticesScanForTheSupportedNetworkDevicesV1
    description: Complete reference of the TriggersAFieldNoticesScanForTheSupportedNetworkDevicesV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!triggers-a-field-notices-scan-for-the-supported-network-devices
notes:
  - SDK Method used are
    compliance.Compliance.triggers_a_field_notices_scan_for_the_supported_network_devices_v1,
  - Paths used are post /dna/intent/api/v1/fieldNotices/triggerScan,
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.field_notices_trigger_scan_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    failedDevicesOnly: true
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
        "url": "string",
        "taskId": "string"
      }
    }
"""
