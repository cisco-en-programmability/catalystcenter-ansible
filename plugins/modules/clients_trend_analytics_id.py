#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: clients_trend_analytics_id
short_description: Resource module for Clients Trend Analytics Id
description:
  - Manage operation create of the resource Clients Trend Analytics Id.
  - Retrieves the time series information of a specific client by applying complex.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  aggregateAttributes:
    description: Clients Trend Analytics Id's aggregateAttributes.
    elements: dict
    suboptions:
      function:
        description: Clients Trend Analytics Id's function.
        type: str
      name:
        description: Clients Trend Analytics Id's name.
        type: str
    type: list
  attributes:
    description: Clients Trend Analytics Id's attributes.
    elements: str
    type: list
  endTime:
    description: Clients Trend Analytics Id's endTime.
    type: int
  filters:
    description: Clients Trend Analytics Id's filters.
    elements: dict
    suboptions:
      key:
        description: Clients Trend Analytics Id's key.
        type: str
      operator:
        description: Clients Trend Analytics Id's operator.
        type: str
      value:
        description: Clients Trend Analytics Id's value.
        type: int
    type: list
  groupBy:
    description: Clients Trend Analytics Id's groupBy.
    elements: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  id:
    description: Id path parameter. Id is the client mac address. It can be specified in one of the notational conventions
      01 23 45 67 89 AB or 01-23-45-67-89-AB or 0123.4567.89AB and is case insensitive.
    type: str
  page:
    description: Clients Trend Analytics Id's page.
    suboptions:
      cursor:
        description: Clients Trend Analytics Id's cursor.
        type: str
      limit:
        description: Clients Trend Analytics Id's limit.
        type: int
      timeSortOrder:
        description: Clients Trend Analytics Id's timeSortOrder.
        type: str
    type: dict
  startTime:
    description: Clients Trend Analytics Id's startTime.
    type: int
  trendInterval:
    description: Clients Trend Analytics Id's trendInterval.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Clients RetrievesSpecificClientInformationOverASpecifiedPeriodOfTime
    description: Complete reference of the RetrievesSpecificClientInformationOverASpecifiedPeriodOfTime API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-specific-client-information-over-a-specified-period-of-time
notes:
  - SDK Method used are
    clients.Clients.retrieves_specific_client_information_over_a_specified_period_of_time,
  - Paths used are
    post /dna/data/api/v1/clients/{id}/trendAnalytics,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.clients_trend_analytics_id:
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
        value: 0
    groupBy:
      - string
    headers: '{{my_headers | from_json}}'
    id: string
    page:
      cursor: string
      limit: 0
      timeSortOrder: string
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
          "groups": [
            {
              "id": "string",
              "attributes": [
                {
                  "name": "string",
                  "value": 0
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
        "cursor": "string",
        "count": 0,
        "timeSortOrder": "string"
      },
      "version": "string"
    }
"""
