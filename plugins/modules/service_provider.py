#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: service_provider
short_description: Resource module for Service Provider
description:
  - Manage operations create and update of the resource Service Provider.
  - API to create Service Provider Profile QOS .
  - API to update Service Provider Profile QoS .
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  settings:
    description: Service Provider's settings.
    suboptions:
      qos:
        description: Service Provider's qos.
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
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Network Settings CreateSPProfile
    description: Complete reference of the CreateSPProfile API.
    link: https://developer.cisco.com/docs/dna-center/#!create-sp-profile
  - name: Cisco DNA Center documentation for Network Settings UpdateSPProfile
    description: Complete reference of the UpdateSPProfile API.
    link: https://developer.cisco.com/docs/dna-center/#!update-sp-profile
notes:
  - SDK Method used are
    network_settings.NetworkSettings.create_sp_profile,
    network_settings.NetworkSettings.update_sp_profile,
  - Paths used are
    post /dna/intent/api/v1/service-provider,
    put /dna/intent/api/v1/service-provider,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.service_provider:
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
- name: Update all
  cisco.catalystcenter.service_provider:
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
"""
RETURN = r"""
dnac_response:
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
