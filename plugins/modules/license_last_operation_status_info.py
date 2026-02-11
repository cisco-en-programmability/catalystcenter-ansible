#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: license_last_operation_status_info
short_description: Information module for License Last Operation Status
description:
  - Get all License Last Operation Status. - > Retrieves the status of the last system licensing operation. If the operation
    does not exist or has not been triggered, the API responds with an HTTP 404 Not Found error.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Licenses SystemLicensingLastOperationStatus
    description: Complete reference of the SystemLicensingLastOperationStatus API.
    link: https://developer.cisco.com/docs/dna-center/#!system-licensing-last-operation-status
notes:
  - SDK Method used are
    licenses.Licenses.system_licensing_last_operation_status,
  - Paths used are
    get /dna/system/api/v1/license/lastOperationStatus,
"""

EXAMPLES = r"""
---
- name: Get all License Last Operation Status
  cisco.catalystcenter.license_last_operation_status_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
dnac_response:
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
