#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: icap_settings_configuration_models_preview_activity_id_network_device_status_details_info
short_description: Information module for Icap Settings Configuration Models Preview Activity Id Network Device Status Details
description:
  - Get all Icap Settings Configuration Models Preview Activity Id Network Device Status Details.
  - Get ICAP configuration intent status per network device.
version_added: '2.0.0'
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
        PreviewActivityId path parameter. Activity ID value from the POST
        /dna/intent/api/v1/icapSettings/configurationModels task response.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Sensors GetICAPConfigurationIntentStatusPerNetworkDevice
    description: Complete reference of the GetICAPConfigurationIntentStatusPerNetworkDevice API.
    link: https://developer.cisco.com/docs/dna-center/#!get-icap-configuration-intent-status-per-network-device
notes:
  - SDK Method used are
    sensors.Sensors.get_icap_configuration_intent_status_per_network_device,
  - Paths used are
    get /dna/intent/api/v1/icapSettings/configurationModels/{previewActivityId}/networkDeviceStatusDetails,
"""

EXAMPLES = r"""
---
- name: Get all Icap Settings Configuration Models Preview Activity Id Network Device Status Details
  cisco.catalystcenter.icap_settings_configuration_models_preview_activity_id_network_device_status_details_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    previewActivityId: string
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
