#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: eox_status_summary_v1_info
short_description: Information module for Eox Status Summary V1
description:
  - Get all Eox Status Summary V1.
  - Retrieves EoX summary for all devices in the network.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for EoX GetEoXSummaryV1
    description: Complete reference of the GetEoXSummaryV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-eo-x-summary
notes:
  - SDK Method used are eox.Eox.get_eox_summary_v1,
  - Paths used are get /dna/intent/api/v1/eox-status/summary,
"""
EXAMPLES = r"""
- name: Get all Eox Status Summary V1
  cisco.catalystcenter.eox_status_summary_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "hardwareCount": 0,
        "softwareCount": 0,
        "moduleCount": 0,
        "totalCount": 0
      },
      "version": "string"
    }
"""
