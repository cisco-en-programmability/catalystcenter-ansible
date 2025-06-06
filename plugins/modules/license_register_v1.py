#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: license_register_v1
short_description: Resource module for License Register V1
description:
  - Manage operation create of the resource License Register V1.
  - Registers the system with Cisco Smart Software Manager CSSM .
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  smartAccountId:
    description: The ID of the Smart Account to which the system is registered.
    type: str
  virtualAccountId:
    description: The ID of the Virtual Account to which the system is registered.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Licenses SystemLicensingRegistrationV1
    description: Complete reference of the SystemLicensingRegistrationV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!system-licensing-registration
notes:
  - SDK Method used are licenses.Licenses.system_licensing_registration_v1,
  - Paths used are post /dna/system/api/v1/license/register,
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.license_register_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    smartAccountId: string
    virtualAccountId: string
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
