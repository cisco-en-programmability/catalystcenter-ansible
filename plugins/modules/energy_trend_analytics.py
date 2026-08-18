#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: energy_trend_analytics
short_description: Resource module for Energy Trend Analytics
description:
  - Manage operation create of the resource Energy Trend Analytics.
  - Retrieve the energy trend analytics data related to device energy consumption.
version_added: '2.2.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  aggregateAttributes:
    description: Energy Trend Analytics's aggregateAttributes.
    elements: dict
    suboptions:
      function:
        description: Energy Trend Analytics's function.
        type: str
      name:
        description: Energy Trend Analytics's name.
        type: str
    type: list
  attributes:
    description: Energy Trend Analytics's attributes.
    elements: str
    type: list
  endTime:
    description: Energy Trend Analytics's endTime.
    type: int
  filters:
    description: Energy Trend Analytics's filters.
    elements: dict
    suboptions:
      filters:
        description: Energy Trend Analytics's filters.
        elements: dict
        suboptions:
          key:
            description: Energy Trend Analytics's key.
            type: str
          operator:
            description: Energy Trend Analytics's operator.
            type: str
          value:
            description: Energy Trend Analytics's value.
            elements: str
            type: list
        type: list
      logicalOperator:
        description: Energy Trend Analytics's logicalOperator.
        type: str
    type: list
  groupBy:
    description: Energy Trend Analytics's groupBy.
    elements: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  page:
    description: Energy Trend Analytics's page.
    suboptions:
      limit:
        description: Energy Trend Analytics's limit.
        type: int
      offset:
        description: Energy Trend Analytics's offset.
        type: int
      timestampOrder:
        description: Energy Trend Analytics's timestampOrder.
        type: str
    type: dict
  startTime:
    description: Energy Trend Analytics's startTime.
    type: int
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Know Your Network GetEnergyTrendAnalytics
    description: Complete reference of the GetEnergyTrendAnalytics API.
    link: https://developer.cisco.com/docs/dna-center/#!get-energy-trend-analytics
notes:
  - SDK Method used are
    know_your_network.KnowYourNetwork.get_energy_trend_analytics,
  - Paths used are
    post /dna/data/api/v1/energy/trendAnalytics,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.energy_trend_analytics:
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
            value:
              - string
        logicalOperator: string
    groupBy:
      - string
    headers: '{{my_headers | from_json}}'
    page:
      limit: 0
      offset: 0
      timestampOrder: string
    startTime: 0
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
          "timestamp": 0
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
