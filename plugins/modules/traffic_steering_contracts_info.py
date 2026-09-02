#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: traffic_steering_contracts_info
short_description: Information module for Traffic Steering Contracts
description:
  - Get all Traffic Steering Contracts.
  - Get Traffic Steering Contracts by id.
  - This API fetches a steering contract using a given id. The API supports views to fetch only the required fields. - > This
    API fetches a list of steering contracts. The response data can be sorted by `name`, `creationTime`, or `lastUpdatedTime`.
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
      - Id path parameter. The ID of the steering contract to retrieve.
    type: str
  views:
    description:
      - >
        Views query parameter. The specific views being requested. This is an optional parameter which can be
        passed. If this is not provided, then it will default to `DETAILED` views. Attributes covered by the
        views are * `BASIC` id, description, name, policyReferenceCount, ruleCount, siteReferenceCount, version.
        * `DETAILED` id, description, name, policyReferenceCount, ruleCount, siteReferenceCount, rules,
        createdTime, lastUpdatedTime, version.
    type: str
  name:
    description:
      - Name query parameter. A property to filter the response by contract name.
    type: str
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: int
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
  sortBy:
    description:
      - SortBy query parameter. A property within the response to sortby.
    type: str
  order:
    description:
      - Order query parameter. Whether ascending or descending order should be used to sort the response.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Security RetrieveATrafficSteeringContractByItsID
    description: Complete reference of the RetrieveATrafficSteeringContractByItsID API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-a-traffic-steering-contract-by-its-id
  - name: Cisco Catalyst Center documentation for Security RetrieveTrafficSteeringContracts
    description: Complete reference of the RetrieveTrafficSteeringContracts API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-traffic-steering-contracts
notes:
  - SDK Method used are
    security.Security.retrieve_a_traffic_steering_contract_by_its_id,
    security.Security.retrieve_traffic_steering_contracts,
  - Paths used are
    get /dna/intent/api/v1/trafficSteeringContracts,
    get /dna/intent/api/v1/trafficSteeringContracts/{id},
"""

EXAMPLES = r"""
---
- name: Get all Traffic Steering Contracts
  cisco.catalystcenter.traffic_steering_contracts_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    views: DETAILED
    name: IP_Access_Redirect_Contract
    limit: 0
    offset: 1
    sortBy: lastUpdatedTime
    order: asc
  register: result
- name: Get Traffic Steering Contracts by id
  cisco.catalystcenter.traffic_steering_contracts_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    views: DETAILED
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
        "description": "string",
        "policyReferenceCount": 0,
        "ruleCount": 0,
        "siteReferenceCount": 0,
        "rules": [
          {
            "applicationName": "string",
            "logging": true,
            "destinationNetworkIdentities": {},
            "sourceNetworkIdentities": {}
          }
        ],
        "createdTime": 0,
        "lastUpdatedTime": 0
      },
      "version": "string"
    }
"""
