#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: clients_summary_analytics
short_description: Resource module for Clients Summary Analytics
description:
  - Manage operation create of the resource Clients Summary Analytics.
  - Retrieves summary analytics data related to clients while applying complex.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  aggregateAttributes:
    description: Clients Summary Analytics's aggregateAttributes.
    elements: dict
    suboptions:
      function:
        description: Clients Summary Analytics's function.
        type: str
      name:
        description: Clients Summary Analytics's name.
        type: str
    type: list
  attributes:
    description: Clients Summary Analytics's attributes.
    elements: str
    type: list
  endTime:
    description: Clients Summary Analytics's endTime.
    type: int
  filters:
    description: Clients Summary Analytics's filters.
    elements: dict
    suboptions:
      key:
        description: Clients Summary Analytics's key.
        type: str
      operator:
        description: Clients Summary Analytics's operator.
        type: str
      value:
        description: Clients Summary Analytics's value.
        type: int
    type: list
  groupBy:
    description: Clients Summary Analytics's groupBy.
    elements: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  page:
    description: Clients Summary Analytics's page.
    suboptions:
      cursor:
        description: Clients Summary Analytics's cursor.
        type: str
      limit:
        description: Clients Summary Analytics's limit.
        type: int
      sortBy:
        description: Clients Summary Analytics's sortBy.
        elements: dict
        suboptions:
          name:
            description: Clients Summary Analytics's name.
            type: str
          order:
            description: Clients Summary Analytics's order.
            type: str
        type: list
    type: dict
  startTime:
    description: Clients Summary Analytics's startTime.
    type: int
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Clients RetrievesSummaryAnalyticsDataRelatedToClients
    description: Complete reference of the RetrievesSummaryAnalyticsDataRelatedToClients API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-summary-analytics-data-related-to-clients
notes:
  - SDK Method used are
    clients.Clients.retrieves_summary_analytics_data_related_to_clients,
  - Paths used are
    post /dna/data/api/v1/clients/summaryAnalytics,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.clients_summary_analytics:
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
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
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
      },
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
