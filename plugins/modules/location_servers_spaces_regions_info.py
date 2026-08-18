#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: location_servers_spaces_regions_info
short_description: Information module for Location Servers Spaces Regions
description:
  - Get all Location Servers Spaces Regions. - > Gets the list of supported Cisco Spaces regions, which can be used when activating
    a new Cisco Spaces account. This is a pass-through to Cisco Spaces API, and the result could dynamically change.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: int
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
  order:
    description:
      - Order query parameter. Whether ascending or descending order should be used to sort the response.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for System Settings RetrievesCiscoSpacesRegions
    description: Complete reference of the RetrievesCiscoSpacesRegions API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-cisco-spaces-regions
notes:
  - SDK Method used are
    system_settings.SystemSettings.retrieves_cisco_spaces_regions,
  - Paths used are
    get /dna/intent/api/v1/locationServers/spaces/regions,
"""

EXAMPLES = r"""
---
- name: Get all Location Servers Spaces Regions
  cisco.catalystcenter.location_servers_spaces_regions_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    limit: 0
    offset: 1
    order: asc
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
        "string"
      ],
      "version": "string"
    }
"""
