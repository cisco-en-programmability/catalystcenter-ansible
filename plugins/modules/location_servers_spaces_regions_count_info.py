#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: location_servers_spaces_regions_count_info
short_description: Information module for Location Servers Spaces Regions Count
description:
  - Get all Location Servers Spaces Regions Count. - > Gets the number of supported Cisco Spaces regions, which can be used
    when activating a new Cisco Spaces account. This is a pass-through to Cisco Spaces API, and the result could dynamically
    change.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for System Settings CountsCiscoSpacesRegions
    description: Complete reference of the CountsCiscoSpacesRegions API.
    link: https://developer.cisco.com/docs/dna-center/#!counts-cisco-spaces-regions
notes:
  - SDK Method used are
    system_settings.SystemSettings.counts_cisco_spaces_regions,
  - Paths used are
    get /dna/intent/api/v1/locationServers/spaces/regions/count,
"""

EXAMPLES = r"""
---
- name: Get all Location Servers Spaces Regions Count
  cisco.catalystcenter.location_servers_spaces_regions_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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
