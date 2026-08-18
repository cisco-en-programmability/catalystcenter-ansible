#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: global_credentials_info
short_description: Information module for Global Credentials
description:
  - Get all Global Credentials.
  - Get Global Credentials by id.
  - API to get global credentials based on the given filters.
  - API to retrieve the global credential details by its unique identifier.
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
      - Id path parameter. Unique identifier of the global credential.
    type: str
  type:
    description:
      - >
        Type query parameter. Returns global credentials for the given credential type. |Type | Description |
        |---------------|------------------------------------| | `CLI` | CLI credentials for TELNET/SSH. | |
        `SNMPV2_READ_COMMUNITY` | SNMP V2 read credentials. | | `SNMPV2_WRITE_COMMUNITY` | SNMP V2 write
        credentials. | | `SNMPV3` | SNMP V3 credentials. | | `HTTP_WRITE` | HTTP write credentials. |
        |`HTTP_READ` | HTTP read credentials. | | `NETCONF` | NETCONF port. |.
    type: str
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: int
  sortBy:
    description:
      - SortBy query parameter. A property within the response to sort by.
    type: str
  order:
    description:
      - Order query parameter. Whether ascending or descending order should be used to sort the response.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Network Settings GetDetailsOfASingleGlobalCredential
    description: Complete reference of the GetDetailsOfASingleGlobalCredential API.
    link: https://developer.cisco.com/docs/dna-center/#!get-details-of-a-single-global-credential
  - name: Cisco Catalyst Center documentation for Network Settings RetrievesGlobalCredentials
    description: Complete reference of the RetrievesGlobalCredentials API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-global-credentials
notes:
  - SDK Method used are
    network_settings.NetworkSettings.get_details_of_a_single_global_credential,
    network_settings.NetworkSettings.retrieves_global_credentials,
  - Paths used are
    get /dna/intent/api/v1/globalCredentials,
    get /dna/intent/api/v1/globalCredentials/{id},
"""

EXAMPLES = r"""
---
- name: Get all Global Credentials
  cisco.catalystcenter.global_credentials_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: ['3fa85f64-5717-4562-b3fc-2c963f66afa6', 'cfa85f64-5717-4562-b3fc-2c963f66afa6']
    type: SNMPV2_READ_COMMUNITY
    offset: 1
    limit: 500
    sortBy: id
    order: asc
  register: result
- name: Get Global Credentials by id
  cisco.catalystcenter.global_credentials_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: 3fa85f64-5717-4562-b3fc-2c963f66afa6
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {},
      "version": "string"
    }
"""
