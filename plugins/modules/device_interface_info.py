#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: device_interface_info
short_description: Information module for Device Interface Info
description:
  - This module represents an alias of the module device_interface_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  offset:
    description:
      - Offset query parameter.
    type: int
  limit:
    description:
      - Limit query parameter. The number of records to show for this page. Min 1,
        Max 500.
    type: int
  lastInputTime:
    description:
      - LastInputTime query parameter. Last Input Time.
    type: str
  lastOutputTime:
    description:
      - LastOutputTime query parameter. Last Output Time.
    type: str
  id:
    description:
      - Id path parameter. Interface ID.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices GetAllInterfacesV1
    description: Complete reference of the GetAllInterfacesV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-all-interfaces
  - name: Cisco DNA Center documentation for Devices GetInterfaceByIdV1
    description: Complete reference of the GetInterfaceByIdV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-interface-by-id
notes:
  - SDK Method used are devices.Devices.get_all_interfaces_v1, devices.Devices.get_interface_by_id_v1,
  - Paths used are get /dna/intent/api/v1/interface, get /dna/intent/api/v1/interface/{id},
  - It should be noted that this module is an alias of device_interface_v1_info
"""
EXAMPLES = r"""
- name: Get all Device Interface Info
  cisco.catalystcenter.device_interface_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    offset: 0
    limit: 0
    lastInputTime: string
    lastOutputTime: string
  register: result
- name: Get Device Interface Info by id
  cisco.catalystcenter.device_interface_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    id: string
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
      },
      "version": "string"
    }
"""
