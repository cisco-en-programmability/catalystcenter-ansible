#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: application_policy_application_set_count_info
short_description: Information module for Application Policy Application Set Count Info
description:
- This module represents an alias of the module application_policy_application_set_count_v2_info
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  scalableGroupType:
    description:
    - ScalableGroupType query parameter. Scalable group type to retrieve, valid value APPLICATION_GROUP.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Application Policy GetApplicationSetCountV2
  description: Complete reference of the GetApplicationSetCountV2 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-application-set-count
notes:
  - SDK Method used are
    application_policy.ApplicationPolicy.get_application_set_count_v2,

  - Paths used are
    get /dna/intent/api/v2/application-policy-application-set-count,
  - It should be noted that this module is an alias of application_policy_application_set_count_v2_info

"""

EXAMPLES = r"""
- name: Get all Application Policy Application Set Count Info
  cisco.catalystcenter.application_policy_application_set_count_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    scalableGroupType: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": 0,
      "version": "string"
    }
"""
