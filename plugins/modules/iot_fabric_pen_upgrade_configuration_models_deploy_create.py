#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: iot_fabric_pen_upgrade_configuration_models_deploy_create
short_description: Resource module for Iot Fabric Pen Upgrade Configuration Models Deploy Create
description:
  - Manage operation create of the resource Iot Fabric Pen Upgrade Configuration Models Deploy Create.
  - This API deploys the configuration model for EN to PEN upgrade on network devices.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  previewActivityId:
    description: PreviewActivityId path parameter. The unique identifier for the activity. It can be retrieved by following
      the steps mentioned in Response Details section of POST API - `/dna/intent/api/v1/fabric/penUpgrade/configurationModels`.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Industrial Configuration DeployTheConfigurationModelForENToPENUpgradeOnNetworkDevices
    description: Complete reference of the DeployTheConfigurationModelForENToPENUpgradeOnNetworkDevices API.
    link: https://developer.cisco.com/docs/dna-center/#!deploy-the-configuration-model-for-en-to-pen-upgrade-on-network-devices
notes:
  - SDK Method used are
    industrial_configuration.IndustrialConfiguration.deploy_the_configuration_model_for_en_to_pen_upgrade_on_network_devices,
  - Paths used are
    post /dna/intent/api/v1/iot/fabric/penUpgrade/configurationModels/{previewActivityId}/deploy,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.iot_fabric_pen_upgrade_configuration_models_deploy_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    previewActivityId: 7f422eeb-effe-4938-9371-ccf6dc2fe15e
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
