#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module:
  icap_settings_configuration_models_preview_activity_id_network_devices_network_device_id_config
short_description: Resource module for Icap Settings Configuration Models Preview
  Activity Id Network Devices Network Device Id Config                                                                                  # noqa: E501
description:
  - This module represents an alias of the module
    icap_settings_configuration_models_preview_activity_id_network_devices_network_device_id_config_v1                                              # noqa: E501
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  networkDeviceId:
    description: NetworkDeviceId path parameter. Device id from intent/api/v1/network-device.
    type: str
  object:
    description: Object.
    type: str
  previewActivityId:
    description: PreviewActivityId path parameter. Activity from the POST /deviceConfigugrationModels
      task response.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sensors GeneratesTheDevice'sCLIsOfTheICAPConfigurationIntentV1
    description: Complete reference of the GeneratesTheDevice'sCLIsOfTheICAPConfigurationIntentV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!generates-the-device's-cl-is-of-the-icap-configuration-intent
notes:
  - SDK Method used are sensors.Sensors.generates_the_devices_clis_of_the_i_cap_configuration_intent_v1,
  - Paths used are post
    /dna/intent/api/v1/icapSettings/configurationModels/{previewActivityId}/networkDevices/{networkDeviceId}/config,
  - It should be noted that this module is an alias of
    icap_settings_configuration_models_preview_activity_id_network_devices_network_device_id_config_v1                                                     # noqa: E501
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.icap_settings_configuration_models_preview_activity_id_network_devices_network_device_id_config:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    state: present
    networkDeviceId: string
    object: string
    previewActivityId: string
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
