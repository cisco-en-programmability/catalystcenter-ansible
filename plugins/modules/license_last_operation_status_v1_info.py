#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: license_last_operation_status_v1_info
short_description: Information module for License Last Operation Status V1
description:
  - Get all License Last Operation Status V1.
  - Retrieves the status of the last system licensing operation.
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
  - name: Cisco DNA Center documentation for Licenses SystemLicensingLastOperationStatusV1
    description: Complete reference of the SystemLicensingLastOperationStatusV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!system-licensing-last-operation-status
notes:
  - SDK Method used are licenses.Licenses.system_licensing_last_operation_status_v1,
  - Paths used are get /dna/system/api/v1/license/lastOperationStatus,
"""
EXAMPLES = r"""
- name: Get all License Last Operation Status V1
  cisco.catalystcenter.license_last_operation_status_v1_info:
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
        "id": "string",
        "status": "string",
        "isError": true,
        "failureReason": "string",
        "errorCode": "string",
        "lastUpdate": 0
      },
      "version": "string"
    }
"""
