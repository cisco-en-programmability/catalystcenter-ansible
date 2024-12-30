#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: icap_settings_device_deployments_count_info
short_description: Information module for Icap Settings Device Deployments Count Info
description:
- This module represents an alias of the module icap_settings_device_deployments_count_v1_info
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
    - NetworkDeviceIds query parameter. Device ids, retrievable from the id attribute in intent/api/v1/network-device.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Sensors GetDeviceDeploymentStatusCountV1
  description: Complete reference of the GetDeviceDeploymentStatusCountV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-device-deployment-status-count
notes:
  - SDK Method used are
    sensors.Sensors.get_device_deployment_status_count_v1,

  - Paths used are
    get /dna/intent/api/v1/icapSettings/deviceDeployments/count,
  - It should be noted that this module is an alias of icap_settings_device_deployments_count_v1_info

"""

EXAMPLES = r"""
- name: Get all Icap Settings Device Deployments Count Info
  cisco.catalystcenter.icap_settings_device_deployments_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    deployActivityId: string
    networkDeviceIds: string
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
        "count": 0
      },
      "version": "string"
    }
"""
