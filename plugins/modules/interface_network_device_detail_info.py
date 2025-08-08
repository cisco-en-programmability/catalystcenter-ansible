#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: interface_network_device_detail_info
short_description: Information module for Interface
  Network Device Detail
description:
  - Get all Interface Network Device Detail.
  - Returns interface by specified device Id and interface
    name.
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
  name:
    description:
      - Name query parameter. Interface name.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices
      GetInterfaceDetailsByDeviceIdAndInterfaceName
    description: Complete reference of the GetInterfaceDetailsByDeviceIdAndInterfaceName
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-interface-details-by-device-id-and-interface-name
notes:
  - SDK Method used are
    devices.Devices.get_interface_details,
  - Paths used are
    get /dna/intent/api/v1/interface/network-device/{deviceId}/interface-name,
"""

EXAMPLES = r"""
---
- name: Get all Interface Network Device Detail
  cisco.catalystcenter.interface_network_device_detail_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
    name: string
    deviceId: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
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
        "voiceVlan": "string",
        "poweroverethernet": "string",
        "networkdevice_id": "string",
        "managedComputeElement": "string",
        "managedNetworkElement": "string",
        "managedNetworkElementUrl": "string",
        "managedComputeElementUrl": "string"
      },
      "version": "string"
    }
"""
