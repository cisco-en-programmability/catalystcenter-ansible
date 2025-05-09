#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_bugs_results_bugs_count_v1_info
short_description: Information module for Network Bugs Results Bugs Count V1
description:
  - Get all Network Bugs Results Bugs Count V1.
  - Get count of network bugs.
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
      - Id query parameter. Id of the network bug.
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
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Compliance GetCountOfNetworkBugsV1
    description: Complete reference of the GetCountOfNetworkBugsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-count-of-network-bugs
notes:
  - SDK Method used are compliance.Compliance.get_count_of_network_bugs_v1,
  - Paths used are get /dna/intent/api/v1/networkBugs/results/bugs/count,
"""
EXAMPLES = r"""
- name: Get all Network Bugs Results Bugs Count V1
  cisco.catalystcenter.network_bugs_results_bugs_count_v1_info:
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
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": {
        "count": 0
      }
    }
"""
