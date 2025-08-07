#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_reboot_apreboot_info
short_description: Information module for Device Reboot
  Apreboot
description:
  - Get all Device Reboot Apreboot.
  - Users can query the access point reboot status using
    this intent API.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  parentTaskId:
    description:
      - ParentTaskId query parameter. Task id of ap
        reboot request.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless
      GetAccessPointRebootTaskResult
    description: Complete reference of the GetAccessPointRebootTaskResult
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-access-point-reboot-task-result
notes:
  - SDK Method used are
    wireless.Wireless.get_access_point_reboot_task_result,
  - Paths used are
    get /dna/intent/api/v1/device-reboot/apreboot/status,
"""

EXAMPLES = r"""
---
- name: Get all Device Reboot Apreboot
  cisco.catalystcenter.device_reboot_apreboot_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    parentTaskId: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "wlcIP": "string",
        "apList": [
          {
            "apName": "string",
            "rebootStatus": "string",
            "failureReason": {}
          }
        ]
      }
    ]
"""
