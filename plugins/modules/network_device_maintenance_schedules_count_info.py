#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_device_maintenance_schedules_count_info
short_description: Information module for Network Device Maintenance Schedules Count
  Info
description:
  - This module represents an alias of the module network_device_maintenance_schedules_count_v1_info
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
      - NetworkDeviceIds query parameter. List of network device ids.
    type: str
  status:
    description:
      - >
        Status query parameter. The status of the maintenance schedule. Possible values
        are UPCOMING, IN_PROGRESS,
        COMPLETED, FAILED. Refer features for more details.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices RetrieveTheTotalNumberOfScheduledMaintenanceWindowsV1
    description: Complete reference of the RetrieveTheTotalNumberOfScheduledMaintenanceWindowsV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!retrieve-the-total-number-of-scheduled-maintenance-windows
notes:
  - SDK Method used are devices.Devices.retrieve_the_total_number_of_scheduled_maintenance_windows_v1,
  - Paths used are get /dna/intent/api/v1/networkDeviceMaintenanceSchedules/count,
  - It should be noted that this module is an alias of network_device_maintenance_schedules_count_v1_info
"""
EXAMPLES = r"""
- name: Get all Network Device Maintenance Schedules Count Info
  cisco.catalystcenter.network_device_maintenance_schedules_count_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    networkDeviceIds: string
    status: string
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
        "count": 0
      },
      "version": "string"
    }
"""
