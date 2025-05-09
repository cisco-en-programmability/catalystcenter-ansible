#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: system_performance_historical_v1_info
short_description: Information module for System Performance Historical V1
description:
  - Get all System Performance Historical V1.
  - >
    Retrieves the average values of cluster key performance indicators KPIs , like
    CPU utilization, memory utilization
    or network rates grouped by time intervals within a specified time range. The
    data will be available from the past
    24 hours.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  kpi:
    description:
      - Kpi query parameter. Fetch historical data for this kpi. Valid values cpu,memory,network.
    type: str
  startTime:
    description:
      - >
        StartTime query parameter. This is the epoch start time in milliseconds from
        which performance indicator
        need to be fetched.
    type: float
  endTime:
    description:
      - >
        EndTime query parameter. This is the epoch end time in milliseconds upto which
        performance indicator need to
        be fetched.
    type: float
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Health and Performance SystemPerformanceHistoricalAPIV1
    description: Complete reference of the SystemPerformanceHistoricalAPIV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!system-performance-historical-api
notes:
  - SDK Method used are health_and_performance.HealthAndPerformance.system_performance_historical,
  - Paths used are get /dna/intent/api/v1/diagnostics/system/performance/history,
"""
EXAMPLES = r"""
- name: Get all System Performance Historical V1
  cisco.catalystcenter.system_performance_historical_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    kpi: string
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
      "hostName": "string",
      "version": "string",
      "kpis": {
        "legends": {
          "cpu": {
            "units": "string"
          },
          "memory": {
            "units": "string"
          },
          "network tx_rate": {
            "units": "string"
          },
          "network rx_rate": {
            "units": "string"
          }
        },
        "data": {
          "t1": [
            "string"
          ]
        },
        "cpuAvg": "string",
        "memoryAvg": "string"
      }
    }
"""
