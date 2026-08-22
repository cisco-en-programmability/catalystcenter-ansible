#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: location_servers_spaces_accounts_count_info
short_description: Information module for Location Servers Spaces Accounts Count
description:
  - Get all Location Servers Spaces Accounts Count. - > Gets the count of existing Cisco Spaces accounts of the active registered
    Cisco.com Credential user. This is a pass-through to Cisco Spaces API, and the result could dynamically change.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  regionName:
    description:
      - RegionName query parameter. The Cisco Spaces region name to list accounts of.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for System Settings CountsCiscoSpacesAccounts
    description: Complete reference of the CountsCiscoSpacesAccounts API.
    link: https://developer.cisco.com/docs/dna-center/#!counts-cisco-spaces-accounts
notes:
  - SDK Method used are
    system_settings.SystemSettings.counts_cisco_spaces_accounts,
  - Paths used are
    get /dna/intent/api/v1/locationServers/spaces/accounts/count,
"""

EXAMPLES = r"""
---
- name: Get all Location Servers Spaces Accounts Count
  cisco.catalystcenter.location_servers_spaces_accounts_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    regionName: string
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
