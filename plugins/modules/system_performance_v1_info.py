#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: system_performance_v1_info
short_description: Information module for System Performance V1
description:
  - Get all System Performance V1.
  - >
    Retrieves the aggregated metrics total, average or maximum of cluster key performance
    indicators KPIs , such as
    CPU utilization, memory utilization or network rates recorded within a specified
    time period. The data will be
    available from the past 24 hours.
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
      - Kpi query parameter. Valid values cpu,memory,network.
    type: str
  function:
    description:
      - Function query parameter. Valid values sum,average,max.
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
  - name: Cisco DNA Center documentation for Health and Performance SystemPerformanceAPIV1
    description: Complete reference of the SystemPerformanceAPIV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!system-performance-api
notes:
  - SDK Method used are health_and_performance.HealthAndPerformance.system_performance,
  - Paths used are get /dna/intent/api/v1/diagnostics/system/performance,
"""
EXAMPLES = r"""
- name: Get all System Performance V1
  cisco.catalystcenter.system_performance_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    kpi: string
    function: string
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
        "cpu": {
          "units": "string",
          "utilization": "string"
        },
        "memory": {
          "units": "string",
          "utilization": "string"
        },
        "network tx_rate": {
          "units": "string",
          "utilization": "string"
        },
        "network rx_rate": {
          "units": "string",
          "utilization": "string"
        }
      }
    }
"""
