#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_device_custom_prompt
short_description: Resource module for Network Device Custom Prompt
description:
  - This module represents an alias of the module network_device_custom_prompt_v1
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
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for System Settings CustomPromptPOSTAPIV1
    description: Complete reference of the CustomPromptPOSTAPIV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!custom-prompt-postapi
notes:
  - SDK Method used are system_settings.SystemSettings.custom_prompt_post_api_v1,
  - Paths used are post /dna/intent/api/v1/network-device/custom-prompt,
  - It should be noted that this module is an alias of network_device_custom_prompt_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.network_device_custom_prompt:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    passwordPrompt: string
    usernamePrompt: string
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
