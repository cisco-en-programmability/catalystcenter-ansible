#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: icap_settings_deploy
short_description: Resource module for Icap Settings Deploy
description:
- This module represents an alias of the module icap_settings_deploy_v1
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Icap Settings Deploy's payload.
    elements: dict
    suboptions:
      apId:
        description: Ap Id.
        type: str
      captureType:
        description: Capture Type.
        type: str
      clientMac:
        description: Client Mac.
        type: str
      durationInMins:
        description: Duration In Mins.
        type: int
      otaBand:
        description: Ota Band.
        type: str
      otaChannel:
        description: Ota Channel.
        type: int
      otaChannelWidth:
        description: Ota Channel Width.
        type: int
      slot:
        description: Slot.
        elements: float
        type: list
      wlcId:
        description: Wlc Id.
        type: str
    type: list
  previewDescription:
    description: PreviewDescription query parameter. The ICAP intent's preview-deploy
      description string.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Sensors DeploysTheGivenICAPConfigurationIntentWithoutPreviewAndApproveV1
  description: Complete reference of the DeploysTheGivenICAPConfigurationIntentWithoutPreviewAndApproveV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!deploys-the-given-icap-configuration-intent-without-preview-and-approve
notes:
  - SDK Method used are
    sensors.Sensors.deploys_the_given_i_cap_configuration_intent_without_preview_and_approve_v1,

  - Paths used are
    post /dna/intent/api/v1/icapSettings/deploy,
  - It should be noted that this module is an alias of icap_settings_deploy_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.icap_settings_deploy:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    payload:
    - apId: string
      captureType: string
      clientMac: string
      durationInMins: 0
      otaBand: string
      otaChannel: 0
      otaChannelWidth: 0
      slot:
      - 0
      wlcId: string
    previewDescription: string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
