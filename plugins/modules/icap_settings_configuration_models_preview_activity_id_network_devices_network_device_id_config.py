#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: icap_settings_configuration_models_preview_activity_id_network_devices_network_device_id_config
short_description: Resource module for Icap Settings Configuration Models Preview Activity Id Network Devices Network Device
  Id Config
description:
  - Manage operation create of the resource Icap Settings Configuration Models Preview Activity Id Network Devices Network
    Device Id Config.
  - Generates the device's CLIs of the ICAP configuration intent.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  networkDeviceId:
    description: NetworkDeviceId path parameter. Device id (wlcId) from intent/api/v1/network-device.
    type: str
  previewActivityId:
    description: PreviewActivityId path parameter. Activity from the POST /dna/intent/api/v1/icapSettings/configura... task
      response.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Sensors GeneratesTheDevicesCLIsOfTheICAPConfigurationIntent
    description: Complete reference of the GeneratesTheDevicesCLIsOfTheICAPConfigurationIntent API.
    link: https://developer.cisco.com/docs/dna-center/#!generates-the-devices-cl-is-of-the-icap-configuration-intent
notes:
  - SDK Method used are
    sensors.Sensors.generates_the_devices_clis_of_the_icap_configuration_intent,
  - Paths used are
    post /dna/intent/api/v1/icapSettings/configurationModels/{previewActivityId}/networkDevices/{networkDeviceId}/config,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.icap_settings_configuration_models_preview_activity_id_network_devices_network_device_id_config:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    networkDeviceId: string
    previewActivityId: string
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
