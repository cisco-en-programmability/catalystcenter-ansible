#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: wireless_access_points_factory_reset_request_status_info
short_description: Information module for Wireless Access Points Factory Reset Request
  Status Info
description:
  - This module represents an alias of the module wireless_access_points_factory_reset_request_status_v1_info
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
      - TaskId query parameter. Provide the task id which is returned in the response
        of ap factory reset post api.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless GetAccessPointsFactoryResetStatusV1
    description: Complete reference of the GetAccessPointsFactoryResetStatusV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-access-points-factory-reset-status
notes:
  - SDK Method used are wireless.Wireless.get_access_points_factory_reset_status_v1,
  - Paths used are get /dna/intent/api/v1/wirelessAccessPoints/factoryResetRequestStatus,
  - It should be noted that this module is an alias of wireless_access_points_factory_reset_request_status_v1_info
"""
EXAMPLES = r"""
- name: Get all Wireless Access Points Factory Reset Request Status Info
  cisco.catalystcenter.wireless_access_points_factory_reset_request_status_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    taskId: string
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
