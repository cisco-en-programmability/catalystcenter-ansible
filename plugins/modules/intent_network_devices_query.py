#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: intent_network_devices_query
short_description: Resource module for Intent Network Devices Query
description:
  - Manage operation create of the resource Intent Network Devices Query.
  - Returns the list of network devices, determined by the filters. It is possible.
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
  page:
    description: Pagination related parameters. This is an optional parameter which can be passed to get the paginated response.
    suboptions:
      limit:
        description: The number of records to show for this page.
        type: int
      offset:
        description: The first record to show for this page; the first record is numbered 1.
        type: int
      sortBy:
        description: The field to sort by. The default sorting field is `hostname`. The order is ascending by default.
        suboptions:
          name:
            description: The field to sort by.
            type: str
          order:
            description: The order to sort by Possible values are * `asc` - Ascending order * `des` - Descending order.
            type: str
        type: dict
    type: dict
  views:
    description: The specific views being requested. This is an optional parameter which can be passed to get one or more
      of the network device data. If this is not provided, then it will default to `BASIC` views. If multiple views are provided,
      the response will contain the union of the views. Attributes covered by the views are Attributes covered by the views
      are * `BASIC` id, managementAddress, dnsResolvedManagementIpAddress, hostname, macAddress, serialNumbers, type, family,
      series, status, platformIds, softwareType, softwareVersion, vendor, stackDevice, bootTime, role, roleSource, apEthernetMacAddress,
      apManagerInterfaceIpAddress, apWlcIpAddress, deviceSupportLevel, snmpContact, snmpLocation, secureMode * `RESYNC` id,
      managementAddress, dnsResolvedManagementIpAddress, hostname, macAddress, serialNumbers, type, family, series, status,
      reachabilityStatus, reachabilityFailureReason, managementState, lastSuccessfulResyncReasons, resyncStartTime, resyncEndTime,
      resyncReasons, resyncRequestedByApps, pendingResyncRequestCount, pendingResyncRequestReasons, resyncIntervalSource,
      resyncIntervalMinutes, errorCode, errorDescription, secureMode * `USER_DEFINED_FIELDS` id, managementAddress, dnsResolvedManagementIpAddress,
      hostname, macAddress, serialNumbers, type, family, series, status, userDefinedFields.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices QueryNetworkDevicesWithFilters
    description: Complete reference of the QueryNetworkDevicesWithFilters API.
    link: https://developer.cisco.com/docs/dna-center/#!query-network-devices-with-filters
notes:
  - SDK Method used are
    devices.Devices.query_network_devices_with_filters,
  - Paths used are
    post /dna/intent/api/v1/networkDevices/query,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.intent_network_devices_query:
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
          "managementAddress": {},
          "dnsResolvedManagementIpAddress": {},
          "hostname": "string",
          "macAddress": "string",
          "serialNumbers": [
            "string"
          ],
          "type": "string",
          "family": "string",
          "series": "string",
          "status": "string",
          "platformIds": "string",
          "softwareType": "string",
          "softwareVersion": "string",
          "vendor": "string",
          "stackDevice": true,
          "bootTime": {},
          "role": "string",
          "roleSource": "string",
          "apEthernetMacAddress": "string",
          "apManagerInterfaceIpAddress": {},
          "apWlcIpAddress": {},
          "deviceSupportLevel": "string",
          "snmpLocation": "string",
          "snmpContact": "string",
          "secureMode": "string",
          "reachabilityStatus": "string",
          "reachabilityFailureReason": "string",
          "managementState": "string",
          "lastSuccessfulResyncReasons": [
            "string"
          ],
          "resyncStartTime": {},
          "resyncEndTime": {},
          "resyncReasons": [
            "string"
          ],
          "resyncRequestedByApps": [
            "string"
          ],
          "pendingResyncRequestCount": 0,
          "pendingResyncRequestReasons": [
            "string"
          ],
          "resyncIntervalSource": "string",
          "resyncIntervalMinutes": 0,
          "errorCode": "string",
          "errorDescription": "string",
          "userDefinedFields": {}
        }
      ],
      "version": "string"
    }
"""
