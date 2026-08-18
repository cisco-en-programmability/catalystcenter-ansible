#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_fabric_border_device
short_description: Resource module for Sda Fabric Border Device
description:
  - Manage operations create and delete of the resource Sda Fabric Border Device.
  - Add border device in SDA Fabric.
  - Delete border device from SDA Fabric.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  deviceManagementIpAddress:
    description: DeviceManagementIpAddress query parameter.
    type: str
  payload:
    description: Add Border Device API (Highlights Supports multi device role,L3 Handoff and L2 Handoff ).
    elements: dict
    suboptions:
      borderPriority:
        description: Border priority associated with a given device. Allowed range for Border Priority is 1-9. A lower value
          indicates higher priority. E.g., a priority of 1 takes precedence over 5. Default priority would be set to 10.
        type: str
      borderSessionType:
        description: Border Session Type.
        type: str
      borderWithExternalConnectivity:
        description: Border With External Connectivity (Note True for transit and False for non-transit border).
        type: bool
      connectedToInternet:
        description: Connected to Internet.
        type: bool
      deviceManagementIpAddress:
        description: Management Ip Address of the provisioned Device.
        type: str
      deviceRole:
        description: Supported Device Roles in SD-Access fabric. Allowed roles are "Border_Node","Control_Plane_Nod... E.g.
          "Border_Node" or "Border_Node", "Control_Plane_Node" or "Border_Node", "Control_Plane_Node","Edge_Node".
        elements: str
        type: list
      externalConnectivityIpPoolName:
        description: External Connectivity IpPool Name.
        type: str
      externalConnectivitySettings:
        description: External Connectivity Settings information of L3 and L2 Handoff.
        elements: dict
        suboptions:
          externalAutonomouSystemNumber:
            description: External Autonomous System Number peer (e.g.,1-65535).
            type: str
          interfaceDescription:
            description: Interface Description.
            type: str
          interfaceName:
            description: Interface Name.
            type: str
          l2Handoff:
            description: L2 Handoff information.
            elements: dict
            suboptions:
              virtualNetworkName:
                description: Virtual Network Name, that is associated to Fabric Site.
                type: str
              vlanName:
                description: Vlan Name of L2 Handoff.
                type: str
            type: list
          l3Handoff:
            description: L3 Handoff information.
            elements: dict
            suboptions:
              virtualNetwork:
                description: Virtual Network information of L3 Hand off.
                suboptions:
                  virtualNetworkName:
                    description: Virtual Network Name, that is associated to Fabric Site.
                    type: str
                  vlanId:
                    description: Vlan Id (e.g.,2-4096 except for reserved VLANs (1002-1005, 2046, 4095)).
                    type: str
                type: dict
            type: list
        type: list
      externalDomainRoutingProtocolName:
        description: External Domain Routing Protocol Name.
        type: str
      internalAutonomouSystemNumber:
        description: Internal Autonomous System Number.
        type: str
      routeDistributionProtocol:
        description: Route Distribution Protocol for Control Plane Device. Allowed values are "LISP_BGP" or "LISP_PUB_SUB".
          Default value is "LISP_BGP".
        type: str
      sdaTransitNetworkName:
        description: SD-Access Transit Network Name.
        type: str
      siteNameHierarchy:
        description: Site Name Hierarchy of provisioned Device(site should be part of Fabric Site).
        type: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for SDA AddBorderDeviceInSDAFabric
    description: Complete reference of the AddBorderDeviceInSDAFabric API.
    link: https://developer.cisco.com/docs/dna-center/#!add-border-device-in-sda-fabric
  - name: Cisco Catalyst Center documentation for SDA DeleteBorderDeviceFromSDAFabric
    description: Complete reference of the DeleteBorderDeviceFromSDAFabric API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-border-device-from-sda-fabric
notes:
  - SDK Method used are
    sda.Sda.adds_border_device,
    sda.Sda.deletes_border_device,
  - Paths used are
    post /dna/intent/api/v1/business/sda/border-device,
    delete /dna/intent/api/v1/business/sda/border-device,
"""

EXAMPLES = r"""
---
- name: Delete all
  cisco.catalystcenter.sda_fabric_border_device:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    deviceManagementIpAddress: application/json
- name: Create
  cisco.catalystcenter.sda_fabric_border_device:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    payload:
      - borderPriority: string
        borderSessionType: string
        borderWithExternalConnectivity: true
        connectedToInternet: true
        deviceManagementIpAddress: string
        deviceRole:
          - string
        externalConnectivityIpPoolName: string
        externalConnectivitySettings:
          - externalAutonomouSystemNumber: string
            interfaceDescription: string
            interfaceName: string
            l2Handoff:
              - virtualNetworkName: string
                vlanName: string
            l3Handoff:
              - virtualNetwork:
                  virtualNetworkName: string
                  vlanId: string
        externalDomainRoutingProtocolName: string
        internalAutonomouSystemNumber: string
        routeDistributionProtocol: string
        sdaTransitNetworkName: string
        siteNameHierarchy: string
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
