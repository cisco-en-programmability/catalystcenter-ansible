#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_licenses_query_create
short_description: Resource module for Network Device Licenses Query Create
description:
  - Manage operation create of the resource Network Device Licenses Query Create.
  - API to retrieve the list of network devices and their licenses, determined by the filters.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  filter:
    description: Network Device Licenses Query Create's filter.
    suboptions:
      filters:
        description: List of filter criteria to query network devices.
        elements: dict
        suboptions:
          key:
            description: The key to filter by.
            type: str
          operator:
            description: The operator to use for filtering the values. | Operator | Description |
                |-----------|--------------------------------------------------------------------------...
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
  page:
    description: Query filter for pagination and sorting.
    suboptions:
      limit:
        description: The maximum number of items to return in a single response. This determines the size of each "page" of
          results. For example, a value of 10 will return up to 10 items. The maximum allowed value is 500.
        type: int
      offset:
        description: The number of items to skip before starting to collect the result set. Use this to retrieve subsequent
          "pages" of results. For example, an offset of 10 will skip the first 10 items.
        type: int
      sortBy:
        description: A property within the response to sort by.
        suboptions:
          name:
            description: The name of the field to sort by.
            type: str
          order:
            description: The sort order.
            type: str
        type: dict
    type: dict
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Licenses QueryNetworkDevicesLicensesWithFilters
    description: Complete reference of the QueryNetworkDevicesLicensesWithFilters API.
    link: https://developer.cisco.com/docs/dna-center/#!query-network-devices-licenses-with-filters
notes:
  - SDK Method used are
    licenses.Licenses.query_network_devices_licenses_with_filters,
  - Paths used are
    post /dna/intent/api/v1/networkDeviceLicenses/query,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.network_device_licenses_query_create:
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
    page:
      limit: 0
      offset: 0
      sortBy:
        name: string
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
          "managementAddress": {},
          "hostname": "string",
          "family": "string",
          "series": "string",
          "siteHierarchy": "string",
          "softwareVersion": "string",
          "licenseMode": "string",
          "licenses": [
            {
              "type": "string",
              "name": "string",
              "status": "string",
              "count": 0,
              "owned": true,
              "evaluationExpiryTime": {}
            }
          ],
          "licenseLevel": "string",
          "triggerReboot": true,
          "changeWirelessLicense": true,
          "registrationStatus": "string",
          "authorizationStatus": "string",
          "smartAccountId": "string",
          "virtualAccountId": "string",
          "customerTags": {
            "tag1": "string",
            "tag2": "string",
            "tag3": "string",
            "tag4": "string"
          },
          "authCodeStatus": "string",
          "throughputValue": "string",
          "lastSuccessfulUsageReportingTime": {},
          "licenseManagedBy": "string",
          "wirelessCapable": true,
          "networkDeviceId": "string"
        }
      ],
      "version": "string"
    }
"""
