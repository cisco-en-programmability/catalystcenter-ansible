#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_port_assignment_for_user_device_v1_info
short_description: Information module for Sda Port Assignment For User Device V1
description:
- Get all Sda Port Assignment For User Device V1.
- Get Port assignment for user device in SDA Fabric.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deviceManagementIpAddress:
    description:
    - DeviceManagementIpAddress query parameter.
    type: str
  interfaceName:
    description:
    - InterfaceName query parameter.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for SDA GetPortAssignmentForUserDeviceInSDAFabricV1
  description: Complete reference of the GetPortAssignmentForUserDeviceInSDAFabricV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-port-assignment-for-user-device-in-sda-fabric
notes:
  - SDK Method used are
    sda.Sda.get_port_assignment_for_user_device,

  - Paths used are
    get /dna/intent/api/v1/business/sda/hostonboarding/user-device,

"""

EXAMPLES = r"""
- name: Get all Sda Port Assignment For User Device V1
  cisco.catalystcenter.sda_port_assignment_for_user_device_v1_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    deviceManagementIpAddress: string
    interfaceName: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "status": "string",
      "description": "string",
      "siteNameHierarchy": "string",
      "deviceManagementIpAddress": "string",
      "interfaceName": "string",
      "dataIpAddressPoolName": "string",
      "voiceIpAddressPoolName": "string",
      "scalableGroupName": "string",
      "authenticateTemplateName": "string"
    }
"""
