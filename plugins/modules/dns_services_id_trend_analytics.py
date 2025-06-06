#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: dns_services_id_trend_analytics
short_description: Resource module for Dns Services Id Trend Analytics
description:
  - This module represents an alias of the module dns_services_id_trend_analytics_v1
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  aggregateAttributes:
    description: Dns Services Id Trend Analytics's aggregateAttributes.
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
    description: Dns Services Id Trend Analytics's filters.
    elements: dict
    suboptions:
      filters:
        description: Filters.
        elements: str
        type: list
      key:
        description: Key.
        type: str
      logicalOperator:
        description: Logical Operator.
        type: str
      operator:
        description: Operator.
        type: str
      value:
        description: Value.
        type: dict
    type: list
  groupBy:
    description: Group By.
    elements: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  id:
    description: Id path parameter. Unique id of the DNS Service. It is the combination
      of DNS Server IP (`serverIp`) and Device UUID (`deviceId`) separated by underscore
      (`_`). Example If `serverIp` is `10.76.81.33` and `deviceId` is `6bef213c-19ca-4170-8375-b694e251101c`,
      then the `id` would be `10.76.81.33_6bef213c-19ca-4170-8375-b694e251101c`.
    type: str
  page:
    description: Dns Services Id Trend Analytics's page.
    suboptions:
      limit:
        description: Limit.
        type: int
      offset:
        description: Offset.
        type: int
      timestampOrder:
        description: Timestamp Order.
        type: str
    type: dict
  startTime:
    description: Start Time.
    type: int
  trendInterval:
    description: Trend Interval.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices GetTrendAnalyticsDataForAGivenDNSServiceMatchingTheIdOfTheServiceV1
    description: Complete reference of the GetTrendAnalyticsDataForAGivenDNSServiceMatchingTheIdOfTheServiceV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-trend-analytics-data-for-a-given-dns-service-matching-the-id-of-the-service
notes:
  - SDK Method used are
    devices.Devices.get_trend_analytics_data_for_a_given_d_n_s_service_matching_the_id_of_the_service_v1,
  - Paths used are post /dna/data/api/v1/dnsServices/{id}/trendAnalytics,
  - It should be noted that this module is an alias of dns_services_id_trend_analytics_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.dns_services_id_trend_analytics:
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
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
