#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: platform_release_summary_v1_info
short_description: Information module for Platform Release Summary V1
description:
  - Get all Platform Release Summary V1.
  - >
    Provides information such as API version, mandatory core packages for installation
    or upgrade, optional packages,
    Cisco Catalyst Center name and version, supported direct updates, and tenant ID.
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
    link:
      https://developer.cisco.com/docs/dna-center/#!cisco-catalyst-center-release-summary
notes:
  - SDK Method used are platform_configuration.PlatformConfiguration.release_summary,
  - Paths used are get /dna/intent/api/v1/dnac-release,
"""
EXAMPLES = r"""
- name: Get all Platform Release Summary V1
  cisco.catalystcenter.platform_release_summary_v1_info:
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
