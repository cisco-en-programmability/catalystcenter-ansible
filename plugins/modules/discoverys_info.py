#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: discoverys_info
short_description: Information module for Discoverys
description:
  - Get all Discoverys.
  - Get Discoverys by id.
  - API to fetch the discovery details using basic filters.
  - API to get discovery details for the given discovery id.
version_added: '2.3.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id query parameter. Optional list of the discovery ids to filter by.
    elements: str
    type: list
  name:
    description:
      - >
        Name query parameter. Optional name of the discovery to filter by. This supports partial search. For
        example, searching for "Disc" will match "Discovery1", "Discovery2", etc.
    type: str
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: int
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices FetchesAllDiscoveryDetails
    description: Complete reference of the FetchesAllDiscoveryDetails API.
    link: https://developer.cisco.com/docs/dna-center/#!fetches-all-discovery-details
  - name: Cisco Catalyst Center documentation for Devices FetchesDiscoveryDetailsById
    description: Complete reference of the FetchesDiscoveryDetailsById API.
    link: https://developer.cisco.com/docs/dna-center/#!fetches-discovery-details-by-id
notes:
  - SDK Method used are
    devices.Devices.fetches_all_discovery_details,
    devices.Devices.fetches_discovery_details_by_id,
  - Paths used are
    get /dna/intent/api/v1/discoverys,
    get /dna/intent/api/v1/discoverys/{id},
"""

EXAMPLES = r"""
---
- name: Get all Discoverys
  cisco.catalystcenter.discoverys_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: [1, 2]
    name: string
    limit: 0
    offset: 1
  register: result
- name: Get Discoverys by id
  cisco.catalystcenter.discoverys_info:
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
      "response": {
        "id": "string",
        "name": "string",
        "managementIpSelectionMethod": "string",
        "discoveryTypeDetails": {},
        "onlyNewDevice": true,
        "updateManagementIp": true,
        "credentials": {
          "cli": {},
          "snmp": {},
          "httpRead": {},
          "httpWrite": {},
          "netconf": {}
        },
        "siteId": "string"
      },
      "version": "string"
    }
"""
