#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: discoverys_count_info
short_description: Information module for Discoverys Count
description:
  - Get all Discoverys Count.
  - API to fetch the count of discoveries using basic filters.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id query parameter. Optional list of the discovery ids to filter by.
    type: str
  name:
    description:
      - >
        Name query parameter. Optional name of the discovery to filter by. This supports partial search. For
        example, searching for "Disc" will match "Discovery1", "Discovery2", etc.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Devices CountTheNumberOfDiscoveries
    description: Complete reference of the CountTheNumberOfDiscoveries API.
    link: https://developer.cisco.com/docs/dna-center/#!count-the-number-of-discoveries
notes:
  - SDK Method used are
    devices.Devices.count_the_number_of_discoveries,
  - Paths used are
    get /dna/intent/api/v1/discoverys/count,
"""

EXAMPLES = r"""
---
- name: Get all Discoverys Count
  cisco.catalystcenter.discoverys_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
    name: string
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
        "count": 0
      },
      "version": "string"
    }
"""
