#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: clients_trend_analytics
short_description: Resource module for Clients Trend Analytics
description:
  - Manage operation create of the resource Clients Trend Analytics.
  - Retrieves the trend analytics of client data for the specified time range. The.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  aggregateAttributes:
    description: Clients Trend Analytics's aggregateAttributes.
    elements: dict
    suboptions:
      function:
        description: Clients Trend Analytics's function.
        type: str
      name:
        description: Clients Trend Analytics's name.
        type: str
    type: list
  attributes:
    description: Clients Trend Analytics's attributes.
    elements: str
    type: list
  endTime:
    description: Clients Trend Analytics's endTime.
    type: int
  filters:
    description: Clients Trend Analytics's filters.
    elements: dict
    suboptions:
      key:
        description: Clients Trend Analytics's key.
        type: str
      operator:
        description: Clients Trend Analytics's operator.
        type: str
      value:
        description: Clients Trend Analytics's value.
        type: int
    type: list
  groupBy:
    description: Clients Trend Analytics's groupBy.
    elements: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  page:
    description: Clients Trend Analytics's page.
    suboptions:
      cursor:
        description: Clients Trend Analytics's cursor.
        type: str
      limit:
        description: Clients Trend Analytics's limit.
        type: int
      timeSortOrder:
        description: Clients Trend Analytics's timeSortOrder.
        type: str
    type: dict
  startTime:
    description: Clients Trend Analytics's startTime.
    type: int
  trendInterval:
    description: Clients Trend Analytics's trendInterval.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Clients RetrievesTheTrendAnalyticsDataRelatedToClients
    description: Complete reference of the RetrievesTheTrendAnalyticsDataRelatedToClients API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-trend-analytics-data-related-to-clients
notes:
  - SDK Method used are
    clients.Clients.retrieves_the_trend_analytics_data_related_to_clients,
  - Paths used are
    post /dna/data/api/v1/clients/trendAnalytics,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.clients_trend_analytics:
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
      timeSortOrder: string
    startTime: 0
    trendInterval: string
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
          "timestamp": 0,
          "groups": [
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
          ]
        }
      ],
      "page": {
        "limit": 0,
        "cursor": "string",
        "count": 0,
        "timeSortOrder": "string"
      },
      "version": "string"
    }
"""
