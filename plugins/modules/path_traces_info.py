#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: path_traces_info
short_description: Information module for Path Traces
description:
  - Get all Path Traces.
  - Get Path Traces by id.
  - Returns a summary of a specific path trace by its ID without the detailed path trace information.
  - Returns a summary of all path traces stored. Results can be filtered by specified parameters.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Unique identifier for the path trace request summary to be retrieved.
    type: str
  periodicRefresh:
    description:
      - >
        PeriodicRefresh query parameter. Indicates whether the analysis is periodically refreshed. | Value |
        Description | | ----- | ----------- | | true | Analysis is refreshed every 30 seconds | | false |
        Analysis is performed once |.
    type: bool
  sourceIpAddress:
    description:
      - >
        SourceIpAddress query parameter. Source IP address used in the path trace. Format can be IPv4 (e.g.,
        192.168.1.1) or IPv6.
    type: str
  sourceMacAddress:
    description:
      - >
        SourceMacAddress query parameter. Source MAC address used in the path trace. Format should be XX XX XX
        XX XX XX (e.g., 00 1A 2B 3C 4D 5E).
    type: str
  destinationIpAddress:
    description:
      - >
        DestinationIpAddress query parameter. Destination IP address used in the path trace. Format can be IPv4
        (e.g., 192.168.1.1) or IPv6.
    type: str
  destinationMacAddress:
    description:
      - >
        DestinationMacAddress query parameter. Destination MAC address used in the path trace. Format should be
        XX XX XX XX XX XX (e.g., 00 1A 2B 3C 4D 5E).
    type: str
  sourcePort:
    description:
      - SourcePort query parameter. Source port used in the path trace. Valid range is 1-65535.
    type: float
  destinationPort:
    description:
      - DestinationPort query parameter. Destination port used in the path trace. Valid range is 1-65535.
    type: float
  greaterThanCreateTime:
    description:
      - >
        GreaterThanCreateTime query parameter. Retrieves analyses requested after this time. Value is in epoch
        milliseconds.
    type: float
  lessThanCreateTime:
    description:
      - LessThanCreateTime query parameter. Retrieves analyses requested before this time. Value is in epoch milliseconds.
    type: float
  protocol:
    description:
      - >
        Protocol query parameter. Protocol used in the path trace. | Value | Description | | ----- | -----------
        | | TCP | Transmission Control Protocol | | UDP | User Datagram Protocol |.
    type: str
  status:
    description:
      - >
        Status query parameter. Status of the path trace. | Value | Description | | ----- | ----------- | |
        SUCCESS | Path trace completed successfully | | INPROGRESS | Path trace is currently running | | FAILED
        | Path trace failed to complete | | SCHEDULED | Path trace is scheduled to run | | PENDING | Path trace
        is pending execution | | COMPLETED | Path trace has completed |.
    type: str
  lastUpdateTime:
    description:
      - >
        LastUpdateTime query parameter. Retrieves analyses that were last updated at this time. Value is in
        epoch milliseconds.
    type: float
  limit:
    description:
      - Limit query parameter. Maximum number of resources to return in the response. Use for pagination.
    type: int
  offset:
    description:
      - Offset query parameter. Starting index of resources to be returned (1-based). Use for pagination.
    type: int
  order:
    description:
      - >
        Order query parameter. Sorting order for the returned results. | Value | Description | | ----- |
        ----------- | | asc | Ascending order | | desc | Descending order |.
    type: str
  sortBy:
    description:
      - >
        SortBy query parameter. Field to sort the results by. Common values include createTime, status,
        sourceIpAddress, destinationIpAddress.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Path Trace RetrievesTheSummaryOfASpecificPathTrace
    description: Complete reference of the RetrievesTheSummaryOfASpecificPathTrace API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-summary-of-a-specific-path-trace
  - name: Cisco Catalyst Center documentation for Path Trace RetrievesTheSummaryOfAllPreviousPathTraces
    description: Complete reference of the RetrievesTheSummaryOfAllPreviousPathTraces API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-summary-of-all-previous-path-traces
notes:
  - SDK Method used are
    path_trace.PathTrace.retrieves_the_summary_of_a_specific_path_trace,
    path_trace.PathTrace.retrieves_the_summary_of_all_previous_path_traces,
  - Paths used are
    get /dna/intent/api/v1/pathTraces,
    get /dna/intent/api/v1/pathTraces/{id},
"""

EXAMPLES = r"""
---
- name: Get all Path Traces
  cisco.catalystcenter.path_traces_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    periodicRefresh: True
    sourceIpAddress: 10.1.15.10
    sourceMacAddress: 00:1A:2B:3C:4D:5E
    destinationIpAddress: 10.1.25.10
    destinationMacAddress: AA:BB:CC:DD:EE:FF
    sourcePort: 443
    destinationPort: 8080
    greaterThanCreateTime: 1625097600000
    lessThanCreateTime: 1627776000000
    protocol: TCP
    status: SUCCESS
    lastUpdateTime: 1625184000000
    limit: 50
    offset: 1
    order: desc
    sortBy: createTime
  register: result
- name: Get Path Traces by id
  cisco.catalystcenter.path_traces_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: fad5db1e-8c2a-4bf8-94a5-1fa498c4d651
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
        "controlPath": true,
        "createTime": 0,
        "destinationIpAddress": "string",
        "destinationPort": "string",
        "destinationMacAddress": "string",
        "failureReason": "string",
        "id": "string",
        "inclusions": [
          "string"
        ],
        "lastUpdateTime": 0,
        "periodicRefresh": true,
        "protocol": "string",
        "sourceIpAddress": "string",
        "sourcePort": "string",
        "sourceMacAddress": "string",
        "status": "string",
        "previousPathTraceId": "string"
      },
      "version": "string"
    }
"""
