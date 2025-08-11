#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_equipment_info
short_description: Information module for Network Device
  Equipment
description:
  - Get all Network Device Equipment. - > Return all
    types of equipment details like PowerSupply, Fan,
    Chassis, Backplane, Module, PROCESSOR, Other and
    SFP for the Given device.
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
        Type query parameter. Type value can be PowerSupply,
        Fan, Chassis, Backplane, Module, PROCESSOR,
        Other, SFP. If no type is mentioned, All equipments
        are fetched for the device.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices
      GetTheDetailsOfPhysicalComponentsOfTheGivenDevice
    description: Complete reference of the GetTheDetailsOfPhysicalComponentsOfTheGivenDevice
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-the-details-of-physical-components-of-the-given-device
notes:
  - SDK Method used are
    devices.Devices.get_the_details_of_physical_components_of_the_given_device,
  - Paths used are
    get /dna/intent/api/v1/network-device/{deviceUuid}/equipment,
"""

EXAMPLES = r"""
---
- name: Get all Network Device Equipment
  cisco.catalystcenter.network_device_equipment_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    type: string
    deviceUuid: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
