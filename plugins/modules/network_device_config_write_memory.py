#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_device_config_write_memory
short_description: Resource module for Network Device Config Write Memory
description:
  - This module represents an alias of the module network_device_config_write_memory_v1
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
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Configuration Archive CommitDeviceConfigurationV1
    description: Complete reference of the CommitDeviceConfigurationV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!commit-device-configuration
notes:
  - SDK Method used are configuration_archive.ConfigurationArchive.commit_device_configuration_v1,
  - Paths used are post /dna/intent/api/v1/network-device-config/write-memory,
  - It should be noted that this module is an alias of network_device_config_write_memory_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.network_device_config_write_memory:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    deviceId:
      - string
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
