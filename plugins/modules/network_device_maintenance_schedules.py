#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_maintenance_schedules
short_description: Resource module for Network Device Maintenance Schedules
description:
  - Manage operations create, update and delete of the resource Network Device Maintenance Schedules. - > API to create maintenance
    schedule for network devices. The state of network device can be queried using API `GET /dna/intent/api/v1/networkDevices`.
    The `managementState` attribute of the network device will be updated to `UNDER_MAINTENANCE` when the maintenance window
    starts. - > API to delete maintenance schedule by id. Deletion is allowed if the maintenance window is in the `UPCOMING`,
    `COMPLETED`, or `FAILED` state. Deletion of maintenance schedule is not allowed if the maintenance window is currently
    `IN_PROGRESS`. To delete the maintenance schedule while it is `IN_PROGRESS`, first exit the current maintenance window
    using `PUT /dna/intent/api/v1/networkDeviceMaintenanceSchedules/{id}` API, and then proceed to delete the maintenance
    schedule.
  - API to update the maintenance schedule for the network devices.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  description:
    description: A brief narrative describing the maintenance schedule.
    type: str
  id:
    description: Id of the schedule maintenance window.
    type: str
  maintenanceSchedule:
    description: Contains all the details necessary to define the maintenance window and its recurrence.
    suboptions:
      endId:
        description: Activity id of end schedule of the maintenance window. To check the status of the end schedule, use `GET
          /dna/intent/api/v1/activities/{id}`. `endId` remains same for every occurrence of recurrence instance.
        type: str
      endTime:
        description: End time indicates the ending of the maintenance window in Unix epoch time in milliseconds.
        type: int
      recurrence:
        description: Details about the recurrence of the maintenance schedule.
        suboptions:
          interval:
            description: Interval for recurrence in days. The interval must be longer than the duration of the schedules.
              The maximum allowed interval is 365 days.
            type: int
          recurrenceEndTime:
            description: The end date for the recurrence in Unix epoch time in milliseconds. Recurrence end time should be
              greater than maintenance end date/time.
            type: int
        type: dict
      startId:
        description: Activity id of start schedule of the maintenance window. To check the status of the start schedule, use
          `GET /dna/intent/api/v1/activities/{id}`. `startId` remains same for every occurrence of recurrence instance.
        type: str
      startTime:
        description: Start time indicates the beginning of the maintenance window in Unix epoch time in milliseconds.
        type: int
      status:
        description: The status of the maintenance schedule. Possible values are - `UPCOMING` The maintenance is scheduled
          and pending execution. - `IN_PROGRESS` The maintenance is currently in progress. - `COMPLETED` The maintenance window
          has been fully completed (For recurring maintenance, this indicates completion of the most recent occurrence). -
          `FAILED` Updating the device's management state was not successful. If the status of startId or endId is `FAILED`,
          this will be indicated as failed. To check the status of startId or endId, refer to `GET /intent/api/v1/activities/{id}`.
        type: str
    type: dict
  networkDeviceIds:
    description: Network Device Maintenance Schedules's networkDeviceIds.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices CreateMaintenanceScheduleForNetworkDevices
    description: Complete reference of the CreateMaintenanceScheduleForNetworkDevices API.
    link: https://developer.cisco.com/docs/dna-center/#!create-maintenance-schedule-for-network-devices
  - name: Cisco Catalyst Center documentation for Devices DeleteMaintenanceSchedule
    description: Complete reference of the DeleteMaintenanceSchedule API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-maintenance-schedule
  - name: Cisco Catalyst Center documentation for Devices UpdatesTheMaintenanceScheduleInformation
    description: Complete reference of the UpdatesTheMaintenanceScheduleInformation API.
    link: https://developer.cisco.com/docs/dna-center/#!updates-the-maintenance-schedule-information
notes:
  - SDK Method used are
    devices.Devices.create_maintenance_schedule_for_network_devices,
    devices.Devices.delete_maintenance_schedule,
    devices.Devices.updates_the_maintenance_schedule_information,
  - Paths used are
    post /dna/intent/api/v1/networkDeviceMaintenanceSchedules,
    delete /dna/intent/api/v1/networkDeviceMaintenanceSchedules/{id},
    put /dna/intent/api/v1/networkDeviceMaintenanceSchedules/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.network_device_maintenance_schedules:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    description: string
    id: string
    maintenanceSchedule:
      endId: string
      endTime: {}
      recurrence:
        interval: 0
        recurrenceEndTime: {}
      startId: string
      startTime: {}
      status: string
    networkDeviceIds:
      - string
- name: Update by id
  cisco.catalystcenter.network_device_maintenance_schedules:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    description: string
    id: string
    maintenanceSchedule:
      endId: string
      endTime: {}
      recurrence:
        interval: 0
        recurrenceEndTime: {}
      startId: string
      startTime: {}
      status: string
    networkDeviceIds:
      - string
- name: Delete by id
  cisco.catalystcenter.network_device_maintenance_schedules:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
