#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_port_assignments_info
short_description: Information module for Sda Port Assignments
description:
  - Get all Sda Port Assignments.
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
  nativeVlanId:
    description:
      - >
        NativeVlanId query parameter. Native VLAN of the port assignment, this option is only applicable to
        TRUNKING_DEVICE connectedDeviceType.(VLAN must be between 1 and 4094. In cases value not set when
        connectedDeviceType is TRUNKING_DEVICE, default value will be '1').
    type: float
  offset:
    description:
      - Offset query parameter. Starting record for pagination.
    type: int
  limit:
    description:
      - >
        Limit query parameter. Maximum number of records to return. The maximum number of objects supported in a
        single request is 500.
    type: int
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for SDA GetPortAssignments
    description: Complete reference of the GetPortAssignments API.
    link: https://developer.cisco.com/docs/dna-center/#!get-port-assignments
notes:
  - SDK Method used are
    sda.Sda.get_port_assignments,
  - Paths used are
    get /dna/intent/api/v1/sda/portAssignments,
"""

EXAMPLES = r"""
---
- name: Get all Sda Port Assignments
  cisco.catalystcenter.sda_port_assignments_info:
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
    nativeVlanId: 0
    offset: 0
    limit: 0
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "siteId": "string",
          "networkDeviceId": "string"
        }
      ],
      "version": "string"
    }
"""
