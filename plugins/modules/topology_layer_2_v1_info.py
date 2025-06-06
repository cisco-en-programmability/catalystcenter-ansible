#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: topology_layer_2_v1_info
short_description: Information module for Topology Layer 2 V1
description:
  - Get Topology Layer 2 V1 by id.
  - Returns Layer 2 network topology by specified VLAN ID.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  vlanID:
    description:
      - VlanID path parameter. Vlan Name for e.g Vlan1, Vlan23 etc.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Topology GetTopologyDetailsV1
    description: Complete reference of the GetTopologyDetailsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-topology-details
notes:
  - SDK Method used are topology.Topology.get_topology_details_v1,
  - Paths used are get /dna/intent/api/v1/topology/l2/{vlanID},
"""
EXAMPLES = r"""
- name: Get Topology Layer 2 V1 by id
  cisco.catalystcenter.topology_layer_2_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    vlanID: string
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
