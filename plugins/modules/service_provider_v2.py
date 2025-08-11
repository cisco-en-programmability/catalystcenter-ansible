#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: service_provider_v2
short_description: Resource module for Service Provider
  V2
description:
  - Manage operations create and update of the resource
    Service Provider V2.
  - API to create Service Provider Profile QOS .
  - API to update Service Provider Profile QoS .
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  settings:
    description: Service Provider V2's settings.
    suboptions:
      qos:
        description: Service Provider V2's qos.
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
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Network
      Settings CreateSPProfileV2
    description: Complete reference of the CreateSPProfileV2
      API.
    link: https://developer.cisco.com/docs/dna-center/#!create-sp-profile-v-2
  - name: Cisco DNA Center documentation for Network
      Settings UpdateSPProfileV2
    description: Complete reference of the UpdateSPProfileV2
      API.
    link: https://developer.cisco.com/docs/dna-center/#!update-sp-profile-v-2
notes:
  - SDK Method used are
    network_settings.NetworkSettings.create_sp_profile_v2,
    network_settings.NetworkSettings.update_sp_profile_v2,
  - Paths used are
    post /dna/intent/api/v2/service-provider,
    put /dna/intent/api/v2/service-provider,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.service_provider:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    settings:
      qos:
        - model: string
          profileName: string
          wanProvider: string
- name: Update all
  cisco.catalystcenter.service_provider:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    settings:
      qos:
        - model: string
          oldProfileName: string
          profileName: string
          wanProvider: string
"""
RETURN = r"""
dnac_response:
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
