#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: license_deregister
short_description: Resource module for License Deregister
description:
  - Manage operation create of the resource License
    Deregister.
  - Deregisters the system with Cisco Smart Software
    Manager CSSM .
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options: {}
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Licenses
      SmartLicensingDeregistration
    description: Complete reference of the SmartLicensingDeregistration
      API.
    link: https://developer.cisco.com/docs/dna-center/#!smart-licensing-deregistration
notes:
  - SDK Method used are
    licenses.Licenses.smart_licensing_deregistration,
  - Paths used are
    post /dna/system/api/v1/license/deregister,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.license_deregister:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
