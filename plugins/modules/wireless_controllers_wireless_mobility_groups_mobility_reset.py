#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wirelessControllers_wirelessMobilityGroups_mobilityReset
short_description: Resource module for Wirelesscontrollers Wirelessmobilitygroups Mobilityreset
description:
- Manage operation create of the resource Wirelesscontrollers Wirelessmobilitygroups Mobilityreset.
- This API is used to reset wireless mobility which in turn sets mobility group name as 'default'.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  networkDeviceId:
    description: Network device Id of Cisco wireless controller.Obtain the network device
      ID value by using the API call GET - /dna/intent/api/v1/network-device/ip-address/${ipAddress}.
    type: str
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Wireless MobilityResetV1
  description: Complete reference of the MobilityResetV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!mobility-reset-v-1
notes:
  - SDK Method used are
    wireless.Wireless.mobility_reset_v1,

  - Paths used are
    post /dna/intent/api/v1/wirelessControllers/wirelessMobilityGroups/mobilityReset,

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.wirelessControllers_wirelessMobilityGroups_mobilityReset:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    networkDeviceId: string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
