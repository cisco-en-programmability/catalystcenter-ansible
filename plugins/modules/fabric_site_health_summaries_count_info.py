#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: fabric_site_health_summaries_count_info
short_description: Information module for Fabric Site Health Summaries Count Info
description:
  - This module represents an alias of the module fabric_site_health_summaries_count_v1_info
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
        Id query parameter. The list of entity Uuids. (Ex."6bef213c-19ca-4170-8375-b694e251101c")
        Examples
        id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested) id=6bef213c-19ca-4170-8375-
        b694e251101c&id=32219612-819e-4b5e-a96b-cf22aca13dd9&id=2541e9a7-b80d-4955-8aa2-79b233318ba0
        (multiple
        entity uuid with '&' separator).
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA ReadFabricSiteCountV1
    description: Complete reference of the ReadFabricSiteCountV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!read-fabric-site-count
notes:
  - SDK Method used are sda.Sda.read_fabric_site_count_v1,
  - Paths used are get /dna/data/api/v1/fabricSiteHealthSummaries/count,
  - It should be noted that this module is an alias of fabric_site_health_summaries_count_v1_info
"""
EXAMPLES = r"""
- name: Get all Fabric Site Health Summaries Count Info
  cisco.catalystcenter.fabric_site_health_summaries_count_info:
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
  type: dict
  sample: >
    {
      "response": {
        "count": 0
      },
      "version": "string"
    }
"""
