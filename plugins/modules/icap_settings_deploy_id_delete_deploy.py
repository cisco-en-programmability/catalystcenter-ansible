#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: icap_settings_deploy_id_delete_deploy
short_description: Resource module for Icap Settings Deploy Id Delete Deploy
description:
  - Manage operation create of the resource Icap Settings Deploy Id Delete Deploy.
  - Remove the ICAP configuration from the device using id without preview-.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  id:
    description: Id path parameter. A unique ID of the deployed ICAP object, which can be obtained from GET /dna/intent/api/v1/icapSettings.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Sensors RemoveTheICAPConfigurationOnTheDeviceWithoutPreview
    description: Complete reference of the RemoveTheICAPConfigurationOnTheDeviceWithoutPreview API.
    link: https://developer.cisco.com/docs/dna-center/#!remove-the-icap-configuration-on-the-device-without-preview
notes:
  - SDK Method used are
    sensors.Sensors.remove_the_icap_configuration_on_the_device_without_preview,
  - Paths used are
    post /dna/intent/api/v1/icapSettings/deploy/{id}/deleteDeploy,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.icap_settings_deploy_id_delete_deploy:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    id: string
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
