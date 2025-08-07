#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: eox_status_summary_info
short_description: Information module for Eox Status
  Summary
description:
  - Get all Eox Status Summary.
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
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for EoX GetEoXSummary
    description: Complete reference of the GetEoXSummary
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-eo-x-summary
notes:
  - SDK Method used are
    eox.Eox.get_eox_summary,
  - Paths used are
    get /dna/intent/api/v1/eox-status/summary,
"""

EXAMPLES = r"""
---
- name: Get all Eox Status Summary
  cisco.catalystcenter.eox_status_summary_info:
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
        "hardwareCount": 0,
        "softwareCount": 0,
        "moduleCount": 0,
        "totalCount": 0
      },
      "version": "string"
    }
"""
