#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_devices_trend_analytics_id
short_description: Resource module for Network Devices Trend Analytics Id
description:
  - Manage operation create of the resource Network Devices Trend Analytics Id.
  - The Trend analytics data for the network Device in the specified time range.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  aggregateAttributes:
    description: Network Devices Trend Analytics Id's aggregateAttributes.
    elements: dict
    suboptions:
      function:
        description: Network Devices Trend Analytics Id's function.
        type: str
      name:
        description: Network Devices Trend Analytics Id's name.
        type: str
    type: list
  attributes:
    description: Network Devices Trend Analytics Id's attributes.
    elements: str
    type: list
  endTime:
    description: Network Devices Trend Analytics Id's endTime.
    type: int
  filters:
    description: Network Devices Trend Analytics Id's filters.
    elements: dict
    suboptions:
      filters:
        description: Network Devices Trend Analytics Id's filters.
        elements: str
        type: list
      key:
        description: Network Devices Trend Analytics Id's key.
        type: str
      logicalOperator:
        description: Network Devices Trend Analytics Id's logicalOperator.
        type: str
      operator:
        description: Network Devices Trend Analytics Id's operator.
        type: str
      value:
        description: Network Devices Trend Analytics Id's value.
        type: dict
    type: list
  groupBy:
    description: Network Devices Trend Analytics Id's groupBy.
    elements: str
    type: list
  id:
    description: Id path parameter. The device Uuid.
    type: str
  page:
    description: Network Devices Trend Analytics Id's page.
    suboptions:
      limit:
        description: Network Devices Trend Analytics Id's limit.
        type: int
      offset:
        description: Network Devices Trend Analytics Id's offset.
        type: int
      timestampOrder:
        description: Network Devices Trend Analytics Id's timestampOrder.
        type: str
    type: dict
  startTime:
    description: Network Devices Trend Analytics Id's startTime.
    type: int
  trendIntervalInMinutes:
    description: Network Devices Trend Analytics Id's trendIntervalInMinutes.
    type: int
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices TheTrendAnalyticsDataForTheNetworkDeviceInTheSpecifiedTimeRange
    description: Complete reference of the TheTrendAnalyticsDataForTheNetworkDeviceInTheSpecifiedTimeRange API.
    link: https://developer.cisco.com/docs/dna-center/#!the-trend-analytics-data-for-the-network-device-in-the-specified-time-range
notes:
  - SDK Method used are
    devices.Devices.the_trend_analytics_data_for_the_network_device_in_the_specified_time_range,
  - Paths used are
    post /dna/data/api/v1/networkDevices/{id}/trendAnalytics,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.network_devices_trend_analytics_id:
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
    id: string
    page:
      limit: 0
      offset: 0
      timestampOrder: string
    startTime: 0
    trendIntervalInMinutes: 0
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
