#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: feature_templates_wireless_multicast_configurations_info
short_description: Information module for Feature Templates Wireless Multicast Configurations
description:
  - Get Feature Templates Wireless Multicast Configurations by id.
  - This API allows users to retrieve a specific Multicast configuration feature template by ID.
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
      - Id path parameter. Multicast Configuration Feature Template Id.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Wireless GetMulticastConfigurationFeatureTemplate
    description: Complete reference of the GetMulticastConfigurationFeatureTemplate API.
    link: https://developer.cisco.com/docs/dna-center/#!get-multicast-configuration-feature-template
notes:
  - SDK Method used are
    wireless.Wireless.get_multicast_configuration_feature_template,
  - Paths used are
    get /dna/intent/api/v1/featureTemplates/wireless/multicastConfigurations/{id},
"""

EXAMPLES = r"""
---
- name: Get Feature Templates Wireless Multicast Configurations by id
  cisco.catalystcenter.feature_templates_wireless_multicast_configurations_info:
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
          "globalMulticastEnabled": true,
          "multicastIpv4Mode": "string",
          "multicastIpv4Address": "string",
          "multicastIpv6Mode": "string",
          "multicastIpv6Address": "string"
        },
        "unlockedAttributes": [
          "string"
        ]
      },
      "version": "string"
    }
"""
