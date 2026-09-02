#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: clients_top_n_analytics
short_description: Resource module for Clients Top N Analytics
description:
  - Manage operation create of the resource Clients Top N Analytics.
  - Retrieves the top N analytics data related to clients based on the provided.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  aggregateAttributes:
    description: Clients Top N Analytics's aggregateAttributes.
    elements: dict
    suboptions:
      function:
        description: Clients Top N Analytics's function.
        type: str
      name:
        description: Clients Top N Analytics's name.
        type: str
    type: list
  attributes:
    description: Clients Top N Analytics's attributes.
    elements: str
    type: list
  endTime:
    description: Clients Top N Analytics's endTime.
    type: int
  filters:
    description: Clients Top N Analytics's filters.
    elements: dict
    suboptions:
      key:
        description: Clients Top N Analytics's key.
        type: str
      operator:
        description: Clients Top N Analytics's operator.
        type: str
      value:
        description: Clients Top N Analytics's value.
        type: int
    type: list
  groupBy:
    description: Clients Top N Analytics's groupBy.
    elements: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  page:
    description: Clients Top N Analytics's page.
    suboptions:
      cursor:
        description: Clients Top N Analytics's cursor.
        type: str
      limit:
        description: Clients Top N Analytics's limit.
        type: int
      sortBy:
        description: Clients Top N Analytics's sortBy.
        elements: dict
        suboptions:
          name:
            description: Clients Top N Analytics's name.
            type: str
          order:
            description: Clients Top N Analytics's order.
            type: str
        type: list
    type: dict
  startTime:
    description: Clients Top N Analytics's startTime.
    type: int
  topN:
    description: Clients Top N Analytics's topN.
    type: int
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Clients RetrievesTheTopNAnalyticsDataRelatedToClients
    description: Complete reference of the RetrievesTheTopNAnalyticsDataRelatedToClients API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-top-n-analytics-data-related-to-clients
notes:
  - SDK Method used are
    clients.Clients.retrieves_the_top_n_analytics_data_related_to_clients,
  - Paths used are
    post /dna/data/api/v1/clients/topNAnalytics,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.clients_top_n_analytics:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    aggregateAttributes:
      - function: string
        name: string
    attributes:
      - string
    endTime: 0
    filters:
      - key: string
        operator: string
        value: 0
    groupBy:
      - string
    headers: '{{my_headers | from_json}}'
    page:
      cursor: string
      limit: 0
      sortBy:
        - name: string
          order: string
    startTime: 0
    topN: 0
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
          "attributes": [
            {
              "name": "string",
              "value": 0
            }
          ],
          "aggregateAttributes": [
            {
              "name": "string",
              "function": "string",
              "value": 0
            }
          ]
        }
      ],
      "page": {
        "limit": 0,
        "cursor": "string",
        "count": 0,
        "sortBy": [
          {
            "name": "string",
            "order": "string"
          }
        ]
      },
      "version": "string"
    }
"""
