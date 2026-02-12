#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: interface_operation_create
short_description: Resource module for Interface Operation Create
description:
  - Manage operation create of the resource Interface Operation Create. - > Clear mac-address on an individual port. In request
    body, operation needs to be specified as 'ClearMacAddress'. In the future more possible operations will be added to this
    API.
version_added: '6.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  deploymentMode:
    description: DeploymentMode query parameter. Preview/Deploy 'Preview' means the configuration is not pushed to the device.
      'Deploy' makes the configuration pushed to the device.
    type: str
  interfaceUuid:
    description: InterfaceUuid path parameter. Interface Id.
    type: str
  operation:
    description: Operation needs to be specified as 'ClearMacAddress'.
    type: str
  payload:
    description: Interface Operation Create's payload.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Devices ClearMacAddressTable
    description: Complete reference of the ClearMacAddressTable API.
    link: https://developer.cisco.com/docs/dna-center/#!clear-mac-address-table
notes:
  - SDK Method used are
    devices.Devices.clear_mac_address_table,
  - Paths used are
    post /dna/intent/api/v1/interface/{interfaceUuid}/operation,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.interface_operation_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    deploymentMode: string
    interfaceUuid: string
    operation: string
    payload: {}
"""
RETURN = r"""
dnac_response:
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
