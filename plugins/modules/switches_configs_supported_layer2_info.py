#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: switches_configs_supported_layer2_info
short_description: Information module for Switches Configs Supported Layer2
description:
  - Get all Switches Configs Supported Layer2.
  - Returns the list of supported layer 2 features for the specified switch.
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
      - >
        Id path parameter. Network device id of the switch. The Network device id can be identified from the GET
        network device API /dna/intent/api/v1/network-device response.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wired GetSupportedLayer2Features
    description: Complete reference of the GetSupportedLayer2Features API.
    link: https://developer.cisco.com/docs/dna-center/#!get-supported-layer-2-features
notes:
  - SDK Method used are
    wired.Wired.get_supported_layer2_features,
  - Paths used are
    get /dna/campus/api/v1/switches/{id}/configs/supported/layer2,
"""

EXAMPLES = r"""
---
- name: Get all Switches Configs Supported Layer2
  cisco.catalystcenter.switches_configs_supported_layer2_info:
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
