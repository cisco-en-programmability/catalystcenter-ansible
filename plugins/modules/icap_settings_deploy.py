#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: icap_settings_deploy
short_description: Resource module for Icap Settings Deploy
description:
  - Manage operation create of the resource Icap Settings Deploy.
  - Deploys the given ICAP configuration intent without preview and approve.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  payload:
    description: Icap Settings Deploy's payload.
    elements: dict
    suboptions:
      apId:
        description: Icap Settings Deploy's apId.
        type: str
      captureType:
        description: Icap Settings Deploy's captureType.
        type: str
      clientMac:
        description: Icap Settings Deploy's clientMac.
        type: str
      durationInMins:
        description: Icap Settings Deploy's durationInMins.
        type: int
      otaBand:
        description: Icap Settings Deploy's otaBand.
        type: str
      otaChannel:
        description: Icap Settings Deploy's otaChannel.
        type: int
      otaChannelWidth:
        description: Icap Settings Deploy's otaChannelWidth.
        type: int
      slots:
        description: Icap Settings Deploy's slots.
        elements: float
        type: list
      wlcId:
        description: Icap Settings Deploy's wlcId.
        type: str
    type: list
  previewDescription:
    description: PreviewDescription query parameter. The ICAP intent's preview-deploy description string.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Sensors DeploysTheGivenICAPConfigurationIntentWithoutPreviewAndApprove
    description: Complete reference of the DeploysTheGivenICAPConfigurationIntentWithoutPreviewAndApprove API.
    link: https://developer.cisco.com/docs/dna-center/#!deploys-the-given-icap-configuration-intent-without-preview-and-approve
notes:
  - SDK Method used are
    sensors.Sensors.deploys_the_given_icap_configuration_intent_without_preview_and_approve,
  - Paths used are
    post /dna/intent/api/v1/icapSettings/deploy,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.icap_settings_deploy:
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
