#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: fabric_summary_v1_info
short_description: Information module for Fabric Summary V1
description:
  - Get all Fabric Summary V1.
  - >
    Read Fabric summary for overall deployment. Get an aggregated summary of all fabric
    entities in a deployment
    including the entity health.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  startTime:
    description:
      - >
        StartTime query parameter. Start time from which API queries the data set
        related to the resource. It must
        be specified in UNIX epochtime in milliseconds. Value is inclusive.
    type: float
  endTime:
    description:
      - >
        EndTime query parameter. End time to which API queries the data set related
        to the resource. It must be
        specified in UNIX epochtime in milliseconds. Value is inclusive.
    type: float
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA ReadFabricEntitySummaryV1
    description: Complete reference of the ReadFabricEntitySummaryV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!read-fabric-entity-summary
notes:
  - SDK Method used are sda.Sda.read_fabric_entity_summary_v1,
  - Paths used are get /dna/data/api/v1/fabricSummary,
"""
EXAMPLES = r"""
- name: Get all Fabric Summary V1
  cisco.catalystcenter.fabric_summary_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    startTime: 0
    endTime: 0
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
        "protocolSummaries": [
          {
            "fabricSiteGoodHealthCount": 0,
            "fabricSiteCount": 0,
            "fabricSiteGoodHealthPercentage": 0,
            "fabricSiteNoHealthCount": 0,
            "fabricSitePoorHealthCount": 0,
            "fabricSiteFairHealthCount": 0,
            "l3VnGoodHealthCount": 0,
            "l3VnCount": 0,
            "l3VnGoodHealthPercentage": 0,
            "l3VnNoHealthCount": 0,
            "l3VnFairHealthCount": 0,
            "l3VnPoorHealthCount": 0,
            "l2VnGoodHealthCount": 0,
            "l2VnCount": 0,
            "l2VnGoodHealthPercentage": 0,
            "l2VnNoHealthCount": 0,
            "l2VnPoorHealthCount": 0,
            "l2VnFairHealthCount": 0,
            "transitNetworkGoodHealthCount": 0,
            "transitNetworkCount": 0,
            "transitNetworkGoodHealthPercentage": 0,
            "transitNetworkNoHealthCount": 0,
            "transitNetworkPoorHealthCount": 0,
            "transitNetworkFairHealthCount": 0,
            "ipTransitNetworkCount": 0,
            "fabricDeviceCount": 0,
            "p1IssueCount": 0,
            "p2IssueCount": 0,
            "p3IssueCount": 0,
            "networkSegmentProtocol": "string"
          }
        ]
      },
      "version": "string"
    }
"""
