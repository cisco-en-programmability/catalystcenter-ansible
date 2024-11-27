#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: catalystcenter_packages_v1_info
short_description: Information module for Dnac Packages V1
description:
- Get all Dnac Packages V1.
- Provides information such as name, version of packages installed on the DNA center.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- catalystcentersdk >= 2.3.7.6
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Platform CiscoDNACenterPackagesSummaryV1
  description: Complete reference of the CiscoDNACenterPackagesSummaryV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!cisco-dna-center-packages-summary
notes:
  - SDK Method used are
    platform.Platform.cisco_dna_center_packages_summary_v1,

  - Paths used are
    get /dna/intent/api/v1/dnac-packages,

"""

EXAMPLES = r"""
- name: Get all Dnac Packages V1
  cisco.catalystcenter.catalystcenter_packages_v1_info:
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
      "response": [
        {
          "name": "string",
          "version": "string"
        }
      ],
      "version": "string"
    }
"""
