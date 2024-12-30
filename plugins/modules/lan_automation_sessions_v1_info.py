#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: lan_automation_sessions_v1_info
short_description: Information module for Lan Automation Sessions V1
description:
- Get all Lan Automation Sessions V1.
- Invoke this API to get the LAN Automation active session information.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for LAN Automation LANAutomationActiveSessionsV1
  description: Complete reference of the LANAutomationActiveSessionsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!l-an-automation-active-sessions
notes:
  - SDK Method used are
    lan_automation.LanAutomation.lan_automation_active_sessions_v1,

  - Paths used are
    get /dna/intent/api/v1/lan-automation/sessions,

"""

EXAMPLES = r"""
- name: Get all Lan Automation Sessions V1
  cisco.catalystcenter.lan_automation_sessions_v1_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "maxSupportedCount": "string",
        "activeSessions": "string",
        "activeSessionIds": [
          "string"
        ]
      },
      "version": "string"
    }
"""
