#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_portAssignments_info
short_description: Information module for Sda Portassignments
description:
- Get all Sda Portassignments.
- Returns a list of port assignments that match the provided query parameters.
version_added: '6.14.0'
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
    - NetworkDeviceId query parameter. Network device ID of the port assignment.
    type: str
  interfaceName:
    description:
    - InterfaceName query parameter. Interface name of the port assignment.
    type: str
  dataVlanName:
    description:
    - DataVlanName query parameter. Data VLAN name of the port assignment.
    type: str
  voiceVlanName:
    description:
    - VoiceVlanName query parameter. Voice VLAN name of the port assignment.
    type: str
  offset:
    description:
    - Offset query parameter. Starting record for pagination.
    type: float
  limit:
    description:
    - Limit query parameter. Maximum number of records to return.
    type: float
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for SDA GetPortAssignmentsV1
  description: Complete reference of the GetPortAssignmentsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-port-assignments-v-1
notes:
  - SDK Method used are
    sda.Sda.get_port_assignments_v1,

  - Paths used are
    get /dna/intent/api/v1/sda/portAssignments,

"""

EXAMPLES = r"""
- name: Get all Sda Portassignments
  cisco.catalystcenter.sda_portAssignments_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    fabricId: string
    networkDeviceId: string
    interfaceName: string
    dataVlanName: string
    voiceVlanName: string
    offset: 0
    limit: 0
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
          "id": "string",
          "fabricId": "string",
          "networkDeviceId": "string",
          "interfaceName": "string",
          "connectedDeviceType": "string",
          "dataVlanName": "string",
          "voiceVlanName": "string",
          "authenticateTemplateName": "string",
          "securityGroupName": "string",
          "interfaceDescription": "string"
        }
      ],
      "version": "string"
    }
"""
