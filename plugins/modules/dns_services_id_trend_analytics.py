#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: dns_services_id_trend_analytics
short_description: Resource module for Dns Services Id Trend Analytics
description:
  - Manage operation create of the resource Dns Services Id Trend Analytics.
  - Gets the trend analytics data related to a particular DNS Service matching the.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  aggregateAttributes:
    description: Dns Services Id Trend Analytics's aggregateAttributes.
    elements: dict
    suboptions:
      function:
        description: Dns Services Id Trend Analytics's function.
        type: str
      name:
        description: Dns Services Id Trend Analytics's name.
        type: str
    type: list
  attributes:
    description: Dns Services Id Trend Analytics's attributes.
    elements: str
    type: list
  endTime:
    description: Dns Services Id Trend Analytics's endTime.
    type: int
  filters:
    description: Dns Services Id Trend Analytics's filters.
    elements: dict
    suboptions:
      filters:
        description: Dns Services Id Trend Analytics's filters.
        elements: str
        type: list
      key:
        description: Dns Services Id Trend Analytics's key.
        type: str
      logicalOperator:
        description: Dns Services Id Trend Analytics's logicalOperator.
        type: str
      operator:
        description: Dns Services Id Trend Analytics's operator.
        type: str
      value:
        description: Dns Services Id Trend Analytics's value.
        type: dict
    type: list
  groupBy:
    description: Dns Services Id Trend Analytics's groupBy.
    elements: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  id:
    description: Id path parameter. Unique id of the DNS Service. It is the combination of DNS Server IP (`serverIp`) and
      Device UUID (`deviceId`) separated by underscore (`_`). Example If `serverIp` is `10.76.81.33` and `deviceId` is `6bef213c-19ca-4170-8375-b694e251101c`,
      then the `id` would be `10.76.81.33_6bef213c-19ca-4170-8375-b694e251101c`.
    type: str
  page:
    description: Dns Services Id Trend Analytics's page.
    suboptions:
      limit:
        description: Dns Services Id Trend Analytics's limit.
        type: int
      offset:
        description: Dns Services Id Trend Analytics's offset.
        type: int
      timestampOrder:
        description: Dns Services Id Trend Analytics's timestampOrder.
        type: str
    type: dict
  startTime:
    description: Dns Services Id Trend Analytics's startTime.
    type: int
  trendInterval:
    description: Dns Services Id Trend Analytics's trendInterval.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices GetTrendAnalyticsDataForAGivenDNSServiceMatchingTheIdOfTheService
    description: Complete reference of the GetTrendAnalyticsDataForAGivenDNSServiceMatchingTheIdOfTheService API.
    link: https://developer.cisco.com/docs/dna-center/#!get-trend-analytics-data-for-a-given-dns-service-matching-the-id-of-the-service
notes:
  - SDK Method used are
    devices.Devices.get_trend_analytics_data_for_a_given_dns_service_matching_the_id_of_the_service,
  - Paths used are
    post /dna/data/api/v1/dnsServices/{id}/trendAnalytics,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.dns_services_id_trend_analytics:
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
    id: string
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
