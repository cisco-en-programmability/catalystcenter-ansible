#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: switches_configs_status_create
short_description: Resource module for Switches Configs Status Create
description:
  - Manage operation create of the resource Switches Configs Status Create.
  - Returns the deployed configuration learning status for each requested device UUID.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  deviceUuids:
    description: One or more switch UUIDs. The Network device id can be identified from the GET network device API /dna/intent/api/v1/network-device
      response.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wired GetDeployedConfigurationLearningStatus
    description: Complete reference of the GetDeployedConfigurationLearningStatus API.
    link: https://developer.cisco.com/docs/dna-center/#!get-deployed-configuration-learning-status
notes:
  - SDK Method used are
    wired.Wired.get_deployed_configuration_learning_status,
  - Paths used are
    post /dna/campus/api/v1/switches/configs/status,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.switches_configs_status_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    deviceUuids:
      - 8a4f95df-13da-4f5a-9a89-95ca4f8f6f79
      - 8a4f95df-13da-4f5a-9a89-95ca4f8f6f80
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "items": [
        {
          "deviceId": "string",
          "status": "string",
          "isSyncRequired": true
        }
      ]
    }
"""
