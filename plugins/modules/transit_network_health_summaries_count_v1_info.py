#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: transit_network_health_summaries_count_v1_info
short_description: Information module for Transit Network Health Summaries Count V1
description:
  - Get all Transit Network Health Summaries Count V1.
  - Get a count of transit networks. Use available query parameters to get the count
    of a subset of transit networks.
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
  id:
    description:
      - >
        Id query parameter. The list of transit entity ids. (Ex "1551156a-bc97-3c63-aeda-8a6d3765b5b9")
        Examples
        id=1551156a-bc97-3c63-aeda-8a6d3765b5b9 (single entity uuid requested)
        id=1551156a-bc97-3c63-aeda-8a6d3765b5b9&id=4aa20652-237c-4625-b2b4-fd7e82b6a81e
        (multiple entity uuids with
        '&' separator).
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA ReadTransitNetworksCountV1
    description: Complete reference of the ReadTransitNetworksCountV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!read-transit-networks-count
notes:
  - SDK Method used are sda.Sda.read_transit_networks_count_v1,
  - Paths used are get /dna/data/api/v1/transitNetworkHealthSummaries/count,
"""
EXAMPLES = r"""
- name: Get all Transit Network Health Summaries Count V1
  cisco.catalystcenter.transit_network_health_summaries_count_v1_info:
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
    id: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "errorCode": 0,
        "message": "string",
        "detail": "string"
      }
    ]
"""
