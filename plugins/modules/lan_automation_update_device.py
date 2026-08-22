#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: lan_automation_update_device
short_description: Resource module for Lan Automation Update Device
description:
  - Manage operation update of the resource Lan Automation Update Device. - > Invoke this API to perform a DAY-N update on
    LAN Automation-related devices. Supported features include Loopback0 IP update, hostname update, link addition, and link
    deletion.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  feature:
    description: Feature query parameter. Feature ID for the update. Supported feature IDs include LOOPBACK0_IPADDRESS_UPDATE,
      HOSTNAME_UPDATE, LINK_ADD, and LINK_DELETE.
    type: str
  hostnameUpdateDevices:
    description: The list of Devices identified by its Management IP Address for Hostname Update.
    elements: dict
    suboptions:
      deviceManagementIPAddress:
        description: Device Management IP Address.
        type: str
      newHostName:
        description: New hostname for the device.
        type: str
    type: list
  linkUpdate:
    description: Link Update Details.
    suboptions:
      destinationDeviceInterfaceName:
        description: Destination Device Interface Name.
        type: str
      destinationDeviceManagementIPAddress:
        description: Destination Device Management IP Address.
        type: str
      ipPoolName:
        description: Name of the IP LAN Pool, required for Link Add should be from discovery site of source and destination
          device. It is optional for Link Delete.
        type: str
      ipV6Only:
        description: Flag to enable ipv6 for lan automation.
        type: bool
      sourceDeviceInterfaceName:
        description: Source Device Interface Name.
        type: str
      sourceDeviceManagementIPAddress:
        description: Source Device Management IP Address.
        type: str
      useP2PLinkLocalAddress:
        description: Flag to enable local link ip enablement for ipv6, can be true only when ipv6 flag is set to true.
        type: bool
    type: dict
  loopbackUpdateDeviceList:
    description: The list of Devices identified by its Management IP Address for Loopback0 IP Address Update.
    elements: dict
    suboptions:
      deviceManagementIPAddress:
        description: Device Management IP Address.
        type: str
      newLoopback0IPAddress:
        description: New Loopback0 IP Address from LAN Pool of Device Discovery Site(Shared pool should not be used).
        type: str
    type: list
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for LAN Automation LANAutomationDeviceUpdate
    description: Complete reference of the LANAutomationDeviceUpdate API.
    link: https://developer.cisco.com/docs/dna-center/#!l-an-automation-device-update
notes:
  - SDK Method used are
    lan_automation.LanAutomation.lan_automation_device_update,
  - Paths used are
    put /dna/intent/api/v1/lan-automation/updateDevice,
"""

EXAMPLES = r"""
---
- name: Update all
  cisco.catalystcenter.lan_automation_update_device:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    feature: string
    hostnameUpdateDevices:
      - deviceManagementIPAddress: string
        newHostName: string
    linkUpdate:
      destinationDeviceInterfaceName: string
      destinationDeviceManagementIPAddress: string
      ipPoolName: string
      ipV6Only: true
      sourceDeviceInterfaceName: string
      sourceDeviceManagementIPAddress: string
      useP2PLinkLocalAddress: true
    loopbackUpdateDeviceList:
      - deviceManagementIPAddress: string
        newLoopback0IPAddress: string
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
