#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: interfaces_id_trend_analytics
short_description: Resource module for Interfaces Id Trend Analytics
description:
  - Manage operation create of the resource Interfaces Id Trend Analytics.
  - The Trend analytcis data for the interface, identified by its instanceUuid, in.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  aggregateAttributes:
    description: Interfaces Id Trend Analytics's aggregateAttributes.
    elements: dict
    suboptions:
      function:
        description: Interfaces Id Trend Analytics's function.
        type: str
      name:
        description: Interfaces Id Trend Analytics's name.
        type: str
    type: list
  attributes:
    description: Interfaces Id Trend Analytics's attributes.
    elements: str
    type: list
  endTime:
    description: Interfaces Id Trend Analytics's endTime.
    type: int
  filters:
    description: Interfaces Id Trend Analytics's filters.
    elements: dict
    suboptions:
      key:
        description: Interfaces Id Trend Analytics's key.
        type: str
      operator:
        description: Interfaces Id Trend Analytics's operator.
        type: str
      value:
        description: Interfaces Id Trend Analytics's value.
        type: str
    type: list
  id:
    description: Id path parameter. The interface instance Uuid.
    type: str
  startTime:
    description: Interfaces Id Trend Analytics's startTime.
    type: int
  timestampOrder:
    description: Interfaces Id Trend Analytics's timestampOrder.
    type: str
  trendIntervalInMinutes:
    description: Interfaces Id Trend Analytics's trendIntervalInMinutes.
    type: int
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices TheTrendAnalytcisDataForTheInterfacesInTheSpecifiedTimeRange
    description: Complete reference of the TheTrendAnalytcisDataForTheInterfacesInTheSpecifiedTimeRange API.
    link: https://developer.cisco.com/docs/dna-center/#!the-trend-analytcis-data-for-the-interfaces-in-the-specified-time-range
notes:
  - SDK Method used are
    devices.Devices.the_trend_analytcis_data_for_the_interfaces_in_the_specified_time_range,
  - Paths used are
    post /dna/data/api/v1/interfaces/{id}/trendAnalytics,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.interfaces_id_trend_analytics:
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
    id: string
    startTime: 0
    timestampOrder: string
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
              "name": "string"
            }
          ]
        }
      ],
      "timestampOrder": "string"
    }
"""
