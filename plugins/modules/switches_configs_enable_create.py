#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: switches_configs_enable_create
short_description: Resource module for Switches Configs Enable Create
description:
  - Manage operation create of the resource Switches Configs Enable Create.
  - Enables deployed configuration learning for the specified switches.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  deviceUuids:
    description: One or more switch UUIDs. The Network device id can be identified from the GET network device API /dna/intent/api/v1/network-device
      response.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wired EnablePerDeviceConfigurationPDCLearning
    description: Complete reference of the EnablePerDeviceConfigurationPDCLearning API.
    link: https://developer.cisco.com/docs/dna-center/#!enable-per-device-configuration-pdc-learning
notes:
  - SDK Method used are
    wired.Wired.enable_per_device_configuration_pdc_learning,
  - Paths used are
    post /dna/campus/api/v1/switches/configs/enable,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.switches_configs_enable_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    deviceUuids:
      - 8a4f95df-13da-4f5a-9a89-95ca4f8f6f79
      - 8a4f95df-13da-4f5a-9a89-95ca4f8f6f80
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
