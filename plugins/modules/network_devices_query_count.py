#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_devices_query_count
short_description: Resource module for Network Devices Query Count
description:
  - Manage operation create of the resource Network Devices Query Count.
  - Gets the total number Network Devices based on the provided complex filters and aggregation functions.
  - For detailed information about the usage of the API, please refer to the Open API specification document
    https //github.com/cisco-en-programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceNetworkDevices-2.0.1-resolved.yaml.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  endTime:
    description: End Time.
    type: int
  filters:
    description: Network Devices Query Count's filters.
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
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Devices GetsTheTotalNumberNetworkDevicesBasedOnTheProvidedComplexFiltersAndAggregationFunctions
    description: Complete reference of the GetsTheTotalNumberNetworkDevicesBasedOnTheProvidedComplexFiltersAndAggregationFunctions
      API.
    link: https://developer.cisco.com/docs/dna-center/#!gets-the-total-number-network-devices-based-on-the-provided-complex-filters-and-aggregation-functions
notes:
  - SDK Method used are
    devices.Devices.gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions,
  - Paths used are
    post /dna/data/api/v1/networkDevices/query/count,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.network_devices_query_count:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    endTime: 0
    filters:
      - key: string
        operator: string
        value: string
    startTime: 0
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
