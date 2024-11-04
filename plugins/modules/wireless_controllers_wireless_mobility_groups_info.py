#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wirelessControllers_wirelessMobilityGroups_info
short_description: Information module for Wirelesscontrollers Wirelessmobilitygroups
description:
- Get all Wirelesscontrollers Wirelessmobilitygroups.
- >
   Retrieve all configured mobility groups if no Network Device Id is provided as a query parameter. If a Network
   Device Id is given and a mobility group is configured for it, return the configured details; otherwise, return the
   default values from the device.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  networkDeviceId:
    description:
    - >
      NetworkDeviceId query parameter. Employ this query parameter to obtain the details of the Mobility Group
      corresponding to the provided networkDeviceId. Obtain the network device ID value by using the API GET call
      /dna/intent/api/v1/network-device/ip-address/${ipAddress}.
    type: str
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Wireless GetAllMobilityGroupsV1
  description: Complete reference of the GetAllMobilityGroupsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-all-mobility-groups-v-1
notes:
  - SDK Method used are
    wireless.Wireless.get_all_mobility_groups_v1,

  - Paths used are
    get /dna/intent/api/v1/wirelessControllers/wirelessMobilityGroups,

"""

EXAMPLES = r"""
- name: Get all Wirelesscontrollers Wirelessmobilitygroups
  cisco.catalystcenter.wirelessControllers_wirelessMobilityGroups_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    networkDeviceId: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "mobilityGroupName": "string",
          "macAddress": "string",
          "managementIp": "string",
          "networkDeviceId": "string",
          "dtlsHighCipher": true,
          "dataLinkEncryption": true,
          "mobilityPeers": [
            {
              "mobilityGroupName": "string",
              "peerNetworkDeviceId": "string",
              "memberMacAddress": "string",
              "deviceSeries": "string",
              "dataLinkEncryption": true,
              "hashKey": "string",
              "status": "string",
              "peerIp": "string",
              "privateIpAddress": "string"
            }
          ]
        }
      ],
      "version": "string"
    }
"""
