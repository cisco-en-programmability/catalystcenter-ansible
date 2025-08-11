#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_interface_isis_info
short_description: Information module for Device Interface
  Isis
description:
  - Get all Device Interface Isis.
  - Returns the interfaces that has ISIS enabled.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices
      GetISISInterfaces
    description: Complete reference of the GetISISInterfaces
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-isis-interfaces
notes:
  - SDK Method used are
    devices.Devices.get_isis_interfaces,
  - Paths used are
    get /dna/intent/api/v1/interface/isis,
"""

EXAMPLES = r"""
---
- name: Get all Device Interface Isis
  cisco.catalystcenter.device_interface_isis_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
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
