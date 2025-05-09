#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: security_advisories_devices_v1_info
short_description: Information module for Security Advisories Devices V1
description:
  - Get all Security Advisories Devices V1.
  - Retrieves list of devices for an advisory.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  advisoryId:
    description:
      - AdvisoryId path parameter. Advisory ID.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Security Advisories GetDevicesPerAdvisoryV1
    description: Complete reference of the GetDevicesPerAdvisoryV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-devices-per-advisory
notes:
  - SDK Method used are security_advisories.SecurityAdvisories.get_devices_per_advisory_v1,
  - Paths used are get /dna/intent/api/v1/security-advisory/advisory/{advisoryId}/device,
"""
EXAMPLES = r"""
- name: Get all Security Advisories Devices V1
  cisco.catalystcenter.security_advisories_devices_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    advisoryId: string
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
        "string"
      ],
      "version": "string"
    }
"""
