#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: system_health_count_v1_info
short_description: Information module for System Health Count V1
description:
  - Get all System Health Count V1.
  - This API gives the count of the latest system events.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  domain:
    description:
      - >
        Domain query parameter. Fetch system events with this domain. Possible values
        of domain are listed here
        /dna/platform/app/consumer-portal/developer-toolkit/events.
    type: str
  subdomain:
    description:
      - >
        Subdomain query parameter. Fetch system events with this subdomain. Possible
        values of subdomain are listed
        here /dna/platform/app/consumer-portal/developer-toolkit/events.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Health and Performance SystemHealthCountAPIV1
    description: Complete reference of the SystemHealthCountAPIV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!system-health-count-api
notes:
  - SDK Method used are health_and_performance.HealthAndPerformance.system_health_count,
  - Paths used are get /dna/intent/api/v1/diagnostics/system/health/count,
"""
EXAMPLES = r"""
- name: Get all System Health Count V1
  cisco.catalystcenter.system_health_count_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    domain: string
    subdomain: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "count": 0
    }
"""
