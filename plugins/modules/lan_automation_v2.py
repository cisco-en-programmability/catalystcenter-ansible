#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: lan_automation_v2
short_description: Resource module for Lan Automation V2
description:
  - Manage operation create of the resource Lan Automation V2. - > Invoke V2 LAN Automation Start API, which supports optional
    auto-stop processing feature based on the provided timeout or a specific device list, or both. The stop processing will
    be executed automatically when either of the cases is satisfied, without specifically calling the stop API. The V2 API
    behaves similarly to V1 if no timeout or device list is provided, and the user needs to call the stop API for LAN Automation
    stop processing. With the V2 API, the user can also specify the level up to which the devices can be LAN automated.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  payload:
    description: Lan Automation V2's payload.
    elements: dict
    suboptions:
      advertiseLANAutomationRoutesIntoBGP:
        description: Advertise LAN Automation summary route into BGP.
        type: bool
      areaId:
        description: OSPF area Id to be used for underlay devices. Default value if not provided is 0.
        type: int
      authenticationKey:
        description: Authentication key string to be used in key chain configuration on interface level.
        type: str
      discoveredDeviceSiteNameHierarchy:
        description: Discovered device site name.
        type: str
      discoveryDevices:
        description: Specific devices that will be LAN Automated in this session. Any other device discovered via DHCP will
          be attempted for a reset and reload to bring it back to the PnP agent state at the end of the LAN Automation process
          before process completion. The maximum supported devices that can be provided for a session is 50. If only the discovery
          devices list is provided and no timeout is provided, then the LAN Automation stop processing will get triggered
          when all devices from the list are discovered and added to inventory. If both the discovery devices list and timeout
          are provided, the stop processing will be attempted whichever happens earlier. Users can always use the LAN Automation
          Stop API to force stop processing.
        elements: dict
        suboptions:
          deviceHostName:
            description: Hostname of the device.
            type: str
          deviceManagementIPAddress:
            description: Management IP Address of the device.
            type: str
          deviceSerialNumber:
            description: Serial number of the device.
            type: str
          deviceSiteNameHierarchy:
            description: "Site name hierarchy for the device, must be a child site of the discoveredDeviceSiteNameHierarchy
              or same if it's not area type."
            type: str
        type: list
      discoveryLevel:
        description: Level below primary seed device upto which the new devices will be LAN Automated by this session, level
          + seed = tier. Supported range for level is 1-5, default level is 2.
        type: int
      discoveryTimeout:
        description: Discovery timeout in minutes. Until this time, the stop processing will not be triggered. Any device
          contacting after the provided discovery timeout will not be processed, and a device reset and reload will be attempted
          to bring it back to the PnP agent state before process completion. The supported timeout range is in minutes 20-10080.
          If both timeout and discovery devices list are provided, the stop processing will be attempted whichever happens
          earlier. Users can always use the LAN Automation delete API to force stop processing.
        type: int
      hostNameFileId:
        description: Use /dna/intent/api/v1/file/namespace/nw_orch API to get the file ID for the already uploaded file in
          the nw_orch namespace.
        type: str
      hostNamePrefix:
        description: Host name prefix assigned to the discovered device.
        type: str
      ipPools:
        description: The list of IP pools with their names and roles.
        elements: dict
        suboptions:
          ipPoolName:
            description: Name of the IP pool.
            type: str
          ipPoolRole:
            description: Role of the IP pool. Supported roles are MAIN_POOL and PHYSICAL_LINK_POOL.
            type: str
        type: list
      ipV6Only:
        description: Flag to enable ipv6 for lan automation.
        type: bool
      isisDomainPwd:
        description: IS-IS domain password in plain text.
        type: str
      multicastEnabled:
        description: Enable underlay native multicast.
        type: bool
      peerDeviceManagmentIPAddress:
        description: Peer seed management IP address.
        type: str
      primaryDeviceInterfaceNames:
        description: The list of interfaces on primary seed via which the discovered devices are connected.
        elements: str
        type: list
      primaryDeviceManagmentIPAddress:
        description: Primary seed management IP address.
        type: str
      processId:
        description: OSPF process Id to be used for underlay devices. Default value if not provided is 1.
        type: int
      redistributeIsisToBgp:
        description: Advertise LAN Automation summary route into BGP.
        type: bool
      routingProtocol:
        description: Underlay routing protocol to be used OSPF or ISIS. ISIS being default if not provided.
        type: dict
      useP2PLinkLocalAddress:
        description: Flag to enable local link ip enablement for ipv6, can be true only when ipv6 flag is set to true.
        type: bool
    type: list
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for LAN Automation LANAutomationStart
    description: Complete reference of the LANAutomationStart API.
    link: https://developer.cisco.com/docs/dna-center/#!l-an-automation-start
notes:
  - SDK Method used are
    lan_automation.LanAutomation.lan_automation_start,
  - Paths used are
    post /dna/intent/api/v2/lan-automation,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.lan_automation_v2:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    payload:
      - advertiseLANAutomationRoutesIntoBGP: true
        areaId: 0
        authenticationKey: string
        discoveredDeviceSiteNameHierarchy: string
        discoveryDevices:
          - deviceHostName: string
            deviceManagementIPAddress: string
            deviceSerialNumber: string
            deviceSiteNameHierarchy: string
        discoveryLevel: 0
        discoveryTimeout: 0
        hostNameFileId: string
        hostNamePrefix: string
        ipPools:
          - ipPoolName: string
            ipPoolRole: string
        ipV6Only: true
        isisDomainPwd: string
        multicastEnabled: true
        peerDeviceManagmentIPAddress: string
        primaryDeviceInterfaceNames:
          - string
        primaryDeviceManagmentIPAddress: string
        processId: 0
        redistributeIsisToBgp: true
        routingProtocol: {}
        useP2PLinkLocalAddress: true
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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
