#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_device_chassis_details_v1_info
short_description: Information module for Network Device Chassis Details V1
description:
  - Get all Network Device Chassis Details V1.
  - Returns chassis details for given device ID.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deviceId:
    description:
      - DeviceId path parameter. Device ID.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices GetChassisDetailsForDeviceV1
    description: Complete reference of the GetChassisDetailsForDeviceV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-chassis-details-for-device
notes:
  - SDK Method used are devices.Devices.get_chassis_details_for_device_v1,
  - Paths used are get /dna/intent/api/v1/network-device/{deviceId}/chassis,
"""
EXAMPLES = r"""
- name: Get all Network Device Chassis Details V1
  cisco.catalystcenter.network_device_chassis_details_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    deviceId: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "assemblyNumber": "string",
          "assemblyRevision": "string",
          "containmentEntity": "string",
          "description": "string",
          "entityPhysicalIndex": "string",
          "hardwareVersion": "string",
          "instanceUuid": "string",
          "isFieldReplaceable": "string",
          "isReportingAlarmsAllowed": "string",
          "manufacturer": "string",
          "name": "string",
          "partNumber": "string",
          "serialNumber": "string",
          "vendorEquipmentType": "string"
        }
      ],
      "version": "string"
    }
"""
