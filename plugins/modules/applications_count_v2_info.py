#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: applications_count_v2_info
short_description: Information module for Applications
  Count V2
description:
  - Get all Applications Count V2.
  - Get the number of all existing applications.
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
      - ScalableGroupType query parameter. Scalable
        group type to retrieve, valid value APPLICATION.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Application
      Policy GetApplicationCountV2
    description: Complete reference of the GetApplicationCountV2
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-application-count-v-2
notes:
  - SDK Method used are
    application_policy.ApplicationPolicy.get_application_count_v2,
  - Paths used are
    get /dna/intent/api/v2/applications-count,
"""

EXAMPLES = r"""
---
- name: Get all Applications Count V2
  cisco.catalystcenter.applications_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    scalableGroupType: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": 0,
      "version": "string"
    }
"""
