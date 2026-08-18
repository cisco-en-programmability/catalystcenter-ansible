#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: capture_wired_configuration_models_deploy_create
short_description: Resource module for Capture Wired Configuration Models Deploy Create
description:
  - Manage operation create of the resource Capture Wired Configuration Models Deploy Create.
  - Deploys the wired capture configurations to the switch device.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  previewActivityId:
    description: PreviewActivityId path parameter. Activity from the POST /deviceConfigugrationModels task response.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices DeploysTheWiredCaptureConfigurationIntent
    description: Complete reference of the DeploysTheWiredCaptureConfigurationIntent API.
    link: https://developer.cisco.com/docs/dna-center/#!deploys-the-wired-capture-configuration-intent
notes:
  - SDK Method used are
    devices.Devices.deploys_the_wired_capture_configuration_intent,
  - Paths used are
    post /dna/intent/api/v1/capture/wired/configurationModels/{previewActivityId}/deploy,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.capture_wired_configuration_models_deploy_create:
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
