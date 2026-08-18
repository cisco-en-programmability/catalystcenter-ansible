#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_licenses_query_count_create
short_description: Resource module for Network Device Licenses Query Count Create
description:
  - Manage operation create of the resource Network Device Licenses Query Count Create.
  - API to retrieve the number of network devices, determined by the filters.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  filter:
    description: Filter to query network devices. The result will contain the network devices that match all the filter criteria
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
            description: The operator to use for filtering the values. | Operator | Description | |-----------|--------------------------------------------------------------------------...
              | `eq` | The result will include entities whose attribute values have the network devices that match the exact
              value. | | `contains`| The result will include entities whose attribute values have the network devices that
              contain the value. | | `in` | The result will include entities whose attribute values match any of the values
              in the list. | | `lt` | The result will include entities whose attribute values are less than the specified
              value. | | `gt` | The result will include entities whose attribute values are greater than the specified value.
              | | `lte` | The result will include entities whose attribute values are less than or equal to the specified
              value. | | `gte` | The result will include entities whose attribute values are greater than or equal to the
              specified value. |.
            type: str
          value:
            description: Value to filter by. For `in` operator, the value should be a list of values.
            type: dict
        type: list
      logicalOperator:
        description: The logical operator to use for combining the filter criteria. If not provided, the default value is
          `AND`. | Logical operator | Description | |-------------|----------------------------------------------------------------------------------------...
          | `AND` | The result will contain the network devices that match all the filter criteria. | | `OR` | The result
          will contain the network devices that match ANY of the filter criteria. |.
        type: str
    type: dict
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Licenses QueryNetworkDevicesLicensesCountWithFilters
    description: Complete reference of the QueryNetworkDevicesLicensesCountWithFilters API.
    link: https://developer.cisco.com/docs/dna-center/#!query-network-devices-licenses-count-with-filters
notes:
  - SDK Method used are
    licenses.Licenses.query_network_devices_licenses_count_with_filters,
  - Paths used are
    post /dna/intent/api/v1/networkDeviceLicenses/query/count,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.network_device_licenses_query_count_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    filter: {}
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
