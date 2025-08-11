#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_family_identifiers_details_info
short_description: Information module for Device Family
  Identifiers Details
description:
  - Get all Device Family Identifiers Details.
  - API to get Device Family Identifiers for all Device
    Families that can be used for tagging an image golden.
version_added: '4.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Software
      Image Management (SWIM) GetDeviceFamilyIdentifiers
    description: Complete reference of the GetDeviceFamilyIdentifiers
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-device-family-identifiers
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.get_device_family_identifiers,
  - Paths used are
    get /dna/intent/api/v1/image/importation/device-family-identifiers,
"""

EXAMPLES = r"""
---
- name: Get all Device Family Identifiers Details
  cisco.catalystcenter.device_family_identifiers_details_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
