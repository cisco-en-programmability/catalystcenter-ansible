#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_maintenance_schedules_count_info
short_description: Information module for Network Device Maintenance Schedules Count
description:
  - Get all Network Device Maintenance Schedules Count.
  - Retrieve the total count of all scheduled maintenance windows for network devices.
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
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices RetrieveTheTotalNumberOfScheduledMaintenanceWindows
    description: Complete reference of the RetrieveTheTotalNumberOfScheduledMaintenanceWindows API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-total-number-of-scheduled-maintenance-windows
notes:
  - SDK Method used are
    devices.Devices.retrieve_the_total_number_of_scheduled_maintenance_windows,
  - Paths used are
    get /dna/intent/api/v1/networkDeviceMaintenanceSchedules/count,
"""

EXAMPLES = r"""
---
- name: Get all Network Device Maintenance Schedules Count
  cisco.catalystcenter.network_device_maintenance_schedules_count_info:
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
