#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: topology_physical_info
short_description: Information module for Topology Physical
description:
- Get all Topology Physical.
- Returns the raw physical topology by specified criteria of nodeType.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  nodeType:
    description:
    - NodeType query parameter.
    type: str
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Topology GetPhysicalTopologyV1
  description: Complete reference of the GetPhysicalTopologyV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-physical-topology-v-1
notes:
  - SDK Method used are
    topology.Topology.get_physical_topology_v1,

  - Paths used are
    get /dna/intent/api/v1/topology/physical-topology,

"""

EXAMPLES = r"""
- name: Get all Topology Physical
  cisco.catalystcenter.topology_physical_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    nodeType: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "id": "string",
        "links": [
          {
            "additionalInfo": {},
            "endPortID": "string",
            "endPortIpv4Address": "string",
            "endPortIpv4Mask": "string",
            "endPortName": "string",
            "endPortSpeed": "string",
            "greyOut": true,
            "id": "string",
            "linkStatus": "string",
            "source": "string",
            "startPortID": "string",
            "startPortIpv4Address": "string",
            "startPortIpv4Mask": "string",
            "startPortName": "string",
            "startPortSpeed": "string",
            "tag": "string",
            "target": "string"
          }
        ],
        "nodes": [
          {
            "aclApplied": true,
            "additionalInfo": {},
            "customParam": {
              "id": "string",
              "label": "string",
              "parentNodeId": "string",
              "x": 0,
              "y": 0
            },
            "connectedDeviceId": "string",
            "dataPathId": "string",
            "deviceType": "string",
            "deviceSeries": "string",
            "family": "string",
            "fixed": true,
            "greyOut": true,
            "id": "string",
            "ip": "string",
            "label": "string",
            "networkType": "string",
            "nodeType": "string",
            "order": 0,
            "osType": "string",
            "platformId": "string",
            "role": "string",
            "roleSource": "string",
            "softwareVersion": "string",
            "tags": [
              "string"
            ],
            "upperNode": "string",
            "userId": "string",
            "vlanId": "string",
            "x": 0,
            "y": 0
          }
        ]
      },
      "version": "string"
    }
"""
