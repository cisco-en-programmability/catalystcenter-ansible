#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: excluded_wireless_clients_info
short_description: Information module for Excluded Wireless Clients
description:
  - Get all Excluded Wireless Clients.
  - Get Excluded Wireless Clients by id. - > This API allows user to retrieve details of a specific excluded wireless client
    by ID. This API allows user to retrieve details of a specific excluded wireless client by ID. - > This API allows user
    to retrieve information about all excluded wireless clients. This API allows user to retrieve information about all excluded
    wireless clients. Results can be filtered and paginated.
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
      - Id path parameter. ID of the excluded wireless client to be retrieved.
    type: str
  macAddress:
    description:
      - MacAddress query parameter. Filter results by MAC address.
    type: str
  networkDeviceId:
    description:
      - NetworkDeviceId query parameter. Filter results by Network Device ID.
    type: str
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: int
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless GetAllExcludedClients
    description: Complete reference of the GetAllExcludedClients API.
    link: https://developer.cisco.com/docs/dna-center/#!get-all-excluded-clients
  - name: Cisco Catalyst Center documentation for Wireless GetExcludedClientByID
    description: Complete reference of the GetExcludedClientByID API.
    link: https://developer.cisco.com/docs/dna-center/#!get-excluded-client-by-id
notes:
  - SDK Method used are
    wireless.Wireless.get_all_excluded_clients,
    wireless.Wireless.get_excluded_client_by_id,
  - Paths used are
    get /dna/intent/api/v1/excludedWirelessClients,
    get /dna/intent/api/v1/excludedWirelessClients/{id},
"""

EXAMPLES = r"""
---
- name: Get all Excluded Wireless Clients
  cisco.catalystcenter.excluded_wireless_clients_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    macAddress: string
    networkDeviceId: string
    offset: 1
    limit: 500
  register: result
- name: Get Excluded Wireless Clients by id
  cisco.catalystcenter.excluded_wireless_clients_info:
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
        "macAddress": "string",
        "description": "string",
        "impactedWlcs": [
          "string"
        ]
      },
      "version": "string"
    }
"""
