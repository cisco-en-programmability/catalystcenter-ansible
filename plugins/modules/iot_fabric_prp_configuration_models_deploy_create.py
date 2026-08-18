#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: iot_fabric_prp_configuration_models_deploy_create
short_description: Resource module for Iot Fabric Prp Configuration Models Deploy Create
description:
  - Manage operation create of the resource Iot Fabric Prp Configuration Models Deploy Create.
  - This API deploys the configuration model for PRP on network devices.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  previewActivityId:
    description: PreviewActivityId path parameter. The unique identifier for the PRP configuration model activity. It can
      be retrieved by following the Response Details steps in one of the following APIs and using the `activityId` value returned
      in the activity details as the `previewActivityId` - `POST /dna/intent/api/v1/iot/fabric/prp/configurationModels...
      - `POST /dna/intent/api/v1/iot/fabric/prp/configurationModels/update` - `POST /dna/intent/api/v1/iot/fabric/prp/configurationModels/delete`.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Industrial Configuration DeployTheConfigurationModelForPRPOnNetworkDevices
    description: Complete reference of the DeployTheConfigurationModelForPRPOnNetworkDevices API.
    link: https://developer.cisco.com/docs/dna-center/#!deploy-the-configuration-model-for-prp-on-network-devices
notes:
  - SDK Method used are
    industrial_configuration.IndustrialConfiguration.deploy_the_configuration_model_for_prp_on_network_devices,
  - Paths used are
    post /dna/intent/api/v1/iot/fabric/prp/configurationModels/{previewActivityId}/deploy,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.iot_fabric_prp_configuration_models_deploy_create:
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
