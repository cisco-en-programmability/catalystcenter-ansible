#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: lan_automation_update_device_v1
short_description: Resource module for Lan Automation Update Device V1
description:
- Manage operation update of the resource Lan Automation Update Device V1.
- >
   Invoke this API to perform a DAY-N update on LAN Automation-related devices. Supported features include Loopback0
   IP update, hostname update, link addition, and link deletion.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  feature:
    description: Feature query parameter. Feature ID for the update. Supported feature
      IDs include LOOPBACK0_IPADDRESS_UPDATE, HOSTNAME_UPDATE, LINK_ADD, and LINK_DELETE.
    type: str
  hostnameUpdateDevices:
    description: Lan Automation Update Device's hostnameUpdateDevices.
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
    description: Lan Automation Update Device's linkUpdate.
    suboptions:
      destinationDeviceInterfaceName:
        description: Destination Device Interface Name.
        type: str
      destinationDeviceManagementIPAddress:
        description: Destination Device Management IP Address.
        type: str
      ipPoolName:
        description: Name of the IP LAN Pool, required for Link Add should be from discovery
          site of source and destination device.
        type: str
      sourceDeviceInterfaceName:
        description: Source Device Interface Name.
        type: str
      sourceDeviceManagementIPAddress:
        description: Source Device Management IP Address.
        type: str
    type: dict
  loopbackUpdateDeviceList:
    description: Lan Automation Update Device's loopbackUpdateDeviceList.
    elements: dict
    suboptions:
      deviceManagementIPAddress:
        description: Device Management IP Address.
        type: str
      newLoopback0IPAddress:
        description: New Loopback0 IP Address from LAN Pool of Device Discovery Site(Shared
          pool should not be used).
        type: str
    type: list
requirements:
- catalystcentersdk >= 2.3.7.6
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for LAN Automation LANAutomationDeviceUpdateV1
  description: Complete reference of the LANAutomationDeviceUpdateV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!l-an-automation-device-update
notes:
  - SDK Method used are
    lan_automation.LanAutomation.lan_automation_device_update_v1,

  - Paths used are
    put /dna/intent/api/v1/lan-automation/updateDevice,

"""

EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.lan_automation_update_device_v1:
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
      sourceDeviceInterfaceName: string
      sourceDeviceManagementIPAddress: string
    loopbackUpdateDeviceList:
    - deviceManagementIPAddress: string
      newLoopback0IPAddress: string

"""
RETURN = r"""
catalystcenter_response:
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
