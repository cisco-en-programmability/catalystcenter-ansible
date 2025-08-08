#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: field_notices_trials_info
short_description: Information module for Field Notices
  Trials
description:
  - Get all Field Notices Trials.
  - Get trial details for field notices detection on
    network devices.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Compliance
      GetTrialDetailsForFieldNoticesDetectionOnNetworkDevices
    description: Complete reference of the GetTrialDetailsForFieldNoticesDetectionOnNetworkDevices
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-trial-details-for-field-notices-detection-on-network-devices
notes:
  - SDK Method used are
    compliance.Compliance.get_trial_details_for_field_notices_detection_on_network_devices,
  - Paths used are
    get /dna/intent/api/v1/fieldNotices/trials,
"""

EXAMPLES = r"""
---
- name: Get all Field Notices Trials
  cisco.catalystcenter.field_notices_trials_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
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
        "type": "string",
        "feature": "string",
        "contractLevel": "string",
        "active": true,
        "startTime": 0,
        "endTime": 0,
        "secondsRemainingToExpiry": 0,
        "secondsSinceExpired": 0
      }
    }
"""
