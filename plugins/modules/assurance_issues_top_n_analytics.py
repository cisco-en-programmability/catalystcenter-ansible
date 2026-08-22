#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: assurance_issues_top_n_analytics
short_description: Resource module for Assurance Issues Top N Analytics
description:
  - Manage operation create of the resource Assurance Issues Top N Analytics.
  - Gets the Top N analytics data related to issues based on given filters and.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  aggregateAttributes:
    description: Assurance Issues Top N Analytics's aggregateAttributes.
    elements: dict
    suboptions:
      function:
        description: Assurance Issues Top N Analytics's function.
        type: str
      name:
        description: Assurance Issues Top N Analytics's name.
        type: str
    type: list
  attributes:
    description: Assurance Issues Top N Analytics's attributes.
    elements: str
    type: list
  endTime:
    description: Assurance Issues Top N Analytics's endTime.
    type: int
  filters:
    description: Assurance Issues Top N Analytics's filters.
    elements: dict
    suboptions:
      filters:
        description: Assurance Issues Top N Analytics's filters.
        elements: dict
        suboptions:
          key:
            description: Assurance Issues Top N Analytics's key.
            type: str
          operator:
            description: Assurance Issues Top N Analytics's operator.
            type: str
          value:
            description: Assurance Issues Top N Analytics's value.
            type: str
        type: list
      key:
        description: Assurance Issues Top N Analytics's key.
        type: str
      logicalOperator:
        description: Assurance Issues Top N Analytics's logicalOperator.
        type: str
      operator:
        description: Assurance Issues Top N Analytics's operator.
        type: str
      value:
        description: Assurance Issues Top N Analytics's value.
        type: str
    type: list
  groupBy:
    description: Assurance Issues Top N Analytics's groupBy.
    elements: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  page:
    description: Assurance Issues Top N Analytics's page.
    suboptions:
      limit:
        description: Assurance Issues Top N Analytics's limit.
        type: int
      offset:
        description: Assurance Issues Top N Analytics's offset.
        type: int
      sortBy:
        description: Assurance Issues Top N Analytics's sortBy.
        elements: dict
        suboptions:
          name:
            description: Assurance Issues Top N Analytics's name.
            type: str
          order:
            description: Assurance Issues Top N Analytics's order.
            type: str
        type: list
    type: dict
  startTime:
    description: Assurance Issues Top N Analytics's startTime.
    type: int
  topN:
    description: Assurance Issues Top N Analytics's topN.
    type: int
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Issues GetTopNAnalyticsDataOfIssues
    description: Complete reference of the GetTopNAnalyticsDataOfIssues API.
    link: https://developer.cisco.com/docs/dna-center/#!get-top-n-analytics-data-of-issues
notes:
  - SDK Method used are
    issues.Issues.get_top_n_analytics_data_of_issues,
  - Paths used are
    post /dna/data/api/v1/assuranceIssues/topNAnalytics,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.assurance_issues_top_n_analytics:
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
      - filters:
          - key: string
            operator: string
            value: string
        key: string
        logicalOperator: string
        operator: string
        value: string
    groupBy:
      - string
    headers: '{{my_headers | from_json}}'
    page:
      limit: 0
      offset: 0
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
      "version": "string",
      "response": [
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
      "page": {
        "limit": 0,
        "offset": 0,
        "count": 0,
        "sortBy": [
          {
            "name": "string",
            "function": {},
            "order": "string"
          }
        ]
      }
    }
"""
