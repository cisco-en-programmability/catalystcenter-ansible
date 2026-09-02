#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_stats_info
short_description: Information module for Wireless Controllers Stats
description:
  - Get all Wireless Controllers Stats.
  - Get Wireless Controllers Stats by id. - > Retrieves the list of Wireless Controllers' statistics. If startTime and endTime
    are not provided, the API defaults to the last 24 hours. - > Retrieves the statistics of a given Wireless Controller.
    If startTime and endTime are not provided, the API defaults to the last 24 hours.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
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
  view:
    description:
      - >
        View query parameter. WLC Stats related Views Refer to WlcStatsView schema for list of views supported
        Examples `view=ClientBandCounts` (single view requested)
        `view=clientAssociationCounts&view=clientStateCounts` (multiple view requested).
    elements: str
    type: list
  attribute:
    description:
      - >
        Attribute query parameter. List of attributes related to resource that can be requested to only be part
        of the response along with the required attributes. Refer to WlcStatsAttribute schema for list of
        attributes supported Examples `attribute=totalClientCount` (single attribute requested)
        `attribute=totalClientCount&attribute=clientRoamCounts` (multiple attribute requested).
    elements: str
    type: list
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
      - Id path parameter. The WLC device UUID.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices RetrievesTheListOfWirelessControllersStatistics
    description: Complete reference of the RetrievesTheListOfWirelessControllersStatistics API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-wireless-controllers-statistics
  - name: Cisco Catalyst Center documentation for Devices RetrievesTheStatisticsOfAGivenWirelessController
    description: Complete reference of the RetrievesTheStatisticsOfAGivenWirelessController API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-statistics-of-a-given-wireless-controller
notes:
  - SDK Method used are
    devices.Devices.retrieves_the_list_of_wireless_controllers_statistics,
    devices.Devices.retrieves_the_statistics_of_a_given_wireless_controller,
  - Paths used are
    get /dna/data/api/v1/wirelessControllersStats,
    get /dna/data/api/v1/wirelessControllersStats/{id},
"""

EXAMPLES = r"""
---
- name: Get all Wireless Controllers Stats
  cisco.catalystcenter.wireless_controllers_stats_info:
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
    view: []
    attribute: []
    limit: 100
    offset: 1
    sortBy: string
    order: asc
  register: result
- name: Get Wireless Controllers Stats by id
  cisco.catalystcenter.wireless_controllers_stats_info:
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
    view: []
    attribute: []
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
        "name": "string",
        "siteHierarchy": "string",
        "siteHierarchyId": "string",
        "lastUpdatedTime": 0
      },
      "version": "string"
    }
"""
