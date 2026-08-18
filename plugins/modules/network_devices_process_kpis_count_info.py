#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_devices_process_kpis_count_info
short_description: Information module for Network Devices Process Kpis Count
description:
  - Get all Network Devices Process Kpis Count. - > Retrieves the number of Processes by applying basic filtering. If startTime
    and endTime are not provided, the API defaults to the last 24 hours.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  networkDeviceId:
    description:
      - NetworkDeviceId path parameter. Network Device UUID.
    type: str
  startTime:
    description:
      - >
        StartTime query parameter. Start time from which API queries the data set related to the resource. It
        must be specified in UNIX epochtime in milliseconds. Value is inclusive.
    type: int
  endTime:
    description:
      - >
        EndTime query parameter. End time to which API queries the data set related to the resource. It must be
        specified in UNIX epochtime in milliseconds. Value is inclusive.
    type: int
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices RetrievesTheTotalCountOfProcessesByApplyingBasicFiltering
    description: Complete reference of the RetrievesTheTotalCountOfProcessesByApplyingBasicFiltering API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-total-count-of-processes-by-applying-basic-filtering
notes:
  - SDK Method used are
    devices.Devices.retrieves_the_total_count_of_processes_by_applying_basic_filtering,
  - Paths used are
    get /dna/data/api/v1/networkDevices/{networkDeviceId}/processKpis/count,
"""

EXAMPLES = r"""
---
- name: Get all Network Devices Process Kpis Count
  cisco.catalystcenter.network_devices_process_kpis_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    startTime: 0
    endTime: 0
    networkDeviceId: string
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
