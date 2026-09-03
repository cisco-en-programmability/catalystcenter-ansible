#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_applications_summary_analytics
short_description: Resource module for Network Applications Summary Analytics
description:
  - Manage operation create of the resource Network Applications Summary Analytics.
  - Retrieves summary analytics data related to network applications while.
version_added: '2.2.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  aggregateAttributes:
    description: Network Applications Summary Analytics's aggregateAttributes.
    elements: dict
    suboptions:
      function:
        description: Network Applications Summary Analytics's function.
        type: str
      name:
        description: Network Applications Summary Analytics's name.
        type: str
    type: list
  attributes:
    description: Network Applications Summary Analytics's attributes.
    elements: str
    type: list
  endTime:
    description: Network Applications Summary Analytics's endTime.
    type: int
  filters:
    description: Network Applications Summary Analytics's filters.
    elements: dict
    suboptions:
      key:
        description: Network Applications Summary Analytics's key.
        type: str
      operator:
        description: Network Applications Summary Analytics's operator.
        type: str
      value:
        description: Network Applications Summary Analytics's value.
        type: int
    type: list
  headers:
    description: Additional headers.
    type: dict
  page:
    description: Network Applications Summary Analytics's page.
    suboptions:
      cursor:
        description: Network Applications Summary Analytics's cursor.
        type: str
      limit:
        description: Network Applications Summary Analytics's limit.
        type: int
      offset:
        description: Network Applications Summary Analytics's offset.
        type: int
      sortBy:
        description: Network Applications Summary Analytics's sortBy.
        elements: dict
        suboptions:
          function:
            description: Network Applications Summary Analytics's function.
            type: str
          name:
            description: Network Applications Summary Analytics's name.
            type: str
          order:
            description: Network Applications Summary Analytics's order.
            type: str
        type: list
    type: dict
  siteIds:
    description: Network Applications Summary Analytics's siteIds.
    elements: str
    type: list
  startTime:
    description: Network Applications Summary Analytics's startTime.
    type: int
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Applications RetrievesSummaryAnalyticsDataRelatedToNetworkApplicationsAlongWithHealthMetrics
    description: Complete reference of the RetrievesSummaryAnalyticsDataRelatedToNetworkApplicationsAlongWithHealthMetrics
      API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-summary-analytics-data-related-to-network-applications-along-with-health-metrics
notes:
  - SDK Method used are
    applications.Applications.retrieves_summary_analytics_data_related_to_network_applications_along_with_health_metrics,
  - Paths used are
    post /dna/data/api/v1/networkApplications/summaryAnalytics,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.network_applications_summary_analytics:
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
    headers: '{{my_headers | from_json}}'
    page:
      cursor: string
      limit: 0
      offset: 0
      sortBy:
        - function: string
          name: string
          order: string
    siteIds:
      - string
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
        "attributes": [
          {
            "name": "string",
            "value": "string"
          }
        ],
        "aggregateAttributes": [
          {
            "name": "string",
            "function": "string",
            "value": 0
          }
        ]
      },
      "page": {
        "limit": 0,
        "offset": 0,
        "cursor": "string",
        "sortBy": [
          {
            "name": "string",
            "function": "string",
            "order": "string"
          }
        ]
      },
      "version": "string"
    }
"""
