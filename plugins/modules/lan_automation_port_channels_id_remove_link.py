#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: lan_automation_port_channels_id_remove_link
short_description: Resource module for Lan Automation
  Port Channels Id Remove Link
description:
  - Manage operation create of the resource Lan Automation
    Port Channels Id Remove Link.
  - This API removes a member link from an existing
    Port Channel, reverting the link to a P2P L3 interface.
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. ID of the port channel.
    type: str
  portChannelMembers:
    description: Lan Automation Port Channels Id Remove
      Link's portChannelMembers.
    elements: dict
    suboptions:
      device1Interface:
        description: Either device1InterfaceUuid or
          device1InterfaceName is required.
        type: str
      device1InterfaceUuid:
        description: Either device1InterfaceUuid or
          device1InterfaceName is required.
        type: str
      device2Interface:
        description: Either device2InterfaceUuid or
          device1InterfaceName is required.
        type: str
      device2InterfaceUuid:
        description: Either device2InterfaceUuid or
          device1InterfaceName is required.
        type: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for LAN Automation
      RemoveALinkFromPortChannel
    description: Complete reference of the RemoveALinkFromPortChannel
      API.
    link: https://developer.cisco.com/docs/dna-center/#!remove-a-link-from-port-channel
notes:
  - SDK Method used are
    lan_automation.LanAutomation.remove_a_link_from_port_channel,
  - Paths used are
    post /dna/intent/api/v1/lanAutomation/portChannels/{id}/removeLink,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.lan_automation_port_channels_id_remove_link:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    id: string
    portChannelMembers:
      - device1Interface: string
        device1InterfaceUuid: string
        device2Interface: string
        device2InterfaceUuid: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
