#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: security_advisories_info
short_description: Information module for Security Advisories
description:
- Get all Security Advisories.
- Retrieves list of advisories on the network.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Security Advisories GetAdvisoriesListV1
  description: Complete reference of the GetAdvisoriesListV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-advisories-list-v-1
notes:
  - SDK Method used are
    security_advisories.SecurityAdvisories.get_advisories_list_v1,

  - Paths used are
    get /dna/intent/api/v1/security-advisory/advisory,

"""

EXAMPLES = r"""
- name: Get all Security Advisories
  cisco.catalystcenter.security_advisories_info:
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
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "advisoryId": "string",
        "deviceCount": 0,
        "hiddenDeviceCount": 0,
        "cves": [
          "string"
        ],
        "publicationUrl": "string",
        "sir": "string",
        "detectionType": "string",
        "defaultDetectionType": "string",
        "defaultConfigMatchPattern": "string",
        "fixedVersions": {}
      },
      "version": "string"
    }
"""
