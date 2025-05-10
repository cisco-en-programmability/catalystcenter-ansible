#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: field_notices_results_trend_count_v1_info
short_description: Information module for Field Notices Results Trend Count V1
description:
  - Get all Field Notices Results Trend Count V1.
  - Get count of field notices results trend over time.
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
      - ScanTime query parameter. Return field notices trend with scanTime greater
        than this scanTime.
    type: float
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Compliance GetCountOfFieldNoticesResultsTrendOverTimeV1
    description: Complete reference of the GetCountOfFieldNoticesResultsTrendOverTimeV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-count-of-field-notices-results-trend-over-time
notes:
  - SDK Method used are compliance.Compliance.get_count_of_field_notices_results_trend_over_time_v1,
  - Paths used are get /dna/intent/api/v1/fieldNotices/resultsTrend/count,
"""
EXAMPLES = r"""
- name: Get all Field Notices Results Trend Count V1
  cisco.catalystcenter.field_notices_results_trend_count_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    scanTime: 0
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
