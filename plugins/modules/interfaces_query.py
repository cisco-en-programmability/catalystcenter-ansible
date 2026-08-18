#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: interfaces_query
short_description: Resource module for Interfaces Query
description:
  - Manage operation create of the resource Interfaces Query.
  - Gets the list of interfaces across the Network Devices based on the provided.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  aggregateAttributes:
    description: Interfaces Query's aggregateAttributes.
    elements: dict
    suboptions:
      function:
        description: Interfaces Query's function.
        type: str
      name:
        description: Interfaces Query's name.
        type: str
    type: list
  attributes:
    description: Interfaces Query's attributes.
    elements: str
    type: list
  endTime:
    description: Interfaces Query's endTime.
    type: int
  filters:
    description: Interfaces Query's filters.
    elements: dict
    suboptions:
      filters:
        description: Interfaces Query's filters.
        elements: dict
        suboptions:
          filters:
            description: Interfaces Query's filters.
            elements: str
            type: list
          key:
            description: Interfaces Query's key.
            type: str
          logicalOperator:
            description: Interfaces Query's logicalOperator.
            type: str
          operator:
            description: Interfaces Query's operator.
            type: str
          value:
            description: Interfaces Query's value.
            type: dict
        type: list
      key:
        description: Interfaces Query's key.
        type: str
      logicalOperator:
        description: Interfaces Query's logicalOperator.
        type: str
      operator:
        description: Interfaces Query's operator.
        type: str
      value:
        description: Interfaces Query's value.
        type: dict
    type: list
  page:
    description: Interfaces Query's page.
    suboptions:
      limit:
        description: Interfaces Query's limit.
        type: int
      offset:
        description: Interfaces Query's offset.
        type: int
      sortBy:
        description: Interfaces Query's sortBy.
        elements: dict
        suboptions:
          name:
            description: Interfaces Query's name.
            type: str
          order:
            description: Interfaces Query's order.
            type: str
        type: list
    type: dict
  startTime:
    description: Interfaces Query's startTime.
    type: int
  views:
    description: Interfaces Query's views.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices GetsTheListOfInterfacesAcrossTheNetworkDevicesBasedOnTheProvidedComplexFiltersAndAggregationFunctions
    description: Complete reference of the GetsTheListOfInterfacesAcrossTheNetworkDevicesBasedOnTheProvidedComplexFiltersAndAggregationFunctions
      API.
    link: https://developer.cisco.com/docs/dna-center/#!gets-the-list-of-interfaces-across-the-network-devices-based-on-the-provided-complex-filters-and-aggregation-functions
notes:
  - SDK Method used are
    devices.Devices.gets_the_list_of_interfaces_across_the_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions,
  - Paths used are
    post /dna/data/api/v1/interfaces/query,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.interfaces_query:
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
              - string
            key: string
            logicalOperator: string
            operator: string
            value: {}
        key: string
        logicalOperator: string
        operator: string
        value: {}
    page:
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
          "adminStatus": "string",
          "description": "string",
          "duplexConfig": "string",
          "duplexOper": "string",
          "interfaceIfIndex": 0,
          "interfaceType": "string",
          "ipv4Address": "string",
          "ipv6AddressList": [
            "string"
          ],
          "isL3Interface": true,
          "isWan": true,
          "macAddr": "string",
          "mediaType": "string",
          "name": "string",
          "operStatus": "string",
          "peerStackMember": 0,
          "peerStackPort": "string",
          "portChannelId": "string",
          "portMode": "string",
          "portType": "string",
          "rxDiscards": 0,
          "rxError": 0,
          "rxRate": 0,
          "rxUtilization": 0,
          "speed": "string",
          "stackPortType": "string",
          "timestamp": 0,
          "txDiscards": 0,
          "txError": 0,
          "txRate": 0,
          "txUtilization": 0,
          "vlanId": "string",
          "networkDeviceId": "string",
          "networkDeviceIpAddress": "string",
          "networkDeviceMacAddress": "string",
          "siteName": "string",
          "siteHierarchy": "string",
          "siteHierarchyId": "string",
          "aggregateAttributes": [
            {
              "name": "string",
              "values": [
                {
                  "key": "string",
                  "value": 0
                }
              ]
            }
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
