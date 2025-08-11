#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: icap_settings_configuration_models_preview_activity_id_network_devices_network_device_id_config
short_description: Resource module for Icap Settings
  Configuration Models Preview Activity Id Network Devices
  Network Device Id Config
description:
  - Manage operation create of the resource Icap Settings
    Configuration Models Preview Activity Id Network
    Devices Network Device Id Config. - > Generates
    the device's CLIs of the ICAP intent for preview
    and approve prior to deploying the ICAP configuration
    intent to the device. After deploying the configuration
    intent, generating intent CLIs will not be available
    for preview. For detailed information about the
    usage of the API, please refer to the Open API specification
    document - https //github.com/cisco-en-programmability/catalyst-center-api-
    specs/blob/main/Assurance/CE_Cat_Center_Org-ICAP_APIs-1.0.0-resolved.yaml.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  networkDeviceId:
    description: NetworkDeviceId path parameter. Device
      id from intent/api/v1/network-device.
    type: str
  object:
    description: Object.
    type: str
  previewActivityId:
    description: PreviewActivityId path parameter. Activity
      from the POST /deviceConfigugrationModels task
      response.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sensors
      GeneratesTheDevicesCLIsOfTheICAPConfigurationIntent
    description: Complete reference of the GeneratesTheDevicesCLIsOfTheICAPConfigurationIntent
      API.
    link: https://developer.cisco.com/docs/dna-center/#!generates-the-devices-cl-is-of-the-icap-configuration-intent
notes:
  - SDK Method used are
    sensors.Sensors.generates_the_devices_clis_of_the_i_cap_configuration_intent,
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
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    networkDeviceId: string
    object: string
    previewActivityId: string
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
