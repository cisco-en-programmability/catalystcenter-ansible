#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_stats_trend_analytics_create
short_description: Resource module for Wireless Controllers Stats Trend Analytics Create
description:
  - Manage operation create of the resource Wireless Controllers Stats Trend Analytics Create. - > Retrieves the time series
    stats of a specific WLC by applying complex filters, aggregate functions, and grouping. The data will be grouped based
    on the specified trend time interval. If startTime and endTime are not provided, the API defaults to the last 24 hours.
    - > Retrieves the time series stats of a specific WLC by applying complex filters, aggregate functions, and grouping.
    The data will be grouped based on the specified trend time interval. If startTime and endTime are not provided, the API
    defaults to the last 24 hours.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  aggregateAttributes:
    description: Wireless Controllers Stats Trend Analytics Create's aggregateAttributes.
    elements: dict
    suboptions:
      function:
        description: Type of aggregate function to apply on the field when querying data.
        type: str
      name:
        description: Supported aggregated attributes related to WlcStats All the aggregate attributes support min, max, avg,
          sum functions.
        type: str
    type: list
  attributes:
    description: Wireless Controllers Stats Trend Analytics Create's attributes.
    elements: str
    type: list
  endTime:
    description: End time to which the API queries the dataset related to the resource. It must be specified in terms of milliseconds
      since UNIX epoch. Value is inclusive.
    type: int
  filters:
    description: Wireless Controllers Stats Trend Analytics Create's filters.
    elements: dict
    suboptions:
      filters:
        description: Nested array of filters in case of AND/OR based filters. Only one level of nesting will be supported.
          Structure of nested filter is the same as parent with all operators supported except AND or OR.
        elements: dict
        suboptions:
          filters:
            description: Nested array of filters in case of AND/OR based filters. Only one level of nesting will be supported.
              Structure of nested filter is the same as parent with all operators supported except AND or OR.
            elements: dict
            suboptions:
              filters:
                description: Nested array of filters in case of AND/OR based filters. Only one level of nesting will be supported.
                  Structure of nested filter is the same as parent with all operators supported except AND or OR.
                elements: dict
                suboptions:
                  filters:
                    description: Nested array of filters in case of AND/OR based filters. Only one level of nesting will be
                      supported. Structure of nested filter is the same as parent with all operators supported except AND
                      or OR.
                    elements: dict
                    suboptions:
                      filters:
                        description: Nested array of filters in case of AND/OR based filters. Only one level of nesting will
                          be supported. Structure of nested filter is the same as parent with all operators supported except
                          AND or OR.
                        elements: dict
                        type: list
                      key:
                        description: Supported filter attributes related to WlcStats.
                        type: str
                      logicalOperator:
                        description: Operator to use when attempting to apply a logical conjunction of more than 1 filter
                          Logical operations include 'and', 'or'.
                        type: str
                      operator:
                        description: Type of filter operator to use for querying data | in and out operator takes multiple
                          values and applies the filters.
                        type: str
                      value:
                        description: Field value(s) to filter the data set. Array of values is used for "in" or "out" operator.
                          Values will be of whatever type the specific field being filtered is defined with. For other operators,
                          filter value is of whatever type the specific field being filtered is defined with. In the case
                          of an "and" or "or" operator, this values array will be ignored, and the values arrays in each of
                          the *nested filters* will be used. The data type of a value, or each item inside the value in case
                          it is a list, must match the type defined in the WlcStats response model.
                        type: dict
                    type: list
                  key:
                    description: Supported filter attributes related to WlcStats.
                    type: str
                  logicalOperator:
                    description: Operator to use when attempting to apply a logical conjunction of more than 1 filter Logical
                      operations include 'and', 'or'.
                    type: str
                  operator:
                    description: Type of filter operator to use for querying data | in and out operator takes multiple values
                      and applies the filters.
                    type: str
                  value:
                    description: Field value(s) to filter the data set. Array of values is used for "in" or "out" operator.
                      Values will be of whatever type the specific field being filtered is defined with. For other operators,
                      filter value is of whatever type the specific field being filtered is defined with. In the case of an
                      "and" or "or" operator, this values array will be ignored, and the values arrays in each of the *nested
                      filters* will be used. The data type of a value, or each item inside the value in case it is a list,
                      must match the type defined in the WlcStats response model.
                    type: dict
                type: list
              key:
                description: Supported filter attributes related to WlcStats.
                type: str
              logicalOperator:
                description: Operator to use when attempting to apply a logical conjunction of more than 1 filter Logical
                  operations include 'and', 'or'.
                type: str
              operator:
                description: Type of filter operator to use for querying data | in and out operator takes multiple values
                  and applies the filters.
                type: str
              value:
                description: Field value(s) to filter the data set. Array of values is used for "in" or "out" operator. Values
                  will be of whatever type the specific field being filtered is defined with. For other operators, filter
                  value is of whatever type the specific field being filtered is defined with. In the case of an "and" or
                  "or" operator, this values array will be ignored, and the values arrays in each of the *nested filters*
                  will be used. The data type of a value, or each item inside the value in case it is a list, must match the
                  type defined in the WlcStats response model.
                type: dict
            type: list
          key:
            description: Supported filter attributes related to WlcStats.
            type: str
          logicalOperator:
            description: Operator to use when attempting to apply a logical conjunction of more than 1 filter Logical operations
              include 'and', 'or'.
            type: str
          operator:
            description: Type of filter operator to use for querying data | in and out operator takes multiple values and
              applies the filters.
            type: str
          value:
            description: Field value(s) to filter the data set. Array of values is used for "in" or "out" operator. Values
              will be of whatever type the specific field being filtered is defined with. For other operators, filter value
              is of whatever type the specific field being filtered is defined with. In the case of an "and" or "or" operator,
              this values array will be ignored, and the values arrays in each of the *nested filters* will be used. The data
              type of a value, or each item inside the value in case it is a list, must match the type defined in the WlcStats
              response model.
            type: dict
        type: list
      key:
        description: Supported filter attributes related to WlcStats.
        type: str
      logicalOperator:
        description: Operator to use when attempting to apply a logical conjunction of more than 1 filter Logical operations
          include 'and', 'or'.
        type: str
      operator:
        description: Type of filter operator to use for querying data | in and out operator takes multiple values and applies
          the filters.
        type: str
      value:
        description: Field value(s) to filter the data set. Array of values is used for "in" or "out" operator. Values will
          be of whatever type the specific field being filtered is defined with. For other operators, filter value is of whatever
          type the specific field being filtered is defined with. In the case of an "and" or "or" operator, this values array
          will be ignored, and the values arrays in each of the *nested filters* will be used. The data type of a value, or
          each item inside the value in case it is a list, must match the type defined in the WlcStats response model.
        type: dict
    type: list
  groupBy:
    description: Wireless Controllers Stats Trend Analytics Create's groupBy.
    elements: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  id:
    description: Id path parameter. The WLC device UUID.
    type: str
  page:
    description: Wireless Controllers Stats Trend Analytics Create's page.
    suboptions:
      count:
        description: Number of records returned after applying applicable filtering. Field is ignored for request and updated
          by API in the response.
        type: int
      cursor:
        description: It's an opaque string field that indicates the next record in the requested collection. If no records
          remain, the API returns a response with a count of zero. The default value is an empty string, and the initial value
          must be an empty string. The cursor value is populated by the API in the response page block. If the user wants
          more records, the cursor in the subsequent request must be updated with the value from the previous response.
        type: str
      limit:
        description: Number of records to fetch in a page.
        type: int
      timeSortOrder:
        description: Sort order. 'asc' for ascending and 'desc' for descending.
        type: str
    type: dict
  startTime:
    description: Start time from which the API queries the dataset related to the resource. It must be specified in terms
      of milliseconds since UNIX epoch. Value is inclusive.
    type: int
  trendInterval:
    description: The time window to aggregate the metrics. Interval can be 5 minutes or 10 minutes or 1 hour or 1 day or 7
      days.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices RetrievesSpecificStatsForAWLCOverASpecifiedPeriodOfTime
    description: Complete reference of the RetrievesSpecificStatsForAWLCOverASpecifiedPeriodOfTime API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-specific-stats-for-awlc-over-a-specified-period-of-time
  - name: Cisco Catalyst Center documentation for Devices RetrievesSpecificStatsForAWLCOverASpecifiedPeriodOfTimeKnowYourNetwork
    description: Complete reference of the RetrievesSpecificStatsForAWLCOverASpecifiedPeriodOfTimeKnowYourNetwork API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-specific-stats-for-awlc-over-a-specified-period-of-time-know-your-network
notes:
  - SDK Method used are
    devices.Devices.retrieves_specific_stats_for_a_wlc_over_a_specified_period_of_time_know_your_network,
  - Paths used are
    post /dna/data/api/v1/wirelessControllersStats/trendAnalytics,
    post /dna/data/api/v1/wirelessControllersStats/{id}/trendAnalytics,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.wireless_controllers_stats_trend_analytics_create:
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
          - filters:
              - filters:
                  - filters:
                      - filters:
                          - {}
                        key: string
                        logicalOperator: string
                        operator: string
                        value: {}
                    key: string
                    logicalOperator: string
                    operator: string
                    value: {}
                key: string
                logicalOperator: string
                operator: string
                value: {}
            key: string
            logicalOperator: string
            operator: string
            value: {}
        key: string
        logicalOperator: string
        operator: string
        value: {}
    groupBy:
      - string
    headers: '{{my_headers | from_json}}'
    id: string
    page:
      count: 0
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
          "attributes": [
            {
              "name": "string",
              "value": {}
            }
          ],
          "aggregateAttributes": [
            {
              "name": "string",
              "function": "string",
              "value": {}
            }
          ],
          "groups": [
            {
              "id": "string",
              "attributes": [
                {
                  "name": "string",
                  "value": {}
                }
              ],
              "aggregateAttributes": [
                {
                  "name": "string",
                  "function": "string",
                  "value": {}
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
