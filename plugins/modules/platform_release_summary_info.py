#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: platform_release_summary_info
short_description: Information module for Platform Release Summary Info
description:
- This module represents an alias of the module platform_release_summary_v1_info
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
- name: Cisco DNA Center documentation for Platform Configuration CiscoCatalystCenterReleaseSummaryV1
  description: Complete reference of the CiscoCatalystCenterReleaseSummaryV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!cisco-catalyst-center-release-summary
notes:
  - SDK Method used are
    platform_configuration.PlatformConfiguration.release_summary,

  - Paths used are
    get /dna/intent/api/v1/dnac-release,
  - It should be noted that this module is an alias of platform_release_summary_v1_info

"""

EXAMPLES = r"""
- name: Get all Platform Release Summary Info
  cisco.catalystcenter.platform_release_summary_info:
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
      "version": "string",
      "response": {
        "corePackages": [
          "string"
        ],
        "packages": [
          "string"
        ],
        "name": "string",
        "installedVersion": "string",
        "systemVersion": "string",
        "supportedDirectUpdates": [
          {}
        ],
        "tenantId": "string"
      }
    }
"""
