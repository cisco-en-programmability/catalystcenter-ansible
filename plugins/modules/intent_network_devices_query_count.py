#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: intent_network_devices_query_count
short_description: Resource module for Intent Network Devices Query Count
description:
  - Manage operation create of the resource Intent Network Devices Query Count.
  - API to fetch the count of network devices for the given filter query. How.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  filter:
    description: Filter to query network devices. The result will contain the network devices that match ALL the filter criteria
      (AND condition) unless specified in 'logicalOperator'. Total number of filter criteria should not exceed 20.
    suboptions:
      filters:
        description: List of filter criteria to query network devices.
        elements: dict
        suboptions:
          key:
            description: The key to filter by.
            type: str
          operator:
            description: The operator to use for filtering the values. * `eq` - The result will contain the network devices
              that match the exact value. * `contains` - The result will contain the network devices that contain the value.
              * `in` - The result will contain the network devices that match any of the values in the list. * `lt` - The
              result will contain the network devices that are less than the value. * `gt` - The result will contain the network
              devices that are greater than the value. * `lte` - The result will contain the network devices that are less
              than or equal to the value. * `gte` - The result will contain the network devices that are greater than or equal
              to the value.
            type: str
          value:
            description: Value to filter by. For `in` operator, the value should be a list of values.
            type: dict
        type: list
      logicalOperator:
        description: The logical operator to use for combining the filter criteria. If not provided, the default value is
          `AND`. * `AND` - The result will contain the network devices that match ALL the filter criteria. * `OR` - The result
          will contain the network devices that match ANY of the filter criteria.
        type: str
    type: dict
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices CountTheNumberOfNetworkDevicesWithFilters
    description: Complete reference of the CountTheNumberOfNetworkDevicesWithFilters API.
    link: https://developer.cisco.com/docs/dna-center/#!count-the-number-of-network-devices-with-filters
notes:
  - SDK Method used are
    devices.Devices.count_the_number_of_network_devices_with_filters,
  - Paths used are
    post /dna/intent/api/v1/networkDevices/query/count,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.intent_network_devices_query_count:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    filter:
      filters:
        - key: string
          operator: string
          value: {}
      logicalOperator: string
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
