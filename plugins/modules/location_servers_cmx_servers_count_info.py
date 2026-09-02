#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: location_servers_cmx_servers_count_info
short_description: Information module for Location Servers Cmx Servers Count
description:
  - Get all Location Servers Cmx Servers Count.
  - Gets the count of CMX Servers.
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
  connectionAddress:
    description:
      - ConnectionAddress query parameter. The CMX Server connection address.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for System Settings CountsCMXServerSettings
    description: Complete reference of the CountsCMXServerSettings API.
    link: https://developer.cisco.com/docs/dna-center/#!counts-cmx-server-settings
notes:
  - SDK Method used are
    system_settings.SystemSettings.counts_cmx_server_settings,
  - Paths used are
    get /dna/intent/api/v1/locationServers/cmxServers/count,
"""

EXAMPLES = r"""
---
- name: Get all Location Servers Cmx Servers Count
  cisco.catalystcenter.location_servers_cmx_servers_count_info:
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
    connectionAddress: string
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
