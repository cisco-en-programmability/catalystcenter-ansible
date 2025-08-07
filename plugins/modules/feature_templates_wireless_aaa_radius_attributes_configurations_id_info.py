#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: feature_templates_wireless_aaa_radius_attributes_configurations_id_info
short_description: Information module for Feature Templates
  Wireless Aaa Radius Attributes Configurations Id
description:
  - Get Feature Templates Wireless Aaa Radius Attributes
    Configurations Id by id.
  - This API allows users to retrieve a specific AAA
    Radius Attributes configuration feature template
    by ID.
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
      - Id path parameter. AAA Radius Attributes Configuration
        Feature Template Id.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless
      GetAAARadiusAttributesConfigurationFeatureTemplate
    description: Complete reference of the GetAAARadiusAttributesConfigurationFeatureTemplate
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-aaa-radius-attributes-configuration-feature-template
notes:
  - SDK Method used are
    wireless.Wireless.get_aaa_radius_attributes_configuration_feature_template,
  - Paths used are
    get /dna/intent/api/v1/featureTemplates/wireless/aaaRadiusAttributesConfigurations/{id},
"""

EXAMPLES = r"""
---
- name: Get Feature Templates Wireless Aaa Radius Attributes
    Configurations Id by id
  cisco.catalystcenter.feature_templates_wireless_aaa_radius_attributes_configurations_id_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "designName": "string",
        "id": "string",
        "featureAttributes": {
          "calledStationId": "string"
        },
        "unlockedAttributes": [
          "string"
        ]
      },
      "version": "string"
    }
"""
