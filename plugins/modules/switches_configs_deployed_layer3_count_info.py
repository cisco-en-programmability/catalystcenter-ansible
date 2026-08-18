#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: switches_configs_deployed_layer3_count_info
short_description: Information module for Switches Configs Deployed Layer3 Count
description:
  - Get Switches Configs Deployed Layer3 Count by id. - > Returns the number of deployed configuration entries for the specified
    layer 3 feature on the switch. The device config learning must have enabled for the switch using the API /dna/campus/api/v1/switches/configs/deployed/enable
    and Error code NCCO15475 can be observed if not enabled.
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
  feature:
    description:
      - >
        Feature path parameter. Name of the feature to retrieve configuration for. The API
        /api/v1/switches/{id}/configs/supported/layer3 can be used to get the list of features supported on a
        device.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wired GetDeployedLayer3ConfigCount
    description: Complete reference of the GetDeployedLayer3ConfigCount API.
    link: https://developer.cisco.com/docs/dna-center/#!get-deployed-layer-3-config-count
notes:
  - SDK Method used are
    wired.Wired.get_deployed_layer3_config_count,
  - Paths used are
    get /dna/campus/api/v1/switches/{id}/configs/deployed/layer3/{feature}/count,
"""

EXAMPLES = r"""
---
- name: Get Switches Configs Deployed Layer3 Count by id
  cisco.catalystcenter.switches_configs_deployed_layer3_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
    feature: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": 0,
      "version": "string"
    }
"""
