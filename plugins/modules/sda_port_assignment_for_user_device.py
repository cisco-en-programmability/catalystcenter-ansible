#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_port_assignment_for_user_device
short_description: Resource module for Sda Port Assignment For User Device
description:
  - Manage operations create and delete of the resource Sda Port Assignment For User Device.
  - Add Port assignment for user device in SDA Fabric.
  - Delete Port assignment for user device in SDA Fabric.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  authenticateTemplateName:
    description: Authenticate TemplateName associated with siteNameHierarchy.
    type: str
  dataIpAddressPoolName:
    description: Ip Pool Name, that is assigned to virtual network with traffic type as DATA(can't be empty if voiceIpAddressPoolName
      is empty).
    type: str
  deviceManagementIpAddress:
    description: Management Ip Address of the Edge Node Device.
    type: str
  interfaceDescription:
    description: User defined text message for port assignment.
    type: str
  interfaceName:
    description: Interface Name on the Edge Node Device.
    type: str
  interfaceNames:
    description: List of Interface Names on the Edge Node Device. E.g."GigabitEthernet1/0/3","GigabitEthernet1/0/4".
    elements: str
    type: list
  scalableGroupName:
    description: Scalable Group name associated with VN.
    type: str
  siteNameHierarchy:
    description: Complete Path of SD-Access Fabric Site.
    type: str
  voiceIpAddressPoolName:
    description: Ip Pool Name, that is assigned to virtual network with traffic type as VOICE(can't be empty if dataIpAddressPoolName
      is empty).
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for SDA AddPortAssignmentForUserDeviceInSDAFabric
    description: Complete reference of the AddPortAssignmentForUserDeviceInSDAFabric API.
    link: https://developer.cisco.com/docs/dna-center/#!add-port-assignment-for-user-device-in-sda-fabric
  - name: Cisco Catalyst Center documentation for SDA DeletePortAssignmentForUserDeviceInSDAFabric
    description: Complete reference of the DeletePortAssignmentForUserDeviceInSDAFabric API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-port-assignment-for-user-device-in-sda-fabric
notes:
  - SDK Method used are
    sda.Sda.add_port_assignment_for_user_device,
    sda.Sda.delete_port_assignment_for_user_device,
  - Paths used are
    post /dna/intent/api/v1/business/sda/hostonboarding/user-device,
    delete /dna/intent/api/v1/business/sda/hostonboarding/user-device,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.sda_port_assignment_for_user_device:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    authenticateTemplateName: string
    dataIpAddressPoolName: string
    deviceManagementIpAddress: string
    interfaceDescription: string
    interfaceName: string
    interfaceNames:
      - string
    scalableGroupName: string
    siteNameHierarchy: string
    voiceIpAddressPoolName: string
- name: Delete all
  cisco.catalystcenter.sda_port_assignment_for_user_device:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    deviceManagementIpAddress: application/json
    interfaceName: application/json
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "status": "string",
      "description": "string",
      "taskId": "string",
      "taskStatusUrl": "string",
      "executionStatusUrl": "string",
      "executionId": "string"
    }
"""
