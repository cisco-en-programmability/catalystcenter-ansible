#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: capture_wired_count_info
short_description: Information module for Capture Wired Count
description:
  - Get all Capture Wired Count.
  - Retrieves the count of wired capture sessions that have been deployed in-progress , completed, or scheduled.
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
      - CaptureStatus query parameter. Catalyst Center wired capture configuration status.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices RetrievesWiredCaptureSessionCount
    description: Complete reference of the RetrievesWiredCaptureSessionCount API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-wired-capture-session-count
notes:
  - SDK Method used are
    devices.Devices.retrieves_wired_capture_session_count,
  - Paths used are
    get /dna/intent/api/v1/capture/wired/count,
"""

EXAMPLES = r"""
---
- name: Get all Capture Wired Count
  cisco.catalystcenter.capture_wired_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    captureStatus: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": 0,
      "version": "string"
    }
"""
