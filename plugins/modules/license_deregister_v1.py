#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: license_deregister_v1
short_description: Resource module for License Deregister V1
description:
- Manage operation create of the resource License Deregister V1.
- Deregisters the system with Cisco Smart Software Manager CSSM .
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options: {}
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Licenses SmartLicensingDeregistrationV1
  description: Complete reference of the SmartLicensingDeregistrationV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!smart-licensing-deregistration
notes:
  - SDK Method used are
    licenses.Licenses.smart_licensing_deregistration_v1,

  - Paths used are
    post /dna/system/api/v1/license/deregister,

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.license_deregister_v1:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"

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
