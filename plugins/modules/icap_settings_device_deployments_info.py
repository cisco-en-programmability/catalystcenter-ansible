#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: icap_settings_device_deployments_info
short_description: Information module for Icap Settings Device Deployments Info
description:
  - This module represents an alias of the module icap_settings_device_deployments_v1_info
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deployActivityId:
    description:
      - DeployActivityId query parameter. Activity from the /deploy task response.
    type: str
  networkDeviceIds:
    description:
      - NetworkDeviceIds query parameter. Device ids, retrievable from the id attribute
        in intent/api/v1/network-device.
    type: str
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first
        record is numbered 1.
    type: float
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: float
  sortBy:
    description:
      - SortBy query parameter. A property within the response to sort by.
    type: str
  order:
    description:
      - Order query parameter. Whether ascending or descending order should be used
        to sort the response.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sensors GetDeviceDeploymentStatusV1
    description: Complete reference of the GetDeviceDeploymentStatusV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-device-deployment-status
notes:
  - SDK Method used are sensors.Sensors.get_device_deployment_status_v1,
  - Paths used are get /dna/intent/api/v1/icapSettings/deviceDeployments,
  - It should be noted that this module is an alias of icap_settings_device_deployments_v1_info
"""
EXAMPLES = r"""
- name: Get all Icap Settings Device Deployments Info
  cisco.catalystcenter.icap_settings_device_deployments_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    deployActivityId: string
    networkDeviceIds: string
    offset: 0
    limit: 0
    sortBy: string
    order: string
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
          "deployActivityId": "string",
          "networkDeviceId": "string",
          "configGroupName": "string",
          "configGroupVersion": 0,
          "status": "string",
          "startTime": 0,
          "endTime": 0,
          "error": {}
        }
      ],
      "version": "string"
    }
"""
