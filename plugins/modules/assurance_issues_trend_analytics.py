#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: assurance_issues_trend_analytics
short_description: Resource module for Assurance Issues Trend Analytics
description:
  - Manage operation create of the resource Assurance Issues Trend Analytics.
  - Gets the trend analytics data related to issues based on given filters and.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  aggregateAttributes:
    description: Assurance Issues Trend Analytics's aggregateAttributes.
    elements: dict
    suboptions:
      function:
        description: Assurance Issues Trend Analytics's function.
        type: str
      name:
        description: Assurance Issues Trend Analytics's name.
        type: str
    type: list
  attributes:
    description: Assurance Issues Trend Analytics's attributes.
    elements: str
    type: list
  endTime:
    description: Assurance Issues Trend Analytics's endTime.
    type: int
  filters:
    description: Assurance Issues Trend Analytics's filters.
    elements: dict
    suboptions:
      key:
        description: Assurance Issues Trend Analytics's key.
        type: str
      operator:
        description: Assurance Issues Trend Analytics's operator.
        type: str
      value:
        description: Assurance Issues Trend Analytics's value.
        type: str
    type: list
  groupBy:
    description: Assurance Issues Trend Analytics's groupBy.
    elements: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  page:
    description: Assurance Issues Trend Analytics's page.
    suboptions:
      limit:
        description: Assurance Issues Trend Analytics's limit.
        type: int
      offset:
        description: Assurance Issues Trend Analytics's offset.
        type: int
      timestampOrder:
        description: Assurance Issues Trend Analytics's timestampOrder.
        type: str
    type: dict
  startTime:
    description: Assurance Issues Trend Analytics's startTime.
    type: int
  trendInterval:
    description: Assurance Issues Trend Analytics's trendInterval.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Issues GetTrendAnalyticsDataOfIssues
    description: Complete reference of the GetTrendAnalyticsDataOfIssues API.
    link: https://developer.cisco.com/docs/dna-center/#!get-trend-analytics-data-of-issues
notes:
  - SDK Method used are
    issues.Issues.get_trend_analytics_data_of_issues,
  - Paths used are
    post /dna/data/api/v1/assuranceIssues/trendAnalytics,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.assurance_issues_trend_analytics:
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
    groupBy:
      - string
    headers: '{{my_headers | from_json}}'
    page:
      limit: 0
      offset: 0
      timestampOrder: string
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
      "version": "string",
      "response": [
        {
          "timestamp": 0,
          "groups": [
            {
              "id": "string",
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
        "offset": 0,
        "count": 0,
        "timestampOrder": "string"
      }
    }
"""
