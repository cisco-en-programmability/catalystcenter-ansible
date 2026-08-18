#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: switches_configs_supported_layer3_info
short_description: Information module for Switches Configs Supported Layer3
description:
  - Get all Switches Configs Supported Layer3. - > Returns the list of supported layer 3 features for the specified switch.The
    feature names are the supported to be used as feature in the all get deployed layer 3 endpoints.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Network device ID of the switch.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wired GetSupportedLayer3Features
    description: Complete reference of the GetSupportedLayer3Features API.
    link: https://developer.cisco.com/docs/dna-center/#!get-supported-layer-3-features
notes:
  - SDK Method used are
    wired.Wired.get_supported_layer3_features,
  - Paths used are
    get /dna/campus/api/v1/switches/{id}/configs/supported/layer3,
"""

EXAMPLES = r"""
---
- name: Get all Switches Configs Supported Layer3
  cisco.catalystcenter.switches_configs_supported_layer3_info:
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
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "name": "string"
        }
      ],
      "version": "string"
    }
"""
