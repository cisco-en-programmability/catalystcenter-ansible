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
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
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
