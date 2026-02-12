#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_port_assignment_for_access_point
short_description: Resource module for Sda Port Assignment For Access Point
description:
  - Manage operations create and delete of the resource Sda Port Assignment For Access Point.
  - Add Port assignment for access point in SDA Fabric.
  - Delete Port assignment for access point in SDA Fabric.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  authenticateTemplateName:
    description: Authenticate TemplateName associated to Fabric Site.
    type: str
    version_added: 4.0.0
  dataIpAddressPoolName:
    description: Ip Pool Name, that is assigned to INFRA_VN.
    type: str
    version_added: 4.0.0
  deviceManagementIpAddress:
    description: DeviceManagementIpAddress query parameter.
    type: str
    version_added: 4.0.0
  interfaceDescription:
    description: Details or note of interface port assignment.
    type: str
    version_added: 4.0.0
  interfaceName:
    description: InterfaceName query parameter.
    type: str
  siteNameHierarchy:
    description: Path of sda Fabric Site.
    type: str
    version_added: 4.0.0
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for SDA AddPortAssignmentForAccessPointInSDAFabric
    description: Complete reference of the AddPortAssignmentForAccessPointInSDAFabric API.
    link: https://developer.cisco.com/docs/dna-center/#!add-port-assignment-for-access-point-in-sda-fabric
  - name: Cisco DNA Center documentation for SDA DeletePortAssignmentForAccessPointInSDAFabric
    description: Complete reference of the DeletePortAssignmentForAccessPointInSDAFabric API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-port-assignment-for-access-point-in-sda-fabric
notes:
  - SDK Method used are
    sda.Sda.add_port_assignment_for_access_point,
    sda.Sda.delete_port_assignment_for_access_point,
  - Paths used are
    post /dna/intent/api/v1/business/sda/hostonboarding/access-point,
    delete /dna/intent/api/v1/business/sda/hostonboarding/access-point,
"""

EXAMPLES = r"""
---
- name: Delete all
  cisco.catalystcenter.sda_port_assignment_for_access_point:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    deviceManagementIpAddress: string
    interfaceName: string
- name: Create
  cisco.catalystcenter.sda_port_assignment_for_access_point:
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
    siteNameHierarchy: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
