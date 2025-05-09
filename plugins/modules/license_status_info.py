#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: license_status_info
short_description: Information module for License Status Info
description:
  - This module represents an alias of the module license_status_v1_info
version_added: '6.17.0'
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
  - name: Cisco DNA Center documentation for Licenses SystemLicensingStatusV1
    description: Complete reference of the SystemLicensingStatusV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!system-licensing-status
notes:
  - SDK Method used are licenses.Licenses.system_licensing_status_v1,
  - Paths used are get /dna/system/api/v1/license/status,
  - It should be noted that this module is an alias of license_status_v1_info
"""
EXAMPLES = r"""
- name: Get all License Status Info
  cisco.catalystcenter.license_status_info:
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
        "registrationStatus": {
          "status": "string",
          "lastAttemptTimestamp": 0,
          "expiryTimestamp": 0,
          "nextAttemptTimestamp": 0,
          "lastAttemptStatus": "string",
          "lastAttemptFailReason": "string"
        },
        "authorizationStatus": {
          "status": "string",
          "lastAttemptTimestamp": 0,
          "evaluationRemainderTimestamp": 0,
          "expiryTimestamp": 0,
          "nextAttemptTimestamp": 0,
          "lastAttemptStatus": "string",
          "lastAttemptFailReason": "string"
        },
        "entitlements": {
          "tag": "string",
          "description": "string",
          "usageCount": 0,
          "status": "string"
        },
        "smartAccountId": "string",
        "virtualAccountId": "string",
        "exportControl": "string"
      },
      "version": "string"
    }
"""
