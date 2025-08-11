#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: security_service_insertion_summaries_count_info
short_description: Information module for Security Service
  Insertion Summaries Count
description:
  - Get all Security Service Insertion Summaries Count.
  - Retrieves the total count of Security Service Insertion
    SSI summaries.
version_added: '6.18.0'
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
  - name: Cisco DNA Center documentation for SDA CountOfSecurityServiceInsertionSummaries
    description: Complete reference of the CountOfSecurityServiceInsertionSummaries
      API.
    link: https://developer.cisco.com/docs/dna-center/#!count-of-security-service-insertion-summaries
notes:
  - SDK Method used are
    sda.Sda.count_of_security_service_insertion_summaries,
  - Paths used are
    get /dna/intent/api/v1/securityServiceInsertionSummaries/count,
"""

EXAMPLES = r"""
---
- name: Get all Security Service Insertion Summaries
    Count
  cisco.catalystcenter.security_service_insertion_summaries_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
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
        "count": 0
      },
      "version": "string"
    }
"""
