#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: service_provider_create_v1
short_description: Resource module for Service Provider Create V1
description:
  - Manage operation create of the resource Service Provider Create V1.
  - API to create Service Provider Profile QOS .
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  settings:
    description: Service Provider Create's settings.
    suboptions:
      qos:
        description: Service Provider Create's qos.
        elements: dict
        suboptions:
          model:
            description: Model.
            type: str
          profileName:
            description: Profile Name.
            type: str
          wanProvider:
            description: Wan Provider.
            type: str
        type: list
    type: dict
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Network Settings CreateSPProfileV1
    description: Complete reference of the CreateSPProfileV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!create-sp-profile
notes:
  - SDK Method used are network_settings.NetworkSettings.create_sp_profile_v1,
  - Paths used are post /dna/intent/api/v1/service-provider,
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.service_provider_create_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    settings:
      qos:
        - model: string
          profileName: string
          wanProvider: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }
"""
