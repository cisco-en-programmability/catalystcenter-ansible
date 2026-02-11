#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: lan_automation_port_channels
short_description: Resource module for Lan Automation Port Channels
description:
  - Manage operations create and delete of the resource Lan Automation Port Channels. - > This API creates a Port Channel
    between two LAN Automation associated devices using the PAgP protocol, with a minimum of 2 and a maximum of 8 LAN Automated
    interfaces in UP status.
  - This API deletes a Port Channel between LAN Automation associated devices using a valid Port Channel ID.
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  device1ManagementIPAddress:
    description: Either device1ManagementIPAddress or device1Uuid is required.
    type: str
  device1Uuid:
    description: Either device1ManagementIPAddress or device1Uuid is required.
    type: str
  device2ManagementIPAddress:
    description: Either device2ManagementIPAddress or device2Uuid is required.
    type: str
  device2Uuid:
    description: Either device2ManagementIPAddress or device2Uuid is required.
    type: str
  id:
    description: Id path parameter. ID of the port channel.
    type: str
  portChannelMembers:
    description: Lan Automation Port Channels's portChannelMembers.
    elements: dict
    suboptions:
      device1Interface:
        description: Either device1InterfaceUuid or device1InterfaceName is required.
        type: str
      device1InterfaceUuid:
        description: Either device1InterfaceUuid or device1InterfaceName is required.
        type: str
      device2Interface:
        description: Either device2InterfaceUuid or device2InterfaceName is required.
        type: str
      device2InterfaceUuid:
        description: Either device2InterfaceUuid or device2InterfaceName is required.
        type: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for LAN Automation CreateANewPortChannelBetweenDevices
    description: Complete reference of the CreateANewPortChannelBetweenDevices API.
    link: https://developer.cisco.com/docs/dna-center/#!create-a-new-port-channel-between-devices
  - name: Cisco DNA Center documentation for LAN Automation DeletePortChannel
    description: Complete reference of the DeletePortChannel API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-port-channel
notes:
  - SDK Method used are
    lan_automation.LanAutomation.create_a_new_port_channel_between_devices,
    lan_automation.LanAutomation.delete_port_channel,
  - Paths used are
    post /dna/intent/api/v1/lanAutomation/portChannels,
    delete /dna/intent/api/v1/lanAutomation/portChannels/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.lan_automation_port_channels:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    device1ManagementIPAddress: string
    device1Uuid: string
    device2ManagementIPAddress: string
    device2Uuid: string
    portChannelMembers:
      - device1Interface: string
        device1InterfaceUuid: string
        device2Interface: string
        device2InterfaceUuid: string
- name: Delete by id
  cisco.catalystcenter.lan_automation_port_channels:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: string
"""
RETURN = r"""
dnac_response:
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
