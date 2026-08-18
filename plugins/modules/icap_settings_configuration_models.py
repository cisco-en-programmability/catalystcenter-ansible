#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: icap_settings_configuration_models
short_description: Resource module for Icap Settings Configuration Models
description:
  - Manage operation create of the resource Icap Settings Configuration Models.
  - Creates an ICAP configuration intent for preview-approve.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  payload:
    description: Icap Settings Configuration Models's payload.
    elements: dict
    suboptions:
      apId:
        description: Icap Settings Configuration Models's apId.
        type: str
      captureType:
        description: Icap Settings Configuration Models's captureType.
        type: str
      clientMac:
        description: Icap Settings Configuration Models's clientMac.
        type: str
      durationInMins:
        description: Icap Settings Configuration Models's durationInMins.
        type: int
      otaBand:
        description: Icap Settings Configuration Models's otaBand.
        type: str
      otaChannel:
        description: Icap Settings Configuration Models's otaChannel.
        type: int
      otaChannelWidth:
        description: Icap Settings Configuration Models's otaChannelWidth.
        type: int
      slots:
        description: Icap Settings Configuration Models's slots.
        elements: float
        type: list
      wlcId:
        description: Icap Settings Configuration Models's wlcId.
        type: str
    type: list
  previewDescription:
    description: PreviewDescription query parameter. The ICAP intent's preview-deploy description string.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Sensors CreatesAnICAPConfigurationIntentForPreviewApprove
    description: Complete reference of the CreatesAnICAPConfigurationIntentForPreviewApprove API.
    link: https://developer.cisco.com/docs/dna-center/#!creates-an-icap-configuration-intent-for-preview-approve
notes:
  - SDK Method used are
    sensors.Sensors.creates_an_icap_configuration_intent_for_preview_approve,
  - Paths used are
    post /dna/intent/api/v1/icapSettings/configurationModels,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.icap_settings_configuration_models:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    payload:
      - apId: string
        captureType: string
        clientMac: string
        durationInMins: 0
        otaBand: string
        otaChannel: 0
        otaChannelWidth: 0
        slots:
          - 0
        wlcId: string
    previewDescription: string
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
