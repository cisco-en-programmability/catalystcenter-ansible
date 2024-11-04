#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wirelessAccessPoints_factoryResetRequest_provision
short_description: Resource module for Wirelessaccesspoints Factoryresetrequest Provision
description:
- Manage operation create of the resource Wirelessaccesspoints Factoryresetrequest Provision.
- >
   This API is used to factory reset Access Points. It is supported for maximum 100 Access Points per request.
   Factory reset clears all configurations from the Access Points. After factory reset the Access Point may become
   unreachable from the currently associated Wireless Controller and may or may not join back the same controller.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  apMacAddresses:
    description: List of Access Point's Ethernet MAC addresses, set maximum 100 ethernet
      MAC addresses per request.
    elements: str
    type: list
  keepStaticIPConfig:
    description: Set the value of keepStaticIPConfig to false, to clear all configurations
      from Access Points and set the value of keepStaticIPConfig to true, to clear all
      configurations from Access Points without clearing static IP configuration.
    type: bool
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Wireless FactoryResetAccessPointsV1
  description: Complete reference of the FactoryResetAccessPointsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!factory-reset-access-points-v-1
notes:
  - SDK Method used are
    wireless.Wireless.factory_reset_access_points_v1,

  - Paths used are
    post /dna/intent/api/v1/wirelessAccessPoints/factoryResetRequest/provision,

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.wirelessAccessPoints_factoryResetRequest_provision:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    apMacAddresses:
    - string
    keepStaticIPConfig: true

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
