#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: icap_settings_configuration_models_preview_activity_id_network_devices_network_device_id_config_info
short_description: Information module for Icap Settings Configuration Models Preview Activity Id Network Devices Network Device
  Id Config
description:
  - Get Icap Settings Configuration Models Preview Activity Id Network Devices Network Device Id Config by id.
  - Returns the device's CLIs of the ICAP intent.
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
        /dna/intent/api/v1/icapSettings/deviceConfigugrationModels task response.
    type: str
  networkDeviceId:
    description:
      - NetworkDeviceId path parameter. Network device UUID, used in ICAP configuration intent wlcId property.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Sensors RetrievesTheDevicesCLIsOfTheICAPIntent
    description: Complete reference of the RetrievesTheDevicesCLIsOfTheICAPIntent API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-devices-cl-is-of-the-icap-intent
notes:
  - SDK Method used are
    sensors.Sensors.retrieves_the_devices_clis_of_the_icapintent,
  - Paths used are
    get /dna/intent/api/v1/icapSettings/configurationModels/{previewActivityId}/networkDevices/{networkDeviceId}/config,
"""

EXAMPLES = r"""
---
- name: Get Icap Settings Configuration Models Preview Activity Id Network Devices Network Device Id Config by id
  cisco.catalystcenter.icap_settings_configuration_models_preview_activity_id_network_devices_network_device_id_config_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    previewActivityId: string
    networkDeviceId: string
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
        "previewItems": [
          {
            "configPreview": "string",
            "configType": "string",
            "errorMessages": [
              "string"
            ],
            "name": "string"
          }
        ],
        "status": "string"
      },
      "version": "string"
    }
"""
