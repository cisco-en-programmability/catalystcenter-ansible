#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_devices_intent_count_info
short_description: Information module for Network Devices Intent Count
description:
  - Get all Network Devices Intent Count. - > API to fetch the count of network devices using basic filters. Use the
      `/dna/intent/api/v1/networkDevices/query/count`
    API if you need advanced filtering.
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
      - Id query parameter. Network device Id.
    type: str
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
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices CountTheNumberOfNetworkDevices
    description: Complete reference of the CountTheNumberOfNetworkDevices API.
    link: https://developer.cisco.com/docs/dna-center/#!count-the-number-of-network-devices
notes:
  - SDK Method used are
    devices.Devices.count_the_number_of_network_devices,
  - Paths used are
    get /dna/intent/api/v1/networkDevices/count,
"""

EXAMPLES = r"""
---
- name: Get all Network Devices Intent Count
  cisco.catalystcenter.network_devices_intent_count_info:
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
    stackDevice: true
    role: ACCESS
    status: string
    reachabilityStatus: REACHABLE
    managementState: MANAGED
    secureMode: UNKNOWN
  register: result
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
