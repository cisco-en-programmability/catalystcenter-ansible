#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: service_provider_v2
short_description: Resource module for Service Provider V2
description:
  - Manage operations create and update of the resource Service Provider V2.
  - API to create Service Provider Profile QOS .
  - API to update Service Provider Profile QoS .
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  settings:
    description: Service Provider V2's settings.
    suboptions:
      qos:
        description: Service Provider V2's qos.
        elements: dict
        suboptions:
          model:
            description: Service Provider V2's model.
            type: str
          oldProfileName:
            description: Service Provider V2's oldProfileName.
            type: str
          profileName:
            description: Service Provider V2's profileName.
            type: str
          wanProvider:
            description: Service Provider V2's wanProvider.
            type: str
        type: list
    type: dict
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Network Settings CreateSPProfile
    description: Complete reference of the CreateSPProfile API.
    link: https://developer.cisco.com/docs/dna-center/#!create-sp-profile
  - name: Cisco Catalyst Center documentation for Network Settings UpdateSPProfile
    description: Complete reference of the UpdateSPProfile API.
    link: https://developer.cisco.com/docs/dna-center/#!update-sp-profile
notes:
  - SDK Method used are
    network_settings.NetworkSettings.create_sp_profile,
    network_settings.NetworkSettings.update_sp_profile,
  - Paths used are
    post /dna/intent/api/v2/service-provider,
    put /dna/intent/api/v2/service-provider,
"""

EXAMPLES = r"""
---
- name: Update all
  cisco.catalystcenter.service_provider_v2:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    settings:
      qos:
        - model: string
          oldProfileName: string
          profileName: string
          wanProvider: string
- name: Create
  cisco.catalystcenter.service_provider_v2:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    settings:
      qos:
        - model: string
          profileName: string
          wanProvider: string
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
