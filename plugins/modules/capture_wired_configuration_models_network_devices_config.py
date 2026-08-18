#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: capture_wired_configuration_models_network_devices_config
short_description: Resource module for Capture Wired Configuration Models Network Devices Config
description:
  - Manage operation create of the resource Capture Wired Configuration Models Network Devices Config.
  - Generates the CLIs that will be applied on the switch device for preview.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  networkDeviceId:
    description: NetworkDeviceId path parameter. Device id from intent/api/v1/network-device.
    type: str
  previewActivityId:
    description: PreviewActivityId path parameter. Activity from the POST /deviceConfigugrationModels task response.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices GeneratesTheDevicesCLIsInPreview
    description: Complete reference of the GeneratesTheDevicesCLIsInPreview API.
    link: https://developer.cisco.com/docs/dna-center/#!generates-the-devices-cl-is-in-preview
notes:
  - SDK Method used are
    devices.Devices.generates_the_devices_clis_in_preview,
  - Paths used are
    post /dna/intent/api/v1/capture/wired/configurationModels/{previewActivityId}/networkDevices/{networkDeviceId}/config,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.capture_wired_configuration_models_network_devices_config:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    networkDeviceId: efab65ed-dcbe-4857-999e-af3e477aed1a
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
