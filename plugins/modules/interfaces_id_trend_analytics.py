#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: interfaces_id_trend_analytics
short_description: Resource module for Interfaces Id Trend Analytics
description:
  - This module represents an alias of the module interfaces_id_trend_analytics_v1
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  aggregateAttributes:
    description: Interfaces Id Trend Analytics's aggregateAttributes.
    elements: dict
    suboptions:
      function:
        description: Function.
        type: str
      name:
        description: Name.
        type: str
    type: list
  attributes:
    description: Attributes.
    elements: str
    type: list
  endTime:
    description: End Time.
    type: int
  filters:
    description: Interfaces Id Trend Analytics's filters.
    elements: dict
    suboptions:
      key:
        description: Key.
        type: str
      operator:
        description: Operator.
        type: str
      value:
        description: Value.
        type: str
    type: list
  id:
    description: Id path parameter. The interface instance Uuid.
    type: str
  startTime:
    description: Start Time.
    type: int
  timestampOrder:
    description: Timestamp Order.
    type: str
  trendIntervalInMinutes:
    description: Trend Interval In Minutes.
    type: int
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices TheTrendAnalytcisDataForTheInterfacesInTheSpecifiedTimeRangeV1
    description: Complete reference of the TheTrendAnalytcisDataForTheInterfacesInTheSpecifiedTimeRangeV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!the-trend-analytcis-data-for-the-interfaces-in-the-specified-time-range
notes:
  - SDK Method used are
    devices.Devices.the_trend_analytcis_data_for_the_interfaces_in_the_specified_time_range_v1,
  - Paths used are post /dna/data/api/v1/interfaces/{id}/trendAnalytics,
  - It should be noted that this module is an alias of interfaces_id_trend_analytics_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.interfaces_id_trend_analytics:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
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
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
