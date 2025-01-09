#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: lan_automation_count_info
short_description: Information module for Lan Automation Count Info
description:
- This module represents an alias of the module lan_automation_count_v1_info
version_added: '6.0.0'
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
- name: Cisco DNA Center documentation for LAN Automation LANAutomationSessionCountV1
  description: Complete reference of the LANAutomationSessionCountV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!l-an-automation-session-count
notes:
  - SDK Method used are
    lan_automation.LanAutomation.lan_automation_session_count_v1,

  - Paths used are
    get /dna/intent/api/v1/lan-automation/count,
  - It should be noted that this module is an alias of lan_automation_count_v1_info

"""

EXAMPLES = r"""
- name: Get all Lan Automation Count Info
  cisco.catalystcenter.lan_automation_count_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
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
      "sessionCount": "string"
    }
"""
