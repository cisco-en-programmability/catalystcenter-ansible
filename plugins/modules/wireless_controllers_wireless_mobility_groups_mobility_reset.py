#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: wireless_controllers_wireless_mobility_groups_mobility_reset
short_description: Resource module for Wireless Controllers Wireless Mobility Groups Mobility Reset
description:
- This module represents an alias of the module wireless_controllers_wireless_mobility_groups_mobility_reset_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  networkDeviceId:
    description: Network device Id of Cisco wireless controller. Obtain the network
      device ID value by using the API call GET - /dna/intent/api/v1/network-device/ip-address/${ipAddress}.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless MobilityResetV1
  description: Complete reference of the MobilityResetV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!mobility-reset
notes:
  - SDK Method used are
    wireless.Wireless.mobility_reset_v1,

  - Paths used are
    post /dna/intent/api/v1/wirelessControllers/wirelessMobilityGroups/mobilityReset,
  - It should be noted that this module is an alias of wireless_controllers_wireless_mobility_groups_mobility_reset_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.wireless_controllers_wireless_mobility_groups_mobility_reset:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    networkDeviceId: string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
