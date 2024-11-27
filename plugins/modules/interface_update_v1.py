#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: interface_update_v1
short_description: Resource module for Interface Update V1
description:
- Manage operation update of the resource Interface Update V1.
- >
   Add/Update Interface description, VLAN membership, Voice VLAN and change Interface admin status 'UP'/'DOWN' from
   Request body.
version_added: '6.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  adminStatus:
    description: Admin status as ('UP'/'DOWN').
    type: str
  deploymentMode:
    description: DeploymentMode query parameter. Preview/Deploy 'Preview' means the
      configuration is not pushed to the device. 'Deploy' makes the configuration pushed
      to the device.
    type: str
  description:
    description: Description for the Interface.
    type: str
  interfaceUuid:
    description: InterfaceUuid path parameter. Interface ID.
    type: str
  vlanId:
    description: VLAN Id to be Updated.
    type: int
  voiceVlanId:
    description: Voice Vlan Id to be Updated.
    type: int
requirements:
- catalystcentersdk >= 2.3.7.6
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices UpdateInterfaceDetailsV1
  description: Complete reference of the UpdateInterfaceDetailsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!update-interface-details
notes:
  - SDK Method used are
    devices.Devices.update_interface_details_v1,

  - Paths used are
    put /dna/intent/api/v1/interface/{interfaceUuid},

"""

EXAMPLES = r"""
- name: Update by id
  cisco.catalystcenter.interface_update_v1:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    adminStatus: string
    deploymentMode: string
    description: string
    interfaceUuid: string
    vlanId: 0
    voiceVlanId: 0

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "type": "string",
        "properties": {
          "taskId": {
            "type": "string"
          },
          "url": {
            "type": "string"
          }
        },
        "required": [
          "string"
        ]
      },
      "version": {
        "type": "string"
      }
    }
"""
