#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: tracked_clients_query_create
short_description: Resource module for Tracked Clients Query Create
description:
  - Manage operation create of the resource Tracked Clients Query Create.
  - Returns tracked-client configurations matching the provided request-body filters.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  filters:
    description: List of filters to apply when querying tracked-client configurations. Supported operators by field are `clientMacAddress`,
      `duid`, `description` eq, neq, in, notIn, like, liker `trackingStartTime`, `trackingEndTime` eq, neq, lt, gt, lte, gte
      `isPresentOnNetwork` eq, neq `randomizedMacAddresses` eq, neq, in, notIn, like, liker `notificationModes` in, notIn
      For `trackingEndTime`, value `0` represents never-expiring tracking. Nested filter composition is supported through
      `logicalOperator` and nested `filters`. Only one level of nested filters is supported.
    elements: dict
    suboptions:
      filters:
        description: Nested tracked-client filters used with `logicalOperator`. Child filters cannot contain nested `filters`
          of their own.
        elements: dict
        suboptions:
          filters:
            description: Nested tracked-client filters used with `logicalOperator`. Child filters cannot contain nested `filters`
              of their own.
            elements: dict
            suboptions:
              filters:
                description: Nested tracked-client filters used with `logicalOperator`. Child filters cannot contain nested
                  `filters` of their own.
                elements: dict
                suboptions:
                  filters:
                    description: Nested tracked-client filters used with `logicalOperator`. Child filters cannot contain nested
                      `filters` of their own.
                    elements: dict
                    suboptions:
                      filters:
                        description: Nested tracked-client filters used with `logicalOperator`. Child filters cannot contain
                          nested `filters` of their own.
                        elements: dict
                        type: list
                      key:
                        description: Supported tracked-client fields for request-body query filtering.
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
                        description: Value or values to apply with the filter operator. Depending on the field and operator,
                          this may be a string, number, boolean, or array of scalar values.
                        type: dict
                    type: list
                  key:
                    description: Supported tracked-client fields for request-body query filtering.
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
                    description: Value or values to apply with the filter operator. Depending on the field and operator, this
                      may be a string, number, boolean, or array of scalar values.
                    type: dict
                type: list
              key:
                description: Supported tracked-client fields for request-body query filtering.
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
                description: Value or values to apply with the filter operator. Depending on the field and operator, this
                  may be a string, number, boolean, or array of scalar values.
                type: dict
            type: list
          key:
            description: Supported tracked-client fields for request-body query filtering.
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
            description: Value or values to apply with the filter operator. Depending on the field and operator, this may
              be a string, number, boolean, or array of scalar values.
            type: dict
        type: list
      key:
        description: Supported tracked-client fields for request-body query filtering.
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
        description: Value or values to apply with the filter operator. Depending on the field and operator, this may be a
          string, number, boolean, or array of scalar values.
        type: dict
    type: list
  headers:
    description: Additional headers.
    type: dict
  page:
    description: Pagination input for tracked-client queries.
    suboptions:
      limit:
        description: Maximum number of tracked-client records to return in one page.
        type: int
      offset:
        description: One-based starting offset for the tracked-client query results.
        type: int
      sortBy:
        description: Sort fields applied before pagination. Only single-field sorting is supported on this API.
        elements: dict
        suboptions:
          name:
            description: Supported tracked-client fields for request-body sorting.
            type: str
          order:
            description: Sort order. 'asc' for ascending and 'desc' for descending.
            type: str
        type: list
    type: dict
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Clients QueryTrackedClientConfigurationsWithRequestBodyFilters
    description: Complete reference of the QueryTrackedClientConfigurationsWithRequestBodyFilters API.
    link: https://developer.cisco.com/docs/dna-center/#!query-tracked-client-configurations-with-request-body-filters
notes:
  - SDK Method used are
    clients.Clients.query_tracked_client_configurations_with_request_body_filters,
  - Paths used are
    post /dna/intent/api/v1/trackedClients/query,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.tracked_clients_query_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
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
      limit: 0
      offset: 0
      sortBy:
        - name: string
          order: string
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
          "clientMacAddress": "string",
          "duid": "string",
          "description": "string",
          "trackingStartTime": 0,
          "trackingEndTime": 0,
          "notificationModes": [
            "string"
          ],
          "lastOnboardedTime": 0,
          "lastDisconnectedTime": 0,
          "isPresentOnNetwork": true,
          "randomizedMacAddresses": [
            "string"
          ]
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
