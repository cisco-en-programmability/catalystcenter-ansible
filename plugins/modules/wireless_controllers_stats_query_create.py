#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_stats_query_create
short_description: Resource module for Wireless Controllers Stats Query Create
description:
  - Manage operation create of the resource Wireless Controllers Stats Query Create. - > Retrieves the list of Wireless Controllers'
    statistics while also supporting aggregate attributes. If startTime and endTime are not provided, the API defaults to
    the last 24 hours.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  aggregateAttributes:
    description: Wireless Controllers Stats Query Create's aggregateAttributes.
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
    description: Wireless Controllers Stats Query Create's attributes.
    elements: str
    type: list
  endTime:
    description: End time to which the API queries the dataset related to the resource. It must be specified in terms of milliseconds
      since UNIX epoch. Value is inclusive.
    type: int
  filters:
    description: Wireless Controllers Stats Query Create's filters.
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
  headers:
    description: Additional headers.
    type: dict
  page:
    description: Wireless Controllers Stats Query Create's page.
    suboptions:
      count:
        description: Total number of records related to the resource after applying applicable filtering. Field is ignored
          for request and updated by API in the response.
        type: int
      limit:
        description: Number of records to fetch in a page.
        type: int
      offset:
        description: Starting offset of data to fetch and returned.
        type: int
      sortBy:
        description: Wireless Controllers Stats Query Create's sortBy.
        elements: dict
        suboptions:
          name:
            description: Attributes related to WlcStats resource that can be used to sort the response.
            type: str
          order:
            description: Sort order. 'asc' for ascending and 'desc' for descending.
            type: str
        type: list
    type: dict
  startTime:
    description: Start time from which the API queries the dataset related to the resource. It must be specified in terms
      of milliseconds since UNIX epoch. Value is inclusive.
    type: int
  views:
    description: Wireless Controllers Stats Query Create's views.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices RetrievesTheListOfWirelessControllersStatisticsWhileAlsoSupportingAggregateAttributes
    description: Complete reference of the RetrievesTheListOfWirelessControllersStatisticsWhileAlsoSupportingAggregateAttributes
      API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-wireless-controllers-statistics-while-also-supporting-aggregate-attributes
notes:
  - SDK Method used are
    devices.Devices.retrieves_the_list_of_wireless_controllers_statistics_while_also_supporting_aggregate_attributes,
  - Paths used are
    post /dna/data/api/v1/wirelessControllersStats/query,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.wireless_controllers_stats_query_create:
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
    headers: '{{my_headers | from_json}}'
    page:
      count: 0
      limit: 0
      offset: 0
      sortBy:
        - name: string
          order: string
    startTime: 0
    views:
      - string
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
          "id": "string",
          "name": "string",
          "siteHierarchy": "string",
          "siteHierarchyId": "string",
          "lastUpdatedTime": 0
        }
      ],
      "page": {
        "limit": 0,
        "offset": 0,
        "count": 0,
        "sortBy": [
          {
            "name": "string",
            "order": "string"
          }
        ]
      },
      "version": "string"
    }
"""
