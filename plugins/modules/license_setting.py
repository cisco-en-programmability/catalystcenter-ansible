#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: license_setting
short_description: Resource module for License Setting
description:
- This module represents an alias of the module license_setting_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  autoRegistrationVirtualAccountId:
    description: Virtual account id.
    type: str
  defaultSmartAccountId:
    description: Default smart account id.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Licenses UpdateLicenseSettingV1
  description: Complete reference of the UpdateLicenseSettingV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!update-license-setting
notes:
  - SDK Method used are
    licenses.Licenses.update_license_setting_v1,

  - Paths used are
    put /dna/intent/api/v1/licenseSetting,
  - It should be noted that this module is an alias of license_setting_v1

"""

EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.license_setting:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    autoRegistrationVirtualAccountId: string
    defaultSmartAccountId: string

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
