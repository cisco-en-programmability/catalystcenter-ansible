#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_devices_delete_without_cleanup
short_description: Resource module for Network Devices Delete Without Cleanup
description:
  - This module represents an alias of the module network_devices_delete_without_cleanup_v1
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  id:
    description: The unique identifier of the network device to be deleted.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices DeleteANetworkDeviceWithoutConfigurationCleanupV1
    description: Complete reference of the DeleteANetworkDeviceWithoutConfigurationCleanupV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!delete-a-network-device-without-configuration-cleanup
notes:
  - SDK Method used are devices.Devices.delete_a_network_device_without_configuration_cleanup_v1,
  - Paths used are post /dna/intent/api/v1/networkDevices/deleteWithoutCleanup,
  - It should be noted that this module is an alias of network_devices_delete_without_cleanup_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.network_devices_delete_without_cleanup:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    id: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
