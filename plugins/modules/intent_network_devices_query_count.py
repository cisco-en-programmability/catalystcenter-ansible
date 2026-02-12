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
  - API to fetch the count of network devices for the given filter query.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  filter:
    description: Intent Network Devices Query Count's filter.
    suboptions:
      filters:
        description: Intent Network Devices Query Count's filters.
        elements: dict
        suboptions:
          key:
            description: The key to filter by.
            type: str
          operator:
            description: The operator to use for filtering the values.
            type: str
          value:
            description: Value to filter by. For `in` operator, the value should be a list of values.
            type: dict
        type: list
      logicalOperator:
        description: The logical operator to use for combining the filter criteria. If not provided, the default value is
          AND.
        type: str
    type: dict
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Devices CountTheNumberOfNetworkDevicesWithFilters
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
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
