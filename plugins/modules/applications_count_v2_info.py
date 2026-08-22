#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: applications_count_v2_info
short_description: Information module for Applications Count V2
description:
  - Get all Applications Count V2.
  - Get the number of all existing applications.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  scalableGroupType:
    description:
      - ScalableGroupType query parameter. Scalable group type to retrieve, valid value APPLICATION.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Application Policy GetApplicationCount
    description: Complete reference of the GetApplicationCount API.
    link: https://developer.cisco.com/docs/dna-center/#!get-application-count
notes:
  - SDK Method used are
    application_policy.ApplicationPolicy.get_application_count,
  - Paths used are
    get /dna/intent/api/v2/applications-count,
"""

EXAMPLES = r"""
---
- name: Get all Applications Count V2
  cisco.catalystcenter.applications_count_v2_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    scalableGroupType: APPLICATION
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": 0,
      "version": "string"
    }
"""
