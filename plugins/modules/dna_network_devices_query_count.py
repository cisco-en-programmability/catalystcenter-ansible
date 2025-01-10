#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: dna_network_devices_query_count
short_description: Resource module for Dna Network Devices Query Count
description:
- This module represents an alias of the module dna_network_devices_query_count_v1
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  endTime:
    description: End Time.
    type: int
  filters:
    description: Dna Network Devices Query Count's filters.
    elements: dict
    suboptions:
      key:
        description: Key.
        type: str
      operator:
        description: Operator.
        type: str
      value:
        description: Value.
        type: str
    type: list
  startTime:
    description: Start Time.
    type: int
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices GetsTheTotalNumberNetworkDevicesBasedOnTheProvidedComplexFiltersAndAggregationFunctionsV1
  description: Complete reference of the GetsTheTotalNumberNetworkDevicesBasedOnTheProvidedComplexFiltersAndAggregationFunctionsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!gets-the-total-number-network-devices-based-on-the-provided-complex-filters-and-aggregation-functions
notes:
  - SDK Method used are
    devices.Devices.gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1,

  - Paths used are
    post /dna/data/api/v1/networkDevices/query/count,
  - It should be noted that this module is an alias of dna_network_devices_query_count_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.dna_network_devices_query_count:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    endTime: 0
    filters:
    - key: string
      operator: string
      value: string
    startTime: 0

"""
RETURN = r"""
catalystcenter_response:
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
