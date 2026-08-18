#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: iot_fabric_pen_upgrade_deploy_create
short_description: Resource module for Iot Fabric Pen Upgrade Deploy Create
description:
  - Manage operation create of the resource Iot Fabric Pen Upgrade Deploy Create.
  - This API performs EN to PEN upgrade without generating a config preview.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  networkDeviceId:
    description: Identifier of the network device which is the extended node. It is the `id` attribute in the response of
      API - `/dna/intent/api/v1/networkDevices`.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Industrial Configuration PerformENToPENUpgradeWithoutGeneratingAConfigPreview
    description: Complete reference of the PerformENToPENUpgradeWithoutGeneratingAConfigPreview API.
    link: https://developer.cisco.com/docs/dna-center/#!perform-en-to-pen-upgrade-without-generating-a-config-preview
notes:
  - SDK Method used are
    industrial_configuration.IndustrialConfiguration.perform_en_to_pen_upgrade_without_generating_a_config_preview,
  - Paths used are
    post /dna/intent/api/v1/iot/fabric/penUpgrade/deploy,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.iot_fabric_pen_upgrade_deploy_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    networkDeviceId: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
