#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: license_setting_v1_info
short_description: Information module for License Setting V1
description:
  - Get all License Setting V1.
  - >
    Retrieves license setting - Default smart account id and virtual account id for
    auto registration of devices for
    smart license flow. If default smart account is not configured, 'defaultSmartAccountId'
    is 'null'. Similarly, if
    auto registration of devices for smart license flow is not enabled, 'autoRegistrationVirtualAccountId'
    is 'null'.
    For smart proxy connection mode, 'autoRegistrationVirtualAccountId' is always
    'null'.
version_added: '6.15.0'
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
  - name: Cisco DNA Center documentation for Licenses RetrieveLicenseSettingV1
    description: Complete reference of the RetrieveLicenseSettingV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-license-setting
notes:
  - SDK Method used are licenses.Licenses.retrieve_license_setting_v1,
  - Paths used are get /dna/intent/api/v1/licenseSetting,
"""
EXAMPLES = r"""
- name: Get all License Setting V1
  cisco.catalystcenter.license_setting_v1_info:
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
        "defaultSmartAccountId": "string",
        "autoRegistrationVirtualAccountId": "string"
      },
      "version": "string"
    }
"""
