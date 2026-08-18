#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: traffic_steering_nodes_top_n_analytics_info
short_description: Information module for Traffic Steering Nodes Top N Analytics
description:
  - Get all Traffic Steering Nodes Top N Analytics. - > This API retrieves the top switches data used by traffic steering
    policies across the network. It provides detailed analytics on the most utilized network nodes, focusing on switches that
    play a critical role in managing and directing network traffic. By accessing this data, network administrators can gain
    valuable insights into network performance and usage patterns. This information is essential for optimizing network operations,
    identifying potential bottlenecks, and ensuring efficient traffic flow. The API supports strategic planning and resource
    allocation by highlighting which switches are most actively involved in traffic management.
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
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Security RetrievesTheTopNAnalyticsDataRelatedToNodes
    description: Complete reference of the RetrievesTheTopNAnalyticsDataRelatedToNodes API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-top-n-analytics-data-related-to-nodes
notes:
  - SDK Method used are
    security.Security.retrieves_the_top_n_analytics_data_related_to_nodes,
  - Paths used are
    get /dna/data/api/v1/trafficSteeringNodes/topNAnalytics,
"""

EXAMPLES = r"""
---
- name: Get all Traffic Steering Nodes Top N Analytics
  cisco.catalystcenter.traffic_steering_nodes_top_n_analytics_info:
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
