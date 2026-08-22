#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: traffic_steering_contracts_top_n_analytics_info
short_description: Information module for Traffic Steering Contracts Top N Analytics
description:
  - Get all Traffic Steering Contracts Top N Analytics. - > This API retrieves the top traffic steering contracts used by
    policies across network switches and firewalls. These contracts define the rules and conditions for managing network traffic,
    ensuring data flows efficiently and securely in accordance with organizational policies. By analyzing the usage of these
    contracts, the API provides valuable insights into how they are employed to optimize network performance and maintain
    security.
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
      - Limit query parameter. The number of top records to retrieve.
    type: int
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
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
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Security RetrievesTheTopNAnalyticsDataRelatedToContracts
    description: Complete reference of the RetrievesTheTopNAnalyticsDataRelatedToContracts API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-top-n-analytics-data-related-to-contracts
notes:
  - SDK Method used are
    security.Security.retrieves_the_top_n_analytics_data_related_to_contracts,
  - Paths used are
    get /dna/data/api/v1/trafficSteeringContracts/topNAnalytics,
"""

EXAMPLES = r"""
---
- name: Get all Traffic Steering Contracts Top N Analytics
  cisco.catalystcenter.traffic_steering_contracts_top_n_analytics_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    limit: 5
    offset: 1
    sortBy: policyCount
    order: desc
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
        {
          "id": "string",
          "name": "string",
          "policyCount": 0
        }
      ],
      "version": "string"
    }
"""
