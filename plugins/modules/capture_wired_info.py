#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: capture_wired_info
short_description: Information module for Capture Wired
description:
  - Get all Capture Wired.
  - Retrieves wired capture sessions that have been deployed in-progress ,.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  captureStatus:
    description:
      - >
        CaptureStatus query parameter. Catalyst Center wired capture configuration status, Complete Status -
        Indicates that a wired capture is completed and packet capture is available. In Progress - Indicates
        that a wired packet capture is in progress and scheduled indicates that the packet capture is scheduled
        in future.
    type: str
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: int
  switchId:
    description:
      - SwitchId query parameter. The wired controller device's UUID.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices RetrievesWiredCaptureSessions
    description: Complete reference of the RetrievesWiredCaptureSessions API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-wired-capture-sessions
notes:
  - SDK Method used are
    devices.Devices.retrieves_wired_capture_sessions,
  - Paths used are
    get /dna/intent/api/v1/capture/wired,
"""

EXAMPLES = r"""
---
- name: Get all Capture Wired
  cisco.catalystcenter.capture_wired_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    captureStatus: string
    offset: 1
    limit: 0
    switchId: 7f422eeb-effe-4938-9371-ccf6dc2fe15e
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "deviceId": "string",
          "interfaceName": "string",
          "durationInSeconds": 0,
          "filterExpression": "string",
          "bufferType": "string",
          "bufferSizeInMb": 0
        }
      ],
      "version": "string",
      "page": {
        "count": 0,
        "offset": 0,
        "limit": 0
      }
    }
"""
