#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: iot_fabric_pen_upgrade_configuration_models_network_devices_config_info
short_description: Information module for Iot Fabric Pen Upgrade Configuration Models Network Devices Config
description:
  - Get Iot Fabric Pen Upgrade Configuration Models Network Devices Config by id. - > This API retrieves the configuration
    for specific network device for a given EN to PEN upgrade configuration model using `previewActivityId` and `networkDeviceId`.
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
        PreviewActivityId path parameter. The unique identifier for the activity. It can be retrieved by
        following the steps mentioned in Response Details section of POST API -
        `/dna/intent/api/v1/fabric/penUpgrade/configurationModels`.
    type: str
  networkDeviceId:
    description:
      - >
        NetworkDeviceId path parameter. Identifier of the network device which is the extended node. It is the
        `id` attribute in the response of API - `/dna/intent/api/v1/networkDevices`.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Industrial Configuration RetrieveTheConfigOfNetworkDeviceForENToPENUpgradeConfigurationModel
    description: Complete reference of the RetrieveTheConfigOfNetworkDeviceForENToPENUpgradeConfigurationModel API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-config-of-network-device-for-en-to-pen-upgrade-configuration-model
notes:
  - SDK Method used are
    industrial_configuration.IndustrialConfiguration.retrieve_the_config_of_network_device_for_en_to_pen_upgrade_configuration_model,
  - Paths used are
    get /dna/intent/api/v1/iot/fabric/penUpgrade/configurationModels/{previewActivityId}/networkDevices/{networkDeviceId}/config,
"""

EXAMPLES = r"""
---
- name: Get Iot Fabric Pen Upgrade Configuration Models Network Devices Config by id
  cisco.catalystcenter.iot_fabric_pen_upgrade_configuration_models_network_devices_config_info:
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
