#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: path_traces
short_description: Resource module for Path Traces
description:
  - Manage operations create and delete of the resource Path Traces.
  - Initiates a new path trace with periodic refresh and stat collection options.
  - Deletes a path trace request by its id.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  controlPath:
    description: Indicates whether to perform control path tracing. Control path traces follow routing table decisions rather
      than data path forwarding decisions. | Value | Description | | ----- | ----------- | | true | Trace control path | |
      false | Trace data path (default) |.
    type: bool
  destinationIpAddress:
    description: Destination IP address for the path trace. Format can be IPv4 (e.g., 192.168.1.1) or IPv6.
    type: str
  destinationMacAddress:
    description: Destination MAC address for the path trace. Format should be XX XX XX XX XX XX (e.g., 00 1A 2B 3C 4D 5E).
    type: str
  destinationPort:
    description: Destination port for the path trace. Must be between 1-65535.
    type: str
  id:
    description: Id path parameter. Unique identifier for the path trace request to be deleted.
    type: str
  inclusions:
    description: Additional data to include in the path trace results. | Value | Description | | ----- | ----------- | | INTERFACE_STATS
      | Include interface statistics (throughput, utilization) | | QOS_STATS | Include Quality of Service statistics | | DEVICE_STATS
      | Include device statistics (CPU, memory) | | PERFORMANCE_STATS | Include performance statistics | | ACL_TRACE | Include
      Access Control List trace information |.
    elements: str
    type: list
  periodicRefresh:
    description: Indicates whether to periodically refresh the path trace. | Value | Description | | ----- | ----------- |
      | true | Refresh the path trace every 30 seconds | | false | Perform the path trace once (default) |.
    type: bool
  protocol:
    description: Network protocol to use for the path trace. | Value | Description | | ----- | ----------- | | TCP | Transmission
      Control Protocol | | UDP | User Datagram Protocol | | (blank) | Check both TCP and UDP |.
    type: str
  sourceIpAddress:
    description: Source IP address for the path trace. Format can be IPv4 (e.g., 192.168.1.1) or IPv6.
    type: str
  sourceMacAddress:
    description: Source MAC address for the path trace. Format should be XX XX XX XX XX XX (e.g., 00 1A 2B 3C 4D 5E).
    type: str
  sourcePort:
    description: Source port for the path trace. Must be between 1-65535.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Path Trace InitiateANewPathTrace
    description: Complete reference of the InitiateANewPathTrace API.
    link: https://developer.cisco.com/docs/dna-center/#!initiate-a-new-path-trace
  - name: Cisco Catalyst Center documentation for Path Trace DeletesPathTraceByID
    description: Complete reference of the DeletesPathTraceByID API.
    link: https://developer.cisco.com/docs/dna-center/#!deletes-path-trace-by-id
notes:
  - SDK Method used are
    path_trace.PathTrace.deletes_path_trace_by_id,
    path_trace.PathTrace.initiate_a_new_path_trace,
  - Paths used are
    post /dna/intent/api/v1/pathTraces,
    delete /dna/intent/api/v1/pathTraces/{id},
"""

EXAMPLES = r"""
---
- name: Delete by id
  cisco.catalystcenter.path_traces:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: string
- name: Create
  cisco.catalystcenter.path_traces:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    controlPath: true
    destinationIpAddress: string
    destinationMacAddress: string
    destinationPort: string
    inclusions:
      - string
    periodicRefresh: true
    protocol: string
    sourceIpAddress: string
    sourceMacAddress: string
    sourcePort: string
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
