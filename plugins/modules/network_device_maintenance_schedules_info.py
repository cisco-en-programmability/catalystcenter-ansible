#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_maintenance_schedules_info
short_description: Information module for Network Device Maintenance Schedules
description:
  - Get all Network Device Maintenance Schedules.
  - Get Network Device Maintenance Schedules by id.
  - API to retrieve the maintenance schedule information for the given id. - > This API retrieves a list of scheduled maintenance
    windows for network devices based on filter parameters. Each maintenance window is composed of a start schedule and end
    schedule, both of which have unique identifiers `startId` and `endId`. These identifiers can be used to fetch the status
    of the start schedule and end schedule using the `GET /dna/intent/api/v1/activities/{id}` API. Completed maintenance schedules
    are automatically removed from the system after two weeks.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  networkDeviceIds:
    description:
      - NetworkDeviceIds query parameter. List of network device ids.
    elements: str
    type: list
  status:
    description:
      - >
        Status query parameter. The status of the maintenance schedule. Possible values are - `UPCOMING` The
        maintenance is scheduled and pending execution. - `IN_PROGRESS` The maintenance is currently in
        progress. - `COMPLETED` The maintenance window has been fully completed (For recurring maintenance, this
        indicates completion of the most recent occurrence). - `FAILED` Updating the device's management state
        was not successful. For more information on failure use `GET /dna/intent/api/v1/activities/{id}` API
        with `startId` and `endId` value.
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
  id:
    description:
      - Id path parameter. Unique identifier for the maintenance schedule.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices RetrieveScheduledMaintenanceWindowsForNetworkDevices
    description: Complete reference of the RetrieveScheduledMaintenanceWindowsForNetworkDevices API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-scheduled-maintenance-windows-for-network-devices
  - name: Cisco Catalyst Center documentation for Devices RetrievesTheMaintenanceScheduleInformation
    description: Complete reference of the RetrievesTheMaintenanceScheduleInformation API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-maintenance-schedule-information
notes:
  - SDK Method used are
    devices.Devices.retrieve_scheduled_maintenance_windows_for_network_devices,
    devices.Devices.retrieves_the_maintenance_schedule_information,
  - Paths used are
    get /dna/intent/api/v1/networkDeviceMaintenanceSchedules,
    get /dna/intent/api/v1/networkDeviceMaintenanceSchedules/{id},
"""

EXAMPLES = r"""
---
- name: Get all Network Device Maintenance Schedules
  cisco.catalystcenter.network_device_maintenance_schedules_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    networkDeviceIds: []
    status: string
    limit: 0
    offset: 1
    sortBy: string
    order: asc
  register: result
- name: Get Network Device Maintenance Schedules by id
  cisco.catalystcenter.network_device_maintenance_schedules_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
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
      "response": {
        "id": "string",
        "description": "string",
        "maintenanceSchedule": {
          "startId": "string",
          "endId": "string",
          "startTime": {},
          "endTime": {},
          "recurrence": {
            "interval": 0,
            "recurrenceEndTime": {}
          },
          "status": "string"
        },
        "networkDeviceIds": [
          "string"
        ]
      },
      "version": "string"
    }
"""
