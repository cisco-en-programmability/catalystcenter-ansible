#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_device_management_address_update_v1
short_description: Resource module for Network Device Management Address Update V1
description:
  - Manage operation update of the resource Network Device Management Address Update
    V1.
  - This is a simple PUT API to edit the management IP Address of the device.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  deviceid:
    description: Deviceid path parameter. The UUID of the device whose management
      IP address is to be updated.
    type: str
  newIP:
    description: New IP Address of the device to be Updated.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices UpdateDeviceManagementAddressV1
    description: Complete reference of the UpdateDeviceManagementAddressV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!update-device-management-address
notes:
  - SDK Method used are devices.Devices.update_device_management_address_v1,
  - Paths used are put /dna/intent/api/v1/network-device/{deviceid}/management-address,
"""
EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.network_device_management_address_update_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    deviceid: string
    newIP: string
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
