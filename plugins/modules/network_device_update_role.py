#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_device_update_role
short_description: Resource module for Network Device Update Role
description:
  - This module represents an alias of the module network_device_update_role_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  id:
    description: DeviceId of the Device.
    type: str
  role:
    description: Role of device as ACCESS, CORE, DISTRIBUTION, BORDER ROUTER.
    type: str
  roleSource:
    description: Role source as MANUAL / AUTO.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices UpdateDeviceRoleV1
    description: Complete reference of the UpdateDeviceRoleV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!update-device-role
notes:
  - SDK Method used are devices.Devices.update_device_role_v1,
  - Paths used are put /dna/intent/api/v1/network-device/brief,
  - It should be noted that this module is an alias of network_device_update_role_v1
"""
EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.network_device_update_role:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    id: string
    role: string
    roleSource: string
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
