#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_devices_summary_analytics
short_description: Resource module for Network Devices Summary Analytics
description:
  - Manage operation create of the resource Network Devices Summary Analytics.
  - Gets the summary analytics data related to network devices based on the.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  aggregateAttributes:
    description: Network Devices Summary Analytics's aggregateAttributes.
    elements: dict
    suboptions:
      function:
        description: Network Devices Summary Analytics's function.
        type: str
      name:
        description: Network Devices Summary Analytics's name.
        type: str
    type: list
  attributes:
    description: Network Devices Summary Analytics's attributes.
    elements: str
    type: list
  endTime:
    description: Network Devices Summary Analytics's endTime.
    type: int
  filters:
    description: Network Devices Summary Analytics's filters.
    elements: dict
    suboptions:
      key:
        description: Network Devices Summary Analytics's key.
        type: str
      operator:
        description: Network Devices Summary Analytics's operator.
        type: str
      value:
        description: Network Devices Summary Analytics's value.
        type: str
    type: list
  groupBy:
    description: Network Devices Summary Analytics's groupBy.
    elements: str
    type: list
  page:
    description: Network Devices Summary Analytics's page.
    suboptions:
      limit:
        description: Network Devices Summary Analytics's limit.
        type: int
      offset:
        description: Network Devices Summary Analytics's offset.
        type: int
      sortBy:
        description: Network Devices Summary Analytics's sortBy.
        elements: dict
        suboptions:
          name:
            description: Network Devices Summary Analytics's name.
            type: str
          order:
            description: Network Devices Summary Analytics's order.
            type: str
        type: list
    type: dict
  startTime:
    description: Network Devices Summary Analytics's startTime.
    type: int
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices GetsTheSummaryAnalyticsDataRelatedToNetworkDevices
    description: Complete reference of the GetsTheSummaryAnalyticsDataRelatedToNetworkDevices API.
    link: https://developer.cisco.com/docs/dna-center/#!gets-the-summary-analytics-data-related-to-network-devices
notes:
  - SDK Method used are
    devices.Devices.gets_the_summary_analytics_data_related_to_network_devices,
  - Paths used are
    post /dna/data/api/v1/networkDevices/summaryAnalytics,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.network_devices_summary_analytics:
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
    page:
      limit: 0
      offset: 0
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
        "attributes": [],
        "aggregateAttributes": [],
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
      },
      "page": [
        {
          "limit": 0,
          "offset": 0,
          "count": 0,
          "sortBy": [
            {
              "name": "string",
              "order": "string"
            }
          ]
        }
      ]
    }
"""
