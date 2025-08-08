#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: security_advisories_summary_info
short_description: Information module for Security Advisories
  Summary
description:
  - Get all Security Advisories Summary.
  - Retrieves summary of advisories on the network.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Security
      Advisories GetAdvisoriesSummary
    description: Complete reference of the GetAdvisoriesSummary
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-advisories-summary
notes:
  - SDK Method used are
    security_advisories.SecurityAdvisories.get_advisories_summary,
  - Paths used are
    get /dna/intent/api/v1/security-advisory/advisory/aggregate,
"""

EXAMPLES = r"""
---
- name: Get all Security Advisories Summary
  cisco.catalystcenter.security_advisories_summary_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "INFORMATIONAL": {
          "CONFIG": 0,
          "CUSTOM_CONFIG": 0,
          "VERSION": 0,
          "TOTAL": 0
        },
        "LOW": {
          "CONFIG": 0,
          "CUSTOM_CONFIG": 0,
          "VERSION": 0,
          "TOTAL": 0
        },
        "MEDIUM": {
          "CONFIG": 0,
          "CUSTOM_CONFIG": 0,
          "VERSION": 0,
          "TOTAL": 0
        },
        "HIGH": {
          "CONFIG": 0,
          "CUSTOM_CONFIG": 0,
          "VERSION": 0,
          "TOTAL": 0
        },
        "CRITICAL": {
          "CONFIG": 0,
          "CUSTOM_CONFIG": 0,
          "VERSION": 0,
          "TOTAL": 0
        },
        "NA": {
          "CONFIG": 0,
          "CUSTOM_CONFIG": 0,
          "VERSION": 0,
          "TOTAL": 0
        }
      },
      "version": "string"
    }
"""
