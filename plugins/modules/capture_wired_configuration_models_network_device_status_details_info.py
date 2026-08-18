#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: capture_wired_configuration_models_network_device_status_details_info
short_description: Information module for Capture Wired Configuration Models Network Device Status Details
description:
  - Get all Capture Wired Configuration Models Network Device Status Details.
  - Get wired capture configuration intent status per network device by the previewActivityId.
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
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices GetWiredCaptureConfigurationStatus
    description: Complete reference of the GetWiredCaptureConfigurationStatus API.
    link: https://developer.cisco.com/docs/dna-center/#!get-wired-capture-configuration-status
notes:
  - SDK Method used are
    devices.Devices.get_wired_capture_configuration_status,
  - Paths used are
    get /dna/intent/api/v1/capture/wired/configurationModels/{previewActivityId}/networkDeviceStatusDetails,
"""

EXAMPLES = r"""
---
- name: Get all Capture Wired Configuration Models Network Device Status Details
  cisco.catalystcenter.capture_wired_configuration_models_network_device_status_details_info:
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
