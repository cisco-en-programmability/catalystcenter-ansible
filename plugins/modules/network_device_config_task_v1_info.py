#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_config_task_v1_info
short_description: Information module for Network Device Config Task V1
description:
- Get all Network Device Config Task V1.
- Returns a config task result details by specified id.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  parentTaskId:
    description:
    - ParentTaskId query parameter. Task Id.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Configuration Archive GetConfigTaskDetailsV1
  description: Complete reference of the GetConfigTaskDetailsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-config-task-details
notes:
  - SDK Method used are
    configuration_archive.ConfigurationArchive.get_config_task_details_v1,

  - Paths used are
    get /dna/intent/api/v1/network-device-config/task,

"""

EXAMPLES = r"""
- name: Get all Network Device Config Task V1
  cisco.catalystcenter.network_device_config_task_v1_info:
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
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": [
        {
          "startTime": 0,
          "errorCode": "string",
          "deviceId": "string",
          "taskId": "string",
          "taskStatus": "string",
          "parentTaskId": "string",
          "deviceIpAddress": "string",
          "detailMessage": "string",
          "failureMessage": "string",
          "taskType": "string",
          "completionTime": 0,
          "hostName": "string"
        }
      ]
    }
"""
