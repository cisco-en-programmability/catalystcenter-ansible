#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: capture_wired_configuration_models_create
short_description: Resource module for Capture Wired Configuration Models Create
description:
  - Manage operation create of the resource Capture Wired Configuration Models Create.
  - Creates a wired capture session for preview prior to deploying the configurations on to the switch device.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  metadata:
    description: Additional metadata for the request.
    type: dict
  previewDescription:
    description: The wired capture session's preview-deploy description string.
    type: str
  wiredCaptureSettings:
    description: A list of wired capture session intents parameters that will be applied to switch.
    elements: dict
    suboptions:
      bufferSizeInMb:
        description: The capture buffer size in megabytes. This value is enforced to 100 MB by the server regardless of client
          input and should not be provided in request payloads.
        type: int
      bufferType:
        description: This is the buffer type. Only LINEAR is supported.
        type: str
      deviceId:
        description: The switch UUID.
        type: str
      durationInSeconds:
        description: The duration of the wired capture session in minutes.
        type: int
      filterExpression:
        description: The filter expression which will be used in capturing packets at the switch interface. Packets that are
          not satisfied the filter conditions will not be captured.
        type: str
      interfaceName:
        description: The switch interface where the capture settings are applied. In wired packet capture intent API, tell
          user to use API /data/api/v1/interfaces/query to get the interface name list by following the example below. The
          switch is identified by networkDeviceId=<UUID> in the POST body. It is best to use startTime and endTime as time
          range for the last 15 minutes.
        type: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices CreatesAWiredCaptureForPreview
    description: Complete reference of the CreatesAWiredCaptureForPreview API.
    link: https://developer.cisco.com/docs/dna-center/#!creates-a-wired-capture-for-preview
notes:
  - SDK Method used are
    devices.Devices.creates_a_wired_capture_for_preview,
  - Paths used are
    post /dna/intent/api/v1/capture/wired/configurationModels,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.capture_wired_configuration_models_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    metadata: {}
    previewDescription: string
    wiredCaptureSettings:
      - bufferSizeInMb: 0
        bufferType: string
        deviceId: string
        durationInSeconds: 0
        filterExpression: string
        interfaceName: string
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
