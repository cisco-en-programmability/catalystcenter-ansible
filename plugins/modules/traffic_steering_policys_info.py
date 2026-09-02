#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: traffic_steering_policys_info
short_description: Information module for Traffic Steering Policys
description:
  - Get all Traffic Steering Policys.
  - Get Traffic Steering Policys by id.
  - This API fetches a steering policy using a given id. - > This API retrieves the list of steering policies. The response
    data can be sorted by the time the instance was created or updated.
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
      - Id path parameter. The ID of the steering policy to retrieve.
    type: str
  views:
    description:
      - >
        Views query parameter. The specific views being requested. This is an optional parameter which can be
        passed. If this is not provided, then it will default to `DETAILED` views. Attributes covered by the
        views are * `BASIC` id, contractName, destinationName, sourceName, virtualNetworkFirewallCount, version.
        * `DETAILED` id, contractId, contractName, createdTime, destinationName, destinationId, siteId,
        sourceId, sourceName, lastUpdatedTime, virtualNetworkFirewallCount, virtualNetworkFirewall, version.".
    type: str
  siteId:
    description:
      - SiteId query parameter. A property to filter the response by the site ID.
    type: str
  sourceName:
    description:
      - SourceName query parameter. A property to filter the response by the sourceName.
    type: str
  destinationName:
    description:
      - DestinationName query parameter. A property to filter the response by the destinationName.
    type: str
  contractName:
    description:
      - ContractName query parameter. A property to filter the response by the contractName.
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
  - name: Cisco Catalyst Center documentation for Security RetrieveATrafficSteeringPolicy
    description: Complete reference of the RetrieveATrafficSteeringPolicy API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-a-traffic-steering-policy
  - name: Cisco Catalyst Center documentation for Security RetrieveTrafficSteeringPolicies
    description: Complete reference of the RetrieveTrafficSteeringPolicies API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-traffic-steering-policies
notes:
  - SDK Method used are
    security.Security.retrieve_a_traffic_steering_policy,
    security.Security.retrieve_traffic_steering_policies,
  - Paths used are
    get /dna/intent/api/v1/trafficSteeringPolicys,
    get /dna/intent/api/v1/trafficSteeringPolicys/{id},
"""

EXAMPLES = r"""
---
- name: Get all Traffic Steering Policys
  cisco.catalystcenter.traffic_steering_policys_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    views: DETAILED
    siteId: bdfd311b-3ff5-4b7a-82c3-1d50bbd218b4
    sourceName: Extranet
    destinationName: Intranet
    contractName: IP_Access_Redirect_Contract
    limit: 0
    offset: 1
    sortBy: lastUpdatedTime
    order: asc
  register: result
- name: Get Traffic Steering Policys by id
  cisco.catalystcenter.traffic_steering_policys_info:
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
        "contractId": "string",
        "contractName": "string",
        "createdTime": 0,
        "destinationId": "string",
        "destinationName": "string",
        "lastUpdatedTime": 0,
        "siteId": "string",
        "sourceId": "string",
        "sourceName": "string",
        "virtualNetworkFirewall": [
          {
            "firewallIpAddress": "string",
            "subnetMask": 0,
            "firewallName": "string",
            "virtualNetworkName": "string",
            "virtualNetworkId": 0
          }
        ],
        "virtualNetworkFirewallCount": 0
      },
      "version": "string"
    }
"""
