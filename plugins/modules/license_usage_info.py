#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: license_usage_info
short_description: Information module for License Usage
description:
  - Get all License Usage. - > Retrieves the count of purchased, used, and available licenses Cisco DNA, Network, and CNS
    licenses for a smart account/virtual account in CSSM. Additionally, it provides information on the number of licenses
    consumed by devices managed through Cisco Catalyst Center.
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
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: int
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Licenses APIToObtainLicenseCounts_GroupedByProductFamilyAndLicenseType
    description: Complete reference of the APIToObtainLicenseCounts_GroupedByProductFamilyAndLicenseType API.
    link: https://developer.cisco.com/docs/dna-center/#!a-pi-to-obtain-license-counts-grouped-by-product-family-and-license-type
notes:
  - SDK Method used are
    licenses.Licenses.api_to_obtain_license_counts_grouped_by_product_family_and_license_type,
  - Paths used are
    get /dna/intent/api/v1/licenseUsage,
"""

EXAMPLES = r"""
---
- name: Get all License Usage
  cisco.catalystcenter.license_usage_info:
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
    limit: 0
    offset: 1
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "smartAccountId": "string",
          "virtualAccountId": "string",
          "licenseCountsSummary": [
            {
              "productFamily": "string",
              "licenses": [
                {
                  "type": "string",
                  "counts": {
                    "purchased": 0,
                    "used": 0,
                    "available": 0,
                    "usedByManagedNetworkDevices": 0
                  }
                }
              ]
            }
          ]
        }
      ],
      "version": "string"
    }
"""
