#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_access_points_factory_reset_request_status_info
short_description: Information module for Wireless Access Points Factory Reset Request Status
description:
  - Get all Wireless Access Points Factory Reset Request Status.
  - This API returns each AP Factory Reset initiation status.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  taskId:
    description:
      - TaskId query parameter. Provide the task id which is returned in the response of ap factory reset post api.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Wireless GetAccessPointsFactoryResetStatus
    description: Complete reference of the GetAccessPointsFactoryResetStatus API.
    link: https://developer.cisco.com/docs/dna-center/#!get-access-points-factory-reset-status
notes:
  - SDK Method used are
    wireless.Wireless.get_access_points_factory_reset_status,
  - Paths used are
    get /dna/intent/api/v1/wirelessAccessPoints/factoryResetRequestStatus,
"""

EXAMPLES = r"""
---
- name: Get all Wireless Access Points Factory Reset Request Status
  cisco.catalystcenter.wireless_access_points_factory_reset_request_status_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    taskId: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "wlcIP": "string",
          "wlcName": "string",
          "apResponseInfoList": [
            {
              "apName": "string",
              "apFactoryResetStatus": "string",
              "failureReason": "string",
              "radioMacAddress": "string",
              "ethernetMacAddress": "string"
            }
          ]
        }
      ],
      "version": "string"
    }
"""
