#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: energy_summary_analytics
short_description: Resource module for Energy Summary Analytics
description:
  - Manage operation create of the resource Energy Summary Analytics.
  - Retrieve the summary analytics data related to device energy consumption for.
version_added: '2.2.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  aggregateAttributes:
    description: Energy Summary Analytics's aggregateAttributes.
    elements: dict
    suboptions:
      function:
        description: Energy Summary Analytics's function.
        type: str
      name:
        description: Energy Summary Analytics's name.
        type: str
    type: list
  attributes:
    description: Energy Summary Analytics's attributes.
    elements: str
    type: list
  endTime:
    description: Energy Summary Analytics's endTime.
    type: int
  filters:
    description: Energy Summary Analytics's filters.
    elements: dict
    suboptions:
      filters:
        description: Energy Summary Analytics's filters.
        elements: dict
        suboptions:
          key:
            description: Energy Summary Analytics's key.
            type: str
          operator:
            description: Energy Summary Analytics's operator.
            type: str
          value:
            description: Energy Summary Analytics's value.
            elements: str
            type: list
        type: list
      logicalOperator:
        description: Energy Summary Analytics's logicalOperator.
        type: str
    type: list
  groupBy:
    description: Energy Summary Analytics's groupBy.
    elements: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  page:
    description: Energy Summary Analytics's page.
    suboptions:
      limit:
        description: Energy Summary Analytics's limit.
        type: int
      offset:
        description: Energy Summary Analytics's offset.
        type: int
      sortBy:
        description: Energy Summary Analytics's sortBy.
        elements: dict
        suboptions:
          function:
            description: Energy Summary Analytics's function.
            type: str
          name:
            description: Energy Summary Analytics's name.
            type: str
          order:
            description: Energy Summary Analytics's order.
            type: str
        type: list
    type: dict
  startTime:
    description: Energy Summary Analytics's startTime.
    type: int
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Know Your Network GetEnergySummaryAnalytics
    description: Complete reference of the GetEnergySummaryAnalytics API.
    link: https://developer.cisco.com/docs/dna-center/#!get-energy-summary-analytics
notes:
  - SDK Method used are
    know_your_network.KnowYourNetwork.get_energy_summary_analytics,
  - Paths used are
    post /dna/data/api/v1/energy/summaryAnalytics,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.energy_summary_analytics:
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
      sortBy:
        - function: string
          name: string
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
      "page": {
        "limit": 0,
        "offset": 0,
        "count": 0,
        "sortBy": [
          {
            "name": "string",
            "order": "string",
            "function": "string"
          }
        ]
      },
      "version": "string"
    }
"""
