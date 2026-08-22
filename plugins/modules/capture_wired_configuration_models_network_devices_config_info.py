#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: capture_wired_configuration_models_network_devices_config_info
short_description: Information module for Capture Wired Configuration Models Network Devices Config
description:
  - Get Capture Wired Configuration Models Network Devices Config by id.
  - Returns the device's CLIs of the wired capture intent.
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
      - PreviewActivityId path parameter. Activity from the POST /deviceConfigugrationModels task response.
    type: str
  networkDeviceId:
    description:
      - NetworkDeviceId path parameter. Device id from intent/api/v1/network-device.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices RetrievesTheDevicesCLIsInPreview
    description: Complete reference of the RetrievesTheDevicesCLIsInPreview API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-devices-cl-is-in-preview
notes:
  - SDK Method used are
    devices.Devices.retrieves_the_devices_clis_in_preview,
  - Paths used are
    get /dna/intent/api/v1/capture/wired/configurationModels/{previewActivityId}/networkDevices/{networkDeviceId}/config,
"""

EXAMPLES = r"""
---
- name: Get Capture Wired Configuration Models Network Devices Config by id
  cisco.catalystcenter.capture_wired_configuration_models_network_devices_config_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    previewActivityId: 7f422eeb-effe-4938-9371-ccf6dc2fe15e
    networkDeviceId: efab65ed-dcbe-4857-999e-af3e477aed1a
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
