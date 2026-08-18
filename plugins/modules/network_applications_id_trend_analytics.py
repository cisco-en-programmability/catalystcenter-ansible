#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_applications_id_trend_analytics
short_description: Resource module for Network Applications Id Trend Analytics
description:
  - Manage operation create of the resource Network Applications Id Trend Analytics.
  - Retrieves the trend analytics of applications experience data to specific.
version_added: '2.2.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  aggregateAttributes:
    description: Network Applications Id Trend Analytics's aggregateAttributes.
    elements: dict
    suboptions:
      function:
        description: Network Applications Id Trend Analytics's function.
        type: str
      name:
        description: Network Applications Id Trend Analytics's name.
        type: str
    type: list
  attributes:
    description: Network Applications Id Trend Analytics's attributes.
    elements: str
    type: list
  endTime:
    description: Network Applications Id Trend Analytics's endTime.
    type: int
  filters:
    description: Network Applications Id Trend Analytics's filters.
    elements: dict
    suboptions:
      key:
        description: Network Applications Id Trend Analytics's key.
        type: str
      operator:
        description: Network Applications Id Trend Analytics's operator.
        type: str
      value:
        description: Network Applications Id Trend Analytics's value.
        type: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  id:
    description: Id path parameter. Id is the network application name.
    type: str
  page:
    description: Network Applications Id Trend Analytics's page.
    suboptions:
      cursor:
        description: Network Applications Id Trend Analytics's cursor.
        type: str
      limit:
        description: Network Applications Id Trend Analytics's limit.
        type: int
      timeSortOrder:
        description: Network Applications Id Trend Analytics's timeSortOrder.
        type: str
    type: dict
  siteIds:
    description: Network Applications Id Trend Analytics's siteIds.
    elements: str
    type: list
  startTime:
    description: Network Applications Id Trend Analytics's startTime.
    type: int
  trendInterval:
    description: Network Applications Id Trend Analytics's trendInterval.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Applications RetrievesTheTrendAnalyticsRelatedToSpecificNetworkApplication
    description: Complete reference of the RetrievesTheTrendAnalyticsRelatedToSpecificNetworkApplication API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-trend-analytics-related-to-specific-network-application
notes:
  - SDK Method used are
    applications.Applications.retrieves_the_trend_analytics_related_to_specific_network_application,
  - Paths used are
    post /dna/data/api/v1/networkApplications/{id}/trendAnalytics,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.network_applications_id_trend_analytics:
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
        value: string
    headers: '{{my_headers | from_json}}'
    id: string
    page:
      cursor: string
      limit: 0
      timeSortOrder: string
    siteIds:
      - string
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
