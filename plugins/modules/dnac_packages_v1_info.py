#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: dnac_packages_v1_info
short_description: Information module for Dnac Packages V1
description:
  - Get all Dnac Packages V1.
  - Provides information such as name, version of packages installed on the Catalyst
    center.
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
  - name: Cisco DNA Center documentation for Platform CiscoCatalystCenterPackagesSummaryV1
    description: Complete reference of the CiscoCatalystCenterPackagesSummaryV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!cisco-catalyst-center-packages-summary
notes:
  - SDK Method used are platform.Platform.cisco_catalyst_center_packages_summary_v1,
  - Paths used are get /dna/intent/api/v1/dnac-packages,
"""
EXAMPLES = r"""
- name: Get all Dnac Packages V1
  cisco.catalystcenter.dnac_packages_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
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
