#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_devices_process_kpis_query_count_create
short_description: Resource module for Network Devices Process Kpis Query Count Create
description:
  - Manage operation create of the resource Network Devices Process Kpis Query Count Create. - > Retrieves the number of processKpis
    by applying complex filters. If startTime and endTime are not provided, the API defaults to the last 24 hours.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  endTime:
    description: End time to which the API queries the dataset related to the resource. It must be specified in terms of milliseconds
      since UNIX epoch. Value is inclusive.
    type: int
  filters:
    description: Network Devices Process Kpis Query Count Create's filters.
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
                        description: Supported filter attributes related to ProcessKpis.
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
                          it is a list, must match the type defined in the ProcessKpis response model.
                        type: dict
                    type: list
                  key:
                    description: Supported filter attributes related to ProcessKpis.
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
                      must match the type defined in the ProcessKpis response model.
                    type: dict
                type: list
              key:
                description: Supported filter attributes related to ProcessKpis.
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
                  type defined in the ProcessKpis response model.
                type: dict
            type: list
          key:
            description: Supported filter attributes related to ProcessKpis.
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
              type of a value, or each item inside the value in case it is a list, must match the type defined in the ProcessKpis
              response model.
            type: dict
        type: list
      key:
        description: Supported filter attributes related to ProcessKpis.
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
          each item inside the value in case it is a list, must match the type defined in the ProcessKpis response model.
        type: dict
    type: list
  headers:
    description: Additional headers.
    type: dict
  networkDeviceId:
    description: NetworkDeviceId path parameter. Network Device UUID.
    type: str
  startTime:
    description: Start time from which the API queries the dataset related to the resource. It must be specified in terms
      of milliseconds since UNIX epoch. Value is inclusive.
    type: int
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices RetrievesTheNumberOfProcessesByApplyingComplexFilters
    description: Complete reference of the RetrievesTheNumberOfProcessesByApplyingComplexFilters API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-number-of-processes-by-applying-complex-filters
notes:
  - SDK Method used are
    devices.Devices.retrieves_the_number_of_processes_by_applying_complex_filters,
  - Paths used are
    post /dna/data/api/v1/networkDevices/{networkDeviceId}/processKpis/query/count,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.network_devices_process_kpis_query_count_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
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
    networkDeviceId: string
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
        "count": 0
      },
      "version": "string"
    }
"""
