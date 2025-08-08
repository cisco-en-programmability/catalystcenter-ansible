#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: field_notices_trials
short_description: Resource module for Field Notices
  Trials
description:
  - Manage operation create of the resource Field Notices
    Trials.
  - Creates a trial for field notices detection on network
    devices. The consent to.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options: {}
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Compliance
      CreatesATrialForFieldNoticesDetectionOnNetworkDevices
    description: Complete reference of the CreatesATrialForFieldNoticesDetectionOnNetworkDevices
      API.
    link: https://developer.cisco.com/docs/dna-center/#!creates-a-trial-for-field-notices-detection-on-network-devices
notes:
  - SDK Method used are
    compliance.Compliance.creates_a_trial_for_field_notices_detection_on_network_devices,
  - Paths used are
    post /dna/intent/api/v1/fieldNotices/trials,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.field_notices_trials:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    state: present
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
