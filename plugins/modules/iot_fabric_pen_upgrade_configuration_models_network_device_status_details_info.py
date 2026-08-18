#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: iot_fabric_pen_upgrade_configuration_models_network_device_status_details_info
short_description: Information module for Iot Fabric Pen Upgrade Configuration Models Network Device Status Details
description:
  - Get all Iot Fabric Pen Upgrade Configuration Models Network Device Status Details.
  - This API retrieves the status of the configuration model for network devices in EN to PEN upgrade.
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
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Industrial Configuration RetrieveConfigurationModelGenerationStatusForENToPENUpgrade
    description: Complete reference of the RetrieveConfigurationModelGenerationStatusForENToPENUpgrade API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-configuration-model-generation-status-for-en-to-pen-upgrade
notes:
  - SDK Method used are
    industrial_configuration.IndustrialConfiguration.retrieve_configuration_model_generation_status_for_en_to_pen_upgrade,
  - Paths used are
    get /dna/intent/api/v1/iot/fabric/penUpgrade/configurationModels/{previewActivityId}/networkDeviceStatusDetails,
"""

EXAMPLES = r"""
---
- name: Get all Iot Fabric Pen Upgrade Configuration Models Network Device Status Details
  cisco.catalystcenter.iot_fabric_pen_upgrade_configuration_models_network_device_status_details_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    previewActivityId: 7f422eeb-effe-4938-9371-ccf6dc2fe15e
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
          "networkDeviceId": "string",
          "status": "string"
        }
      ],
      "version": "string"
    }
"""
