#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: path_traces_count_info
short_description: Information module for Path Traces Count
description:
  - Get all Path Traces Count.
  - Returns the count of path traces that match the specified filter parameters.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  periodicRefresh:
    description:
      - >
        PeriodicRefresh query parameter. Indicates whether the analysis is periodically refreshed. | false |
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
      - Protocol query parameter. Protocol used in the path trace. | UDP | User Datagram Protocol |.
    type: str
  status:
    description:
      - >
        Status query parameter. Status of the path trace. | SCHEDULED | Path trace is scheduled to run | |
        PENDING | Path trace is pending execution | | COMPLETED | Path trace has completed |.
    type: str
  lastUpdateTime:
    description:
      - >
        LastUpdateTime query parameter. Retrieves analyses that were last updated at this time. Value is in
        epoch milliseconds.
    type: float
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Path Trace RetrievesTheCountOfPathTracesMatchingFilterCriteria
    description: Complete reference of the RetrievesTheCountOfPathTracesMatchingFilterCriteria API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-count-of-path-traces-matching-filter-criteria
notes:
  - SDK Method used are
    path_trace.PathTrace.retrieves_the_count_of_path_traces_matching_filter_criteria,
  - Paths used are
    get /dna/intent/api/v1/pathTraces/count,
"""

EXAMPLES = r"""
---
- name: Get all Path Traces Count
  cisco.catalystcenter.path_traces_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    periodicRefresh: true
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
