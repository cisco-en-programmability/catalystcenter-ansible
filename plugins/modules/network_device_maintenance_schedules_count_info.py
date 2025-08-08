#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_maintenance_schedules_count_info
short_description: Information module for Network Device
  Maintenance Schedules Count
description:
  - Get all Network Device Maintenance Schedules Count.
  - Retrieve the total count of all scheduled maintenance
    windows for network devices.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  networkDeviceIds:
    description:
      - NetworkDeviceIds query parameter. List of network
        device ids.
    type: str
  status:
    description:
      - >
        Status query parameter. The status of the maintenance
        schedule. Possible values are UPCOMING, IN_PROGRESS,
        COMPLETED, FAILED. Refer features for more details.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices
      RetrieveTheTotalNumberOfScheduledMaintenanceWindows
    description: Complete reference of the RetrieveTheTotalNumberOfScheduledMaintenanceWindows
      API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-total-number-of-scheduled-maintenance-windows
notes:
  - SDK Method used are
    devices.Devices.retrieve_the_total_number_of_scheduled_maintenance_windows,
  - Paths used are
    get /dna/intent/api/v1/networkDeviceMaintenanceSchedules/count,
"""

EXAMPLES = r"""
---
- name: Get all Network Device Maintenance Schedules
    Count
  cisco.catalystcenter.network_device_maintenance_schedules_count_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
    networkDeviceIds: string
    status: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
