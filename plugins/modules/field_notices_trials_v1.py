#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: field_notices_trials_v1
short_description: Resource module for Field Notices Trials V1
description:
- Manage operation create of the resource Field Notices Trials V1.
- Creates a trial for field notices detection on network devices. The consent to.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options: {}
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Compliance CreatesATrialForFieldNoticesDetectionOnNetworkDevicesV1
  description: Complete reference of the CreatesATrialForFieldNoticesDetectionOnNetworkDevicesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!creates-a-trial-for-field-notices-detection-on-network-devices
notes:
  - SDK Method used are
    compliance.Compliance.creates_a_trial_for_field_notices_detection_on_network_devices_v1,

  - Paths used are
    post /dna/intent/api/v1/fieldNotices/trials,

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.field_notices_trials_v1:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    state: present

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
