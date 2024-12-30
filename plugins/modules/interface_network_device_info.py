#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: interface_network_device_info
short_description: Information module for Interface Network Device Info
description:
- This module represents an alias of the module interface_network_device_v1_info
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
- name: Cisco DNA Center documentation for Devices GetInterfaceInfoByIdV1
  description: Complete reference of the GetInterfaceInfoByIdV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-interface-info-by-id
notes:
  - SDK Method used are
    devices.Devices.get_interface_info_by_id_v1,

  - Paths used are
    get /dna/intent/api/v1/interface/network-device/{deviceId},
  - It should be noted that this module is an alias of interface_network_device_v1_info

"""

EXAMPLES = r"""
- name: Get Interface Network Device Info by id
  cisco.catalystcenter.interface_network_device_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
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
          "addresses": [
            {
              "address": {
                "ipAddress": {
                  "address": "string"
                },
                "ipMask": {
                  "address": "string"
                },
                "isInverseMask": true
              },
              "type": "string"
            }
          ],
          "adminStatus": "string",
          "className": "string",
          "description": "string",
          "name": "string",
          "deviceId": "string",
          "duplex": "string",
          "id": "string",
          "ifIndex": "string",
          "instanceTenantId": "string",
          "instanceUuid": "string",
          "interfaceType": "string",
          "ipv4Address": "string",
          "ipv4Mask": "string",
          "isisSupport": "string",
          "lastOutgoingPacketTime": 0,
          "lastIncomingPacketTime": 0,
          "lastUpdated": "string",
          "macAddress": "string",
          "mappedPhysicalInterfaceId": "string",
          "mappedPhysicalInterfaceName": "string",
          "mediaType": "string",
          "mtu": "string",
          "nativeVlanId": "string",
          "ospfSupport": "string",
          "pid": "string",
          "portMode": "string",
          "portName": "string",
          "portType": "string",
          "serialNo": "string",
          "series": "string",
          "speed": "string",
          "status": "string",
          "vlanId": "string",
          "voiceVlan": "string"
        }
      ],
      "version": "string"
    }
"""
