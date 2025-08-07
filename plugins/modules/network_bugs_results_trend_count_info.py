#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_bugs_results_trend_count_info
short_description: Information module for Network Bugs
  Results Trend Count
description:
  - Get all Network Bugs Results Trend Count.
  - Get count of network bugs results trend over time.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  scanTime:
    description:
      - ScanTime query parameter. Return bugs trend
        with scanTime greater than this scanTime.
    type: float
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Compliance
      GetCountOfNetworkBugsResultsTrendOverTime
    description: Complete reference of the GetCountOfNetworkBugsResultsTrendOverTime
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-count-of-network-bugs-results-trend-over-time
notes:
  - SDK Method used are
    compliance.Compliance.get_count_of_network_bugs_results_trend_over_time,
  - Paths used are
    get /dna/intent/api/v1/networkBugs/resultsTrend/count,
"""

EXAMPLES = r"""
---
- name: Get all Network Bugs Results Trend Count
  cisco.catalystcenter.network_bugs_results_trend_count_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    scanTime: 0
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
