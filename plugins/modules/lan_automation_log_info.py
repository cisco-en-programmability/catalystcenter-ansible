#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: lan_automation_log_info
short_description: Information module for Lan Automation Log Info
description:
- This module represents an alias of the module lan_automation_log_v1_info
version_added: '6.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  offset:
    description:
    - Offset query parameter. Starting index of the LAN Automation session. Minimum value is 1.
    type: float
  limit:
    description:
    - Limit query parameter. Number of LAN Automation sessions to be retrieved. Limit value can range between 1 to 10.
    type: float
  id:
    description:
    - Id path parameter. LAN Automation session identifier.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for LAN Automation LANAutomationLogByIdV1
  description: Complete reference of the LANAutomationLogByIdV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!l-an-automation-log-by-id
- name: Cisco DNA Center documentation for LAN Automation LANAutomationLogV1
  description: Complete reference of the LANAutomationLogV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!l-an-automation-log
notes:
  - SDK Method used are
    lan_automation.LanAutomation.lan_automation_log_by_id_v1,
    lan_automation.LanAutomation.lan_automation_log_v1,

  - Paths used are
    get /dna/intent/api/v1/lan-automation/log,
    get /dna/intent/api/v1/lan-automation/log/{id},
  - It should be noted that this module is an alias of lan_automation_log_v1_info

"""

EXAMPLES = r"""
- name: Get all Lan Automation Log Info
  cisco.catalystcenter.lan_automation_log_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    offset: 0
    limit: 0
  register: result

- name: Get Lan Automation Log Info by id
  cisco.catalystcenter.lan_automation_log_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "nwOrchId": "string",
          "entry": [
            {
              "logLevel": "string",
              "timeStamp": "string",
              "record": "string",
              "deviceId": "string"
            }
          ]
        }
      ],
      "version": "string"
    }
"""
