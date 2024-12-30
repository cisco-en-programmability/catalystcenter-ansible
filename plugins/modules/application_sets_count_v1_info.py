#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: application_sets_count_v1_info
short_description: Information module for Application Sets Count V1
description:
- Get all Application Sets Count V1.
- Get the number of existing application-sets.
version_added: '3.1.0'
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
- name: Cisco DNA Center documentation for Application Policy GetApplicationSetsCountV1
  description: Complete reference of the GetApplicationSetsCountV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-application-sets-count
notes:
  - SDK Method used are
    application_policy.ApplicationPolicy.get_application_sets_count_v1,

  - Paths used are
    get /dna/intent/api/v1/application-policy-application-set-count,

"""

EXAMPLES = r"""
- name: Get all Application Sets Count V1
  cisco.catalystcenter.application_sets_count_v1_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
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
      "response": "string",
      "version": "string"
    }
"""
