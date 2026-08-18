#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_devices_intent_info
short_description: Information module for Network Devices Intent
description:
  - Get all Network Devices Intent.
  - Get Network Devices Intent by id. - > API to fetch the details of network device using the `id`. Use the `/dna/intent/api/v1/networkDevices/query`
    API for advanced filtering. The API supports views. - > API to fetch the list of network devices using basic filters.
    Use the `/dna/intent/api/v1/networkDevices/query` API for advanced filtering. The API supports views to fetch only the
    required fields.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Unique identifier for the network device.
    type: str
  views:
    description:
      - >
        Views query parameter. The specific views being requested. This is an optional parameter which can be
        passed to get one or more of the network device data. If this is not provided, then it will default to
        `BASIC` views. If multiple views are provided, the response will contain the union of the views.
        Attributes covered by the views are * `BASIC` id, managementAddress, dnsResolvedManagementIpAddress,
        hostname, macAddress, serialNumbers, type, family, series, status, platformIds, softwareType,
        softwareVersion, vendor, stackDevice, bootTime, role, roleSource, apEthernetMacAddress,
        apManagerInterfaceIpAddress, apWlcIpAddress, deviceSupportLevel, snmpContact, snmpLocation, secureMode *
        `RESYNC` id, managementAddress, dnsResolvedManagementIpAddress, hostname, macAddress, serialNumbers,
        type, family, series, status, reachabilityStatus, reachabilityFailureReason, managementState,
        lastSuccessfulResyncReasons, resyncStartTime, resyncEndTime, resyncReasons, resyncRequestedByApps,
        pendingResyncRequestCount, pendingResyncRequestReasons, resyncIntervalSource, resyncIntervalMinutes,
        errorCode, errorDescription, secureMode * `USER_DEFINED_FIELDS` id, managementAddress,
        dnsResolvedManagementIpAddress, hostname, macAddress, serialNumbers, type, family, series, status,
        userDefinedFields * `CREDENTIALS` (without sensitive credentials) id, managementAddress,
        dnsResolvedManagementIpAddress, hostname, macAddress, serialNumbers, type, family, series, status,
        credentials, category Note `CREDENTIALS` view only returns the non-sensitive credentials of the network
        device. The sensitive credentials are not returned in the response.
    elements: str
    type: list
  managementAddress:
    description:
      - ManagementAddress query parameter. Management address of the network device.
    type: str
  serialNumber:
    description:
      - SerialNumber query parameter. Serial number of the network device.
    type: str
  family:
    description:
      - Family query parameter. Product family of the network device. For example, Switches, Routers, etc.
    type: str
  stackDevice:
    description:
      - StackDevice query parameter. Flag indicating if the device is a stack device.
    type: bool
  role:
    description:
      - Role query parameter. Role assigned to the network device.
    type: str
  status:
    description:
      - >
        Status query parameter. Inventory related status of the network device. | status | Description | |
        ---------------------- | -------------------------------------------------------------------------------
        --------------------------------------------------------------------------------------------------------
        ------------------ | | `MANAGED` | The device is successfully managed. | | `SYNC_NOT_STARTED` | Sync
        request is queued and pending processing. | | `SYNC_INIT_FAILED` | Sync initialization failed due to
        bootstrap issues. | | `SYNC_PRECHECK_FAILED` | Device failed to meet necessary preconditions for sync. |
        | `SYNC_IN_PROGRESS` | Sync with the device is in progress. | | `SYNC_INTERNAL_ERROR` | Encountered an
        internal error during data collection, potentially leading to incomplete or outdated device information.
        | | `SYNC_DISABLED` | Sync has been disabled on the device. | | `DELETING_DEVICE` | The device is being
        deleted from Catalyst Center. | | `UNDER_MAINTENANCE` | The device is in maintenance mode. Assurance
        will not raise alerts when the network device is in maintenance mode. | | `QUARANTINED` | The device is
        in quarantined state. Inventory sync and provisioning are disabled for the device. | | `UNASSOCIATED` |
        Access point is not associated with any WLC. | | `UNREACHABLE` | The device is not reachable by either
        SNMP/HTTP/NETCONF or ICMP. | | `UNKNOWN` | All information from the device could not be collected, or
        inventory collection was not started. It may be a temporary issue. Attempt to resync the device, and if
        the error persists, contact Cisco TAC. |.
    type: str
  reachabilityStatus:
    description:
      - >
        ReachabilityStatus query parameter. Reachability status of the network device. Possible values are *
        `REACHABLE` - Device is reachable by SNMP (in case of network device) or HTTP (in case of compute device
        or Meraki device). * `ONLY_PING_REACHABLE` - Mandatory protocol (SNMP/HTTP/NETCONF) failed for the
        device. The device is reachable only by ICMP. * `UNREACHABLE` - Device is not reachable by either
        SNMP/HTTP or ICMP. * `UNKNOWN` - Device reachability status can't be determined. The product hasn't
        interacted with the device yet, or the parent device that controls the device is unreachable.
    type: str
  managementState:
    description:
      - >
        ManagementState query parameter. The status of the network device's manageability. Possible values are *
        `MANAGED` Device is managed. * `UNDER_MAINTENANCE` Device is in service maintenance. * `NEVER_MANAGED`
        Device has never been managed.
    type: str
  secureMode:
    description:
      - SecureMode query parameter. Security mode of the network device.
    type: str
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: int
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
  sortBy:
    description:
      - SortBy query parameter. A property within the response to sort by.
    type: str
  order:
    description:
      - Order query parameter. Whether ascending or descending order should be used to sort the response.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices GetDetailsOfASingleNetworkDevice
    description: Complete reference of the GetDetailsOfASingleNetworkDevice API.
    link: https://developer.cisco.com/docs/dna-center/#!get-details-of-a-single-network-device
  - name: Cisco Catalyst Center documentation for Devices RetrieveNetworkDevices
    description: Complete reference of the RetrieveNetworkDevices API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-network-devices
notes:
  - SDK Method used are
    devices.Devices.get_details_of_a_single_network_device,
    devices.Devices.retrieve_network_devices,
  - Paths used are
    get /dna/intent/api/v1/networkDevices,
    get /dna/intent/api/v1/networkDevices/{id},
"""

EXAMPLES = r"""
---
- name: Get all Network Devices Intent
  cisco.catalystcenter.network_devices_intent_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: e910e834-e35b-4800-9401-a40e22ce09f3
    managementAddress: 1.1.1.1
    serialNumber: FDO20120QWY
    family: Switch
    stackDevice: True
    role: ACCESS
    status: string
    reachabilityStatus: REACHABLE
    managementState: MANAGED
    secureMode: UNKNOWN
    views: ['BASIC']
    limit: 0
    offset: 1
    sortBy: macAddress
    order: asc
  register: result
- name: Get Network Devices Intent by id
  cisco.catalystcenter.network_devices_intent_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    views: ['BASIC']
    id: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {},
      "version": "string"
    }
"""
