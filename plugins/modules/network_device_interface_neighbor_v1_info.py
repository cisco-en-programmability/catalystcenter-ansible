#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_interface_neighbor_v1_info
short_description: Information module for Network Device Interface Neighbor V1
description:
- Get all Network Device Interface Neighbor V1.
- Get connected device detail for given deviceUuid and interfaceUuid.
version_added: '6.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deviceUuid:
    description:
    - DeviceUuid path parameter. Instanceuuid of Device.
    type: str
  interfaceUuid:
    description:
    - InterfaceUuid path parameter. Instanceuuid of interface.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices GetConnectedDeviceDetailV1
  description: Complete reference of the GetConnectedDeviceDetailV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-connected-device-detail
notes:
  - SDK Method used are
    devices.Devices.get_connected_device_detail_v1,

  - Paths used are
    get /dna/intent/api/v1/network-device/{deviceUuid}/interface/{interfaceUuid}/neighbor,

"""

EXAMPLES = r"""
- name: Get all Network Device Interface Neighbor V1
  cisco.catalystcenter.network_device_interface_neighbor_v1_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    deviceUuid: string
    interfaceUuid: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "neighborDevice": "string",
        "neighborPort": "string",
        "capabilities": [
          "string"
        ]
      },
      "version": "string"
    }
"""
