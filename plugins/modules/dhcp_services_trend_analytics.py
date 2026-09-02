#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: dhcp_services_trend_analytics
short_description: Resource module for Dhcp Services Trend Analytics
description:
  - Manage operation create of the resource Dhcp Services Trend Analytics.
  - Gets the trend analytics data related to DHCP Services based on given filters.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  aggregateAttributes:
    description: Dhcp Services Trend Analytics's aggregateAttributes.
    elements: dict
    suboptions:
      function:
        description: Dhcp Services Trend Analytics's function.
        type: str
      name:
        description: Dhcp Services Trend Analytics's name.
        type: str
    type: list
  attributes:
    description: Dhcp Services Trend Analytics's attributes.
    elements: str
    type: list
  endTime:
    description: Dhcp Services Trend Analytics's endTime.
    type: int
  filters:
    description: Dhcp Services Trend Analytics's filters.
    elements: dict
    suboptions:
      filters:
        description: Dhcp Services Trend Analytics's filters.
        elements: str
        type: list
      key:
        description: Dhcp Services Trend Analytics's key.
        type: str
      logicalOperator:
        description: Dhcp Services Trend Analytics's logicalOperator.
        type: str
      operator:
        description: Dhcp Services Trend Analytics's operator.
        type: str
      value:
        description: Dhcp Services Trend Analytics's value.
        type: dict
    type: list
  groupBy:
    description: Dhcp Services Trend Analytics's groupBy.
    elements: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  page:
    description: Dhcp Services Trend Analytics's page.
    suboptions:
      limit:
        description: Dhcp Services Trend Analytics's limit.
        type: int
      offset:
        description: Dhcp Services Trend Analytics's offset.
        type: int
      timestampOrder:
        description: Dhcp Services Trend Analytics's timestampOrder.
        type: str
    type: dict
  startTime:
    description: Dhcp Services Trend Analytics's startTime.
    type: int
  trendInterval:
    description: Dhcp Services Trend Analytics's trendInterval.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices GetTrendAnalyticsDataOfDHCPServicesForGivenSetOfComplexFilters
    description: Complete reference of the GetTrendAnalyticsDataOfDHCPServicesForGivenSetOfComplexFilters API.
    link: https://developer.cisco.com/docs/dna-center/#!get-trend-analytics-data-of-dhcp-services-for-given-set-of-complex-filters
notes:
  - SDK Method used are
    devices.Devices.get_trend_analytics_data_of_dhcp_services_for_given_set_of_complex_filters,
  - Paths used are
    post /dna/data/api/v1/dhcpServices/trendAnalytics,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.dhcp_services_trend_analytics:
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
          - string
        key: string
        logicalOperator: string
        operator: string
        value: {}
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
