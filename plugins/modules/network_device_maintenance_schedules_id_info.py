#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_device_maintenance_schedules_id_info
short_description: Information module for Network Device Maintenance Schedules Id
  Info
description:
  - This module represents an alias of the module network_device_maintenance_schedules_id_v1_info
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Unique identifier for the maintenance schedule.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices RetrievesTheMaintenanceScheduleInformationV1
    description: Complete reference of the RetrievesTheMaintenanceScheduleInformationV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!retrieves-the-maintenance-schedule-information
notes:
  - SDK Method used are devices.Devices.retrieves_the_maintenance_schedule_information_v1,
  - Paths used are get /dna/intent/api/v1/networkDeviceMaintenanceSchedules/{id},
  - It should be noted that this module is an alias of network_device_maintenance_schedules_id_v1_info
"""
EXAMPLES = r"""
- name: Get Network Device Maintenance Schedules Id Info by id
  cisco.catalystcenter.network_device_maintenance_schedules_id_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
          "startTime": 0,
          "endTime": 0,
          "recurrence": {
            "interval": 0,
            "recurrenceEndTime": 0
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
