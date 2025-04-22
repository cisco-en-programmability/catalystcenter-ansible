#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: device_family_identifiers_details_info
short_description: Information module for Device Family Identifiers Details Info
description:
  - This module represents an alias of the module device_family_identifiers_details_v1_info
version_added: '4.0.0'
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
  - name: Cisco DNA Center documentation for Software Image Management (SWIM) GetDeviceFamilyIdentifiersV1
    description: Complete reference of the GetDeviceFamilyIdentifiersV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-device-family-identifiers
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.get_device_family_identifiers_v1,
  - Paths used are get /dna/intent/api/v1/image/importation/device-family-identifiers,
  - It should be noted that this module is an alias of device_family_identifiers_details_v1_info
"""
EXAMPLES = r"""
- name: Get all Device Family Identifiers Details Info
  cisco.catalystcenter.device_family_identifiers_details_info:
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
      "version": "string",
      "response": [
        {
          "deviceFamily": "string",
          "deviceFamilyIdentifier": "string"
        }
      ]
    }
"""
