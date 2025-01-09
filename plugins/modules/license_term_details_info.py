#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: license_term_details_info
short_description: Information module for License Term Details Info
description:
- This module represents an alias of the module license_term_details_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  smart_account_id:
    description:
    - Smart_account_id path parameter. Id of smart account.
    type: str
  virtual_account_name:
    description:
    - >
      Virtual_account_name path parameter. Name of virtual account. Putting "All" will give license term detail
      for all virtual accounts.
    type: str
  device_type:
    description:
    - Device_type query parameter. Type of device like router, switch, wireless or ise.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Licenses LicenseTermDetailsV1
  description: Complete reference of the LicenseTermDetailsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!license-term-details
notes:
  - SDK Method used are
    licenses.Licenses.license_term_details_v1,

  - Paths used are
    get /dna/intent/api/v1/licenses/term/smartAccount/{smart_account_id}/virtualAccount/{virtual_account_name},
  - It should be noted that this module is an alias of license_term_details_v1_info

"""

EXAMPLES = r"""
- name: Get License Term Details Info by name
  cisco.catalystcenter.license_term_details_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    device_type: string
    smart_account_id: string
    virtual_account_name: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "license_details": [
        {
          "model": "string",
          "virtual_account_name": "string",
          "license_term_start_date": "string",
          "license_term_end_date": "string",
          "dna_level": "string",
          "purchased_dna_license_count": "string",
          "is_license_expired": "string"
        }
      ]
    }
"""
