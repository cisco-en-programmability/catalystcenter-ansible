#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: license_renew
short_description: Resource module for License Renew
description:
- This module represents an alias of the module license_renew_v1
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options: {}
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Licenses SmartLicensingRenewOperationV1
  description: Complete reference of the SmartLicensingRenewOperationV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!smart-licensing-renew-operation
notes:
  - SDK Method used are
    licenses.Licenses.smart_licensing_renew_operation_v1,

  - Paths used are
    post /dna/system/api/v1/license/renew,
  - It should be noted that this module is an alias of license_renew_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.license_renew:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "url": "string"
      },
      "version": "string"
    }
"""
