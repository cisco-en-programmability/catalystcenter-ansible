#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wired_network_devices_network_device_id_config_features_intended_device_deployments_info
short_description: Information module for Wired Network
  Devices Network Device Id Config Features Intended
  Device Deployments
description:
  - Get all Wired Network Devices Network Device Id
    Config Features Intended Device Deployments.
  - The API returns device deployment status based on
    filter criteria.
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  networkDeviceId:
    description:
      - >
        NetworkDeviceId path parameter. Network device
        ID of the wired device to provision. The API
        /intent/api/v1/network-device can be used to
        get the network device ID.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wired GetDeviceDeploymentStatusConnectivity
    description: Complete reference of the GetDeviceDeploymentStatusConnectivity
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-device-deployment-status-connectivity
notes:
  - SDK Method used are
    wired.Wired.get_device_deployment_status_connectivity,
  - Paths used are
    get /dna/intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/deviceDeployments,
"""

EXAMPLES = r"""
---
- name: Get all Wired Network Devices Network Device
    Id Config Features Intended Device Deployments
  cisco.catalystcenter.wired_network_devices_network_device_id_config_features_intended_device_deployments_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
    networkDeviceId: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "activityId": "string",
          "configGroupName": "string",
          "configGroupVersion": 0,
          "status": "string",
          "networkDeviceId": "string",
          "createTime": 0,
          "lastUpdateTime": 0,
          "startTime": 0,
          "endTime": 0,
          "error": {
            "message": "string",
            "remedy": "string"
          }
        }
      ],
      "version": "string"
    }
"""
