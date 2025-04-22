#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: security_advisories_results_trend_info
short_description: Information module for Security Advisories Results Trend Info
description:
  - This module represents an alias of the module security_advisories_results_trend_v1_info
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
      - ScanTime query parameter. Return advisories trend with scanTime greater than
        this scanTime.
    type: float
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
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Compliance GetSecurityAdvisoriesResultsTrendOverTimeV1
    description: Complete reference of the GetSecurityAdvisoriesResultsTrendOverTimeV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-security-advisories-results-trend-over-time
notes:
  - SDK Method used are compliance.Compliance.get_security_advisories_results_trend_over_time_v1,
  - Paths used are get /dna/intent/api/v1/securityAdvisories/resultsTrend,
  - It should be noted that this module is an alias of security_advisories_results_trend_v1_info
"""
EXAMPLES = r"""
- name: Get all Security Advisories Results Trend Info
  cisco.catalystcenter.security_advisories_results_trend_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    scanTime: 0
    offset: 0
    limit: 0
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
          "criticalSecurityImpactRatingAdvisoriesCount": 0,
          "highSecurityImpactRatingAdvisoriesCount": 0,
          "scanTime": 0
        }
      ],
      "version": "string"
    }
"""
