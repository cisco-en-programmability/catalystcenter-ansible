#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: iot_fabric_pen_upgrade_configuration_models_create
short_description: Resource module for Iot Fabric Pen Upgrade Configuration Models Create
description:
  - Manage operation create of the resource Iot Fabric Pen Upgrade Configuration Models Create. - > This API creates configuration
    model needed for performing EN to PEN upgrade. This is a pre-requisite if you want to preview the generated config for
    the provisioning intent.
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
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Industrial Configuration CreateAConfigurationModelForPerformingENToPENUpgrade
    description: Complete reference of the CreateAConfigurationModelForPerformingENToPENUpgrade API.
    link: https://developer.cisco.com/docs/dna-center/#!create-a-configuration-model-for-performing-en-to-pen-upgrade
notes:
  - SDK Method used are
    industrial_configuration.IndustrialConfiguration.create_a_configuration_model_for_performing_en_to_pen_upgrade,
  - Paths used are
    post /dna/intent/api/v1/iot/fabric/penUpgrade/configurationModels,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.iot_fabric_pen_upgrade_configuration_models_create:
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
