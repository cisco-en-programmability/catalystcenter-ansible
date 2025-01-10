#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_fabric_zones_count_v1_info
short_description: Information module for Sda Fabric Zones Count V1
description:
- Get all Sda Fabric Zones Count V1.
- Returns the count of fabric zones that match the provided query parameters.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for SDA GetFabricZoneCountV1
  description: Complete reference of the GetFabricZoneCountV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-fabric-zone-count
notes:
  - SDK Method used are
    sda.Sda.get_fabric_zone_count_v1,

  - Paths used are
    get /dna/intent/api/v1/sda/fabricZones/count,

"""

EXAMPLES = r"""
- name: Get all Sda Fabric Zones Count V1
  cisco.catalystcenter.sda_fabric_zones_count_v1_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "count": 0
      },
      "version": "string"
    }
"""
