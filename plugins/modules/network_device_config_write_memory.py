#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_config_write_memory
short_description: Resource module for Network Device
  Config Write Memory
description:
  - Manage operation create of the resource Network
    Device Config Write Memory.
  - This operation would commit device running configuration
    to startup by issuing "write memory" to device.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  deviceId:
    description: UUID of the device.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Configuration
      Archive CommitDeviceConfiguration
    description: Complete reference of the CommitDeviceConfiguration
      API.
    link: https://developer.cisco.com/docs/dna-center/#!commit-device-configuration
notes:
  - SDK Method used are
    configuration_archive.ConfigurationArchive.commit_device_configuration,
  - Paths used are
    post /dna/intent/api/v1/network-device-config/write-memory,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.network_device_config_write_memory:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    deviceId:
      - string
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
