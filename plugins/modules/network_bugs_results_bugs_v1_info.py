#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_bugs_results_bugs_v1_info
short_description: Information module for Network Bugs Results Bugs V1
description:
  - Get all Network Bugs Results Bugs V1.
  - Get network bugs.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id query parameter. The id of the network bug.
    type: str
  deviceCount:
    description:
      - DeviceCount query parameter. Return network bugs with deviceCount greater
        than this deviceCount.
    type: float
  severity:
    description:
      - Severity query parameter. Return network bugs with this severity. Available
        values CATASTROPHIC, SEVERE, MODERATE.
    type: str
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first
        record is numbered 1. Default value is 1.
    type: float
  limit:
    description:
      - >
        Limit query parameter. The number of records to show for this page. Minimum
        value is 1. Maximum value is
        500. Default value is 500.
    type: float
  sortBy:
    description:
      - SortBy query parameter. A property within the response to sort by.
    type: str
  order:
    description:
      - >
        Order query parameter. Whether ascending or descending order should be used
        to sort the response. Available
        values asc, desc. Default value is asc.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Compliance GetNetworkBugsV1
    description: Complete reference of the GetNetworkBugsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-network-bugs
notes:
  - SDK Method used are compliance.Compliance.get_network_bugs_v1,
  - Paths used are get /dna/intent/api/v1/networkBugs/results/bugs,
"""
EXAMPLES = r"""
- name: Get all Network Bugs Results Bugs V1
  cisco.catalystcenter.network_bugs_results_bugs_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    id: string
    deviceCount: 0
    severity: string
    offset: 0
    limit: 0
    sortBy: string
    order: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "headline": "string",
          "publicationUrl": "string",
          "deviceCount": 0,
          "severity": "string",
          "hasWorkaround": true,
          "workaround": "string",
          "affectedVersions": [
            "string"
          ],
          "integratedReleases": [
            "string"
          ]
        }
      ],
      "version": "string"
    }
"""
