#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: provision_switches_configs_intended_device_deployments_info
short_description: Information module for Provision Switches Configs Intended Device Deployments
description:
  - Get all Provision Switches Configs Intended Device Deployments.
  - Returns device deployment status based on filter criteria.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - >
        Id path parameter. Network device id of the switch to provision. The API /intent/api/v1/network-device
        can be used to get the network device ID.
    type: str
  deployActivityId:
    description:
      - DeployActivityId query parameter. Activity from the /deploy task response.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wired GetDeviceDeploymentStatusConnectivity
    description: Complete reference of the GetDeviceDeploymentStatusConnectivity API.
    link: https://developer.cisco.com/docs/dna-center/#!get-device-deployment-status-connectivity
notes:
  - SDK Method used are
    wired.Wired.get_device_deployment_status_connectivity,
  - Paths used are
    get /dna/campus/api/v1/provision/switches/{id}/configs/intended/deviceDeployments,
"""

EXAMPLES = r"""
---
- name: Get all Provision Switches Configs Intended Device Deployments
  cisco.catalystcenter.provision_switches_configs_intended_device_deployments_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    deployActivityId: 98762eeb-effe-4938-9371-ccf6dc2fe15e
    id: dd584a8a-a7ae-4323-97f4-ab950cab52a6
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "activityId": "string",
          "networkDeviceId": "string",
          "configGroupName": "string",
          "configGroupVersion": 0,
          "status": {},
          "createTime": {},
          "lastUpdateTime": {},
          "startTime": {},
          "endTime": {},
          "error": {
            "message": "string",
            "remedy": "string"
          }
        }
      ],
      "version": "string"
    }
"""
