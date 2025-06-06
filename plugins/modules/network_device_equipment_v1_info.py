#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_device_equipment_v1_info
short_description: Information module for Network Device Equipment V1
description:
  - Get all Network Device Equipment V1.
  - >
    Return all types of equipment details like PowerSupply, Fan, Chassis, Backplane,
    Module, PROCESSOR, Other and SFP
    for the Given device.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deviceUuid:
    description:
      - DeviceUuid path parameter.
    type: str
  type:
    description:
      - >
        Type query parameter. Type value can be PowerSupply, Fan, Chassis, Backplane,
        Module, PROCESSOR, Other, SFP.
        If no type is mentioned, All equipments are fetched for the device.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices GetTheDetailsOfPhysicalComponentsOfTheGivenDeviceV1
    description: Complete reference of the GetTheDetailsOfPhysicalComponentsOfTheGivenDeviceV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-the-details-of-physical-components-of-the-given-device
notes:
  - SDK Method used are devices.Devices.get_the_details_of_physical_components_of_the_given_device_v1,
  - Paths used are get /dna/intent/api/v1/network-device/{deviceUuid}/equipment,
"""
EXAMPLES = r"""
- name: Get all Network Device Equipment V1
  cisco.catalystcenter.network_device_equipment_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    type: string
    deviceUuid: string
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
          "operationalStateCode": "string",
          "productId": "string",
          "serialNumber": "string",
          "vendorEquipmentType": "string",
          "description": "string",
          "instanceUuid": "string",
          "name": "string",
          "manufacturer": "string"
        }
      ],
      "version": "string"
    }
"""
