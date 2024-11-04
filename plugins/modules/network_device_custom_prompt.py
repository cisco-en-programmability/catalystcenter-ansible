#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_custom_prompt
short_description: Resource module for Network Device Custom Prompt
description:
- Manage operation create of the resource Network Device Custom Prompt.
- >
   Save custom prompt added by user in Catalyst Center. API will always override the existing prompts. User should
   provide all the custom prompt in case of any update.
version_added: '6.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  passwordPrompt:
    description: Password for Custom Prompt.
    type: str
  usernamePrompt:
    description: Username for Custom Prompt.
    type: str
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for System Settings CustomPromptPOSTAPIV1
  description: Complete reference of the CustomPromptPOSTAPIV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!custom-prompt-postapi-v-1
notes:
  - SDK Method used are
    system_settings.SystemSettings.custom_prompt_post_api_v1,

  - Paths used are
    post /dna/intent/api/v1/network-device/custom-prompt,

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.network_device_custom_prompt:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    passwordPrompt: string
    usernamePrompt: string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
