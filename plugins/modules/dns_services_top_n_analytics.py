#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: dns_services_top_n_analytics
short_description: Resource module for Dns Services Top N Analytics
description:
  - Manage operation create of the resource Dns Services Top N Analytics.
  - Gets the Top N analytics data related to DNS Services based on given filters.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  aggregateAttributes:
    description: Dns Services Top N Analytics's aggregateAttributes.
    elements: dict
    suboptions:
      function:
        description: Dns Services Top N Analytics's function.
        type: str
      name:
        description: Dns Services Top N Analytics's name.
        type: str
    type: list
  attributes:
    description: Dns Services Top N Analytics's attributes.
    elements: str
    type: list
  endTime:
    description: Dns Services Top N Analytics's endTime.
    type: int
  filters:
    description: Dns Services Top N Analytics's filters.
    elements: dict
    suboptions:
      filters:
        description: Dns Services Top N Analytics's filters.
        elements: str
        type: list
      key:
        description: Dns Services Top N Analytics's key.
        type: str
      logicalOperator:
        description: Dns Services Top N Analytics's logicalOperator.
        type: str
      operator:
        description: Dns Services Top N Analytics's operator.
        type: str
      value:
        description: Dns Services Top N Analytics's value.
        type: dict
    type: list
  groupBy:
    description: Dns Services Top N Analytics's groupBy.
    elements: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  page:
    description: Dns Services Top N Analytics's page.
    suboptions:
      limit:
        description: Dns Services Top N Analytics's limit.
        type: int
      offset:
        description: Dns Services Top N Analytics's offset.
        type: int
      sortBy:
        description: Dns Services Top N Analytics's sortBy.
        elements: dict
        suboptions:
          function:
            description: Dns Services Top N Analytics's function.
            type: str
          name:
            description: Dns Services Top N Analytics's name.
            type: str
          order:
            description: Dns Services Top N Analytics's order.
            type: str
        type: list
    type: dict
  startTime:
    description: Dns Services Top N Analytics's startTime.
    type: int
  topN:
    description: Dns Services Top N Analytics's topN.
    type: int
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices GetTopNAnalyticsDataOfDNSServicesForGivenSetOfComplexFilters
    description: Complete reference of the GetTopNAnalyticsDataOfDNSServicesForGivenSetOfComplexFilters API.
    link: https://developer.cisco.com/docs/dna-center/#!get-top-n-analytics-data-of-dns-services-for-given-set-of-complex-filters
notes:
  - SDK Method used are
    devices.Devices.get_top_n_analytics_data_of_dns_services_for_given_set_of_complex_filters,
  - Paths used are
    post /dna/data/api/v1/dnsServices/topNAnalytics,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.dns_services_top_n_analytics:
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
      sortBy:
        - function: string
          name: string
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
        "count": "string",
        "sortBy": [
          {
            "name": "string",
            "function": "string",
            "order": "string"
          }
        ]
      }
    }
"""
