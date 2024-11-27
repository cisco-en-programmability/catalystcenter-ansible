#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sp_profile_delete
short_description: Resource module for Sp Profile Delete
description:
- This module represents an alias of the module sp_profile_delete_v2
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  spProfileName:
    description: SpProfileName path parameter. SP profile name.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.6
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Network Settings DeleteSPProfileV2
  description: Complete reference of the DeleteSPProfileV2 API.
  link: https://developer.cisco.com/docs/dna-center/#!delete-sp-profile-v-2
notes:
  - SDK Method used are
    network_settings.NetworkSettings.delete_sp_profile_v2,

  - Paths used are
    delete /dna/intent/api/v2/sp-profile/{spProfileName},
  - It should be noted that this module is an alias of sp_profile_delete_v2

"""

EXAMPLES = r"""
- name: Delete by name
  cisco.catalystcenter.sp_profile_delete:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    spProfileName: string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
