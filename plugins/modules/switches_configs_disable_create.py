#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: switches_configs_disable_create
short_description: Resource module for Switches Configs Disable Create
description:
  - Manage operation create of the resource Switches Configs Disable Create.
  - Disables deployed configuration learning for the specified switches.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  deviceUuids:
    description: One or more switch UUIDs.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wired DisablePerDeviceConfigurationPDCLearning
    description: Complete reference of the DisablePerDeviceConfigurationPDCLearning API.
    link: https://developer.cisco.com/docs/dna-center/#!disable-per-device-configuration-pdc-learning
notes:
  - SDK Method used are
    wired.Wired.disable_per_device_configuration_pdc_learning,
  - Paths used are
    post /dna/campus/api/v1/switches/configs/disable,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.switches_configs_disable_create:
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
  type: str
  sample: >
    "'string'"
"""
