#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_fabric_sites_count_info
short_description: Information module for Sda Fabric
  Sites Count
description:
  - Get all Sda Fabric Sites Count.
  - Returns the count of fabric sites that match the
    provided query parameters.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA GetFabricSiteCount
    description: Complete reference of the GetFabricSiteCount
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-fabric-site-count
notes:
  - SDK Method used are
    sda.Sda.get_fabric_site_count,
  - Paths used are
    get /dna/intent/api/v1/sda/fabricSites/count,
"""

EXAMPLES = r"""
---
- name: Get all Sda Fabric Sites Count
  cisco.catalystcenter.sda_fabric_sites_count_info:
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
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
