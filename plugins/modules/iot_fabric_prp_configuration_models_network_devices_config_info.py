#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: iot_fabric_prp_configuration_models_network_devices_config_info
short_description: Information module for Iot Fabric Prp Configuration Models Network Devices Config
description:
  - Get Iot Fabric Prp Configuration Models Network Devices Config by id. - > This API retrieves the configuration preview
    for a specific network device for the given PRP configuration model, identified by `previewActivityId` and `networkDeviceId`.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  previewActivityId:
    description:
      - >
        PreviewActivityId path parameter. The unique identifier for the PRP configuration model activity. It can
        be retrieved by following the Response Details steps in one of the following APIs and using the
        `activityId` value returned in the activity details as the `previewActivityId` - `POST
        /dna/intent/api/v1/iot/fabric/prp/configurationModels/create` - `POST
        /dna/intent/api/v1/iot/fabric/prp/configurationModels/update` - `POST
        /dna/intent/api/v1/iot/fabric/prp/configurationModels/delete`.
    type: str
  networkDeviceId:
    description:
      - >
        NetworkDeviceId path parameter. Identifier of the network device. It is the `id` attribute in the
        response of API - `/dna/intent/api/v1/networkDevices`.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Industrial Configuration RetrieveGeneratedPRPConfigurationForTheGivenNetworkDeviceAndPRPConfigurationModel
    description: Complete reference of the RetrieveGeneratedPRPConfigurationForTheGivenNetworkDeviceAndPRPConfigurationModel
      API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-generated-prp-configuration-for-the-given-network-device-and-prp-configuration-model
notes:
  - SDK Method used are
    industrial_configuration.IndustrialConfiguration.retrieve_generated_prp_configuration_for_the_given_network_device_and_prp_configuration_model,
  - Paths used are
    get /dna/intent/api/v1/iot/fabric/prp/configurationModels/{previewActivityId}/networkDevices/{networkDeviceId}/config,
"""

EXAMPLES = r"""
---
- name: Get Iot Fabric Prp Configuration Models Network Devices Config by id
  cisco.catalystcenter.iot_fabric_prp_configuration_models_network_devices_config_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    previewActivityId: 7f422eeb-effe-4938-9371-ccf6dc2fe15e
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "networkDeviceId": "string",
        "status": "string",
        "previewItems": [
          {
            "name": "string",
            "configType": "string",
            "configPreview": "string",
            "errorMessages": [
              "string"
            ]
          }
        ]
      },
      "version": "string"
    }
"""
