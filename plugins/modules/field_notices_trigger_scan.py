#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: field_notices_trigger_scan
short_description: Resource module for Field Notices
  Trigger Scan
description:
  - Manage operation create of the resource Field Notices
    Trigger Scan.
  - Triggers a field notices scan for the supported
    network devices. The supported.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  failedDevicesOnly:
    description: FailedDevicesOnly query parameter.
      Used to specify if the scan should run only for
      the network devices that failed during the previous
      scan. If not specified, this parameter defaults
      to false.
    type: bool
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Compliance
      TriggersAFieldNoticesScanForTheSupportedNetworkDevices
    description: Complete reference of the TriggersAFieldNoticesScanForTheSupportedNetworkDevices
      API.
    link: https://developer.cisco.com/docs/dna-center/#!triggers-a-field-notices-scan-for-the-supported-network-devices
notes:
  - SDK Method used are
    compliance.Compliance.triggers_a_field_notices_scan_for_the_supported_network_devices,
  - Paths used are
    post /dna/intent/api/v1/fieldNotices/triggerScan,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.field_notices_trigger_scan:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    failedDevicesOnly: true
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
