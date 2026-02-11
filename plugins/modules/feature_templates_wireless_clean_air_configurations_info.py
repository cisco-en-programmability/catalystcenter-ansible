#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: feature_templates_wireless_clean_air_configurations_info
short_description: Information module for Feature Templates Wireless Clean Air Configurations
description:
  - Get Feature Templates Wireless Clean Air Configurations by id.
  - This API allows users to retrieve a specific CleanAir configuration feature template by ID.
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Clean Air Configuration Feature Template Id.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Wireless GetCleanAirConfigurationFeatureTemplate
    description: Complete reference of the GetCleanAirConfigurationFeatureTemplate API.
    link: https://developer.cisco.com/docs/dna-center/#!get-clean-air-configuration-feature-template
notes:
  - SDK Method used are
    wireless.Wireless.get_clean_air_configuration_feature_template,
  - Paths used are
    get /dna/intent/api/v1/featureTemplates/wireless/cleanAirConfigurations/{id},
"""

EXAMPLES = r"""
---
- name: Get Feature Templates Wireless Clean Air Configurations by id
  cisco.catalystcenter.feature_templates_wireless_clean_air_configurations_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "designName": "string",
        "id": "string",
        "featureAttributes": {
          "radioBand": "string",
          "cleanAir": true,
          "cleanAirDeviceReporting": true,
          "persistentDevicePropagation": true,
          "description": "string",
          "interferersFeatures": {
            "bleBeacon": true,
            "bluetoothPagingInquiry": true,
            "bluetoothScoAcl": true,
            "continuousTransmitter": true,
            "genericDect": true,
            "genericTdd": true,
            "jammer": true,
            "microwaveOven": true,
            "motorolaCanopy": true,
            "siFhss": true,
            "spectrum80211Fh": true,
            "spectrum80211NonStandardChannel": true,
            "spectrum802154": true,
            "spectrumInverted": true,
            "superAg": true,
            "videoCamera": true,
            "wimaxFixed": true,
            "wimaxMobile": true,
            "xbox": true
          }
        },
        "unlockedAttributes": [
          "string"
        ]
      },
      "version": "string"
    }
"""
