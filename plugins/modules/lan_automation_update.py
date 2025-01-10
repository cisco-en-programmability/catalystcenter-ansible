#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: lan_automation_update
short_description: Resource module for Lan Automation Update
description:
- This module represents an alias of the module lan_automation_update_v1
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. LAN Automation id can be obtained from /dna/intent/api/v1/lan-automation/status.
    type: str
  payload:
    description: Lan Automation Update's payload.
    elements: dict
    suboptions:
      deviceManagementIPAddress:
        description: Device Management IP Address.
        type: str
      newLoopback0IPAddress:
        description: New Loopback0 IP Address from LAN pool of Device Discovery Site.
        type: str
    type: list
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for LAN Automation LANAutomationStopAndUpdateDevicesV1
  description: Complete reference of the LANAutomationStopAndUpdateDevicesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!l-an-automation-stop-and-update-devices
notes:
  - SDK Method used are
    lan_automation.LanAutomation.lan_automation_stop_and_update_devices_v1,

  - Paths used are
    put /dna/intent/api/v1/lan-automation/{id},
  - It should be noted that this module is an alias of lan_automation_update_v1

"""

EXAMPLES = r"""
- name: Update by id
  cisco.catalystcenter.lan_automation_update:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    id: string
    payload:
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
