#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_devices_trend_analytics
short_description: Resource module for Network Devices Trend Analytics
description:
  - Manage operation create of the resource Network Devices Trend Analytics.
  - Gets the Trend analytics Network device data for the given time range. The.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  aggregateAttributes:
    description: Network Devices Trend Analytics's aggregateAttributes.
    elements: str
    type: list
  attributes:
    description: Network Devices Trend Analytics's attributes.
    elements: str
    type: list
  endTime:
    description: Network Devices Trend Analytics's endTime.
    type: int
  filters:
    description: Network Devices Trend Analytics's filters.
    elements: dict
    suboptions:
      key:
        description: Network Devices Trend Analytics's key.
        type: str
      operator:
        description: Network Devices Trend Analytics's operator.
        type: str
      value:
        description: Network Devices Trend Analytics's value.
        type: str
    type: list
  groupBy:
    description: Network Devices Trend Analytics's groupBy.
    elements: str
    type: list
  page:
    description: Network Devices Trend Analytics's page.
    suboptions:
      limit:
        description: Network Devices Trend Analytics's limit.
        type: int
      offset:
        description: Network Devices Trend Analytics's offset.
        type: int
      timestampOrder:
        description: Network Devices Trend Analytics's timestampOrder.
        type: str
    type: dict
  startTime:
    description: Network Devices Trend Analytics's startTime.
    type: int
  trendInterval:
    description: Network Devices Trend Analytics's trendInterval.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices GetsTheTrendAnalyticsData
    description: Complete reference of the GetsTheTrendAnalyticsData API.
    link: https://developer.cisco.com/docs/dna-center/#!gets-the-trend-analytics-data
notes:
  - SDK Method used are
    devices.Devices.gets_the_trend_analytics_data,
  - Paths used are
    post /dna/data/api/v1/networkDevices/trendAnalytics,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.network_devices_trend_analytics:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    aggregateAttributes: []
    attributes:
      - string
    endTime: 0
    filters:
      - key: string
        operator: string
        value: string
    groupBy: []
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
          ],
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
          ]
        }
      ],
      "page": {
        "limit": 0,
        "offset": 0,
        "count": 0,
        "timestampOrder": "string"
      },
      "version": "string"
    }
"""
