#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: license_usage_count_info
short_description: Information module for License Usage Count
description:
  - Get all License Usage Count.
  - API to fetch the count of license usage records based on given filters.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  smartAccountId:
    description:
      - >
        SmartAccountId query parameter. Id of the smart account. Use `GET
        /dna/intent/api/v1/licenses/smartAccounts` intent API to find the smart account Id.
    type: str
  virtualAccountId:
    description:
      - >
        VirtualAccountId query parameter. Id of the virtual account. Use `GET
        /dna/intent/api/v1/licenses/smartAccount/${id}/virtualAccounts` intent API to find the virtual account
        Id.
    type: str
  productFamily:
    description:
      - >
        ProductFamily query parameter. Family of the product | Family | Description |
        |--------------|------------------------------------------| | `SWITCH` | Switch product family | |
        `ROUTER` | Router product family | | `UNIFIED_AP` | Unified Access Point product family | | `ISE` | ISE
        product family |.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Licenses APIToFetchTheCountOfLicenseUsageRecordsBasedOnGivenFilters
    description: Complete reference of the APIToFetchTheCountOfLicenseUsageRecordsBasedOnGivenFilters API.
    link: https://developer.cisco.com/docs/dna-center/#!a-pi-to-fetch-the-count-of-license-usage-records-based-on-given-filters
notes:
  - SDK Method used are
    licenses.Licenses.api_to_fetch_the_count_of_license_usage_records_based_on_given_filters,
  - Paths used are
    get /dna/intent/api/v1/licenseUsage/count,
"""

EXAMPLES = r"""
---
- name: Get all License Usage Count
  cisco.catalystcenter.license_usage_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    smartAccountId: 1034567
    virtualAccountId: 1267
    productFamily: SWITCH
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "count": 0
      },
      "version": "string"
    }
"""
