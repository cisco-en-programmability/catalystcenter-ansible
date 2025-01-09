#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sda_port_channels_info
short_description: Information module for Sda Port Channels Info
description:
- This module represents an alias of the module sda_port_channels_v1_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  fabricId:
    description:
    - FabricId query parameter. ID of the fabric the device is assigned to.
    type: str
  networkDeviceId:
    description:
    - NetworkDeviceId query parameter. ID of the network device.
    type: str
  portChannelName:
    description:
    - PortChannelName query parameter. Name of the port channel.
    type: str
  connectedDeviceType:
    description:
    - >
      ConnectedDeviceType query parameter. Connected device type of the port channel. The allowed values are
      TRUNK, EXTENDED_NODE.
    type: str
  offset:
    description:
    - Offset query parameter. Starting record for pagination.
    type: float
  limit:
    description:
    - >
      Limit query parameter. Maximum number of records to return. The maximum number of objects supported in a
      single request is 500.
    type: float
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for SDA GetPortChannelsV1
  description: Complete reference of the GetPortChannelsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-port-channels
notes:
  - SDK Method used are
    sda.Sda.get_port_channels_v1,

  - Paths used are
    get /dna/intent/api/v1/sda/portChannels,
  - It should be noted that this module is an alias of sda_port_channels_v1_info

"""

EXAMPLES = r"""
- name: Get all Sda Port Channels Info
  cisco.catalystcenter.sda_port_channels_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    fabricId: string
    networkDeviceId: string
    portChannelName: string
    connectedDeviceType: string
    offset: 0
    limit: 0
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
          "id": "string",
          "fabricId": "string",
          "networkDeviceId": "string",
          "portChannelName": "string",
          "interfaceNames": [
            "string"
          ],
          "connectedDeviceType": "string",
          "protocol": "string",
          "description": "string"
        }
      ],
      "version": "string"
    }
"""
