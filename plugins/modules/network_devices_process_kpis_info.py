#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_devices_process_kpis_info
short_description: Information module for Network Devices Process Kpis
description:
  - Get all Network Devices Process Kpis.
  - Get Network Devices Process Kpis by id. - > Retrieves the Process KPIs for a given process of wireless controller. If
    startTime and endTime are not provided, the API defaults to the last 24 hours. - > Retrieves the list of Process CPU and
    Memory KPIs for a given network device. Only the latest top 13 Processes including all WNCD processes are returned. If
    startTime and endTime are not provided, the API defaults to the last 24 hours.
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
  limit:
    description:
      - Limit query parameter. Maximum number of records to return.
    type: int
  offset:
    description:
      - >
        Offset query parameter. Specifies the starting point within all records returned by the API. It's one
        based offset. The starting value is 1.
    type: int
  sortBy:
    description:
      - SortBy query parameter. A field within the response to sort by.
    type: str
  order:
    description:
      - Order query parameter. The sort order of the field ascending or descending.
    type: str
  id:
    description:
      - Id path parameter. Process Name.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices RetrievesTheListOfProcessCPUAndMemoryKPIsForAGivenNetworkDevice
    description: Complete reference of the RetrievesTheListOfProcessCPUAndMemoryKPIsForAGivenNetworkDevice API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-process-cpu-and-memory-kp-is-for-a-given-network-device
  - name: Cisco Catalyst Center documentation for Devices RetrievesTheProcessKPIsForAGivenProcessOfWirelessController
    description: Complete reference of the RetrievesTheProcessKPIsForAGivenProcessOfWirelessController API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-process-kp-is-for-a-given-process-of-wireless-controller
notes:
  - SDK Method used are
    devices.Devices.retrieves_the_list_of_process_cpu_and_memory_kpis_for_a_given_network_device,
    devices.Devices.retrieves_the_process_kpis_for_a_given_process_of_wireless_controller,
  - Paths used are
    get /dna/data/api/v1/networkDevices/{networkDeviceId}/processKpis,
    get /dna/data/api/v1/networkDevices/{networkDeviceId}/processKpis/{id},
"""

EXAMPLES = r"""
---
- name: Get all Network Devices Process Kpis
  cisco.catalystcenter.network_devices_process_kpis_info:
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
    limit: 100
    offset: 1
    sortBy: string
    order: asc
    networkDeviceId: string
  register: result
- name: Get Network Devices Process Kpis by id
  cisco.catalystcenter.network_devices_process_kpis_info:
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
        "siteHierarchy": "string",
        "siteHierarchyId": "string",
        "lastUpdatedTime": 0
      },
      "version": "string"
    }
"""
