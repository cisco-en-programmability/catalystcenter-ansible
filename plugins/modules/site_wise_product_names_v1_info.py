#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: site_wise_product_names_v1_info
short_description: Information module for Site Wise Product Names V1
description:
  - Get all Site Wise Product Names V1.
  - >
    Provides network device product names for a site. The default value of `siteId`
    is global. The response will
    include the network device count and image summary.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  siteId:
    description:
      - >
        SiteId query parameter. Site identifier to get the list of all available products
        under the site. The
        default value is the global site. See https //developer.cisco.com/docs/dna-center/get-site
        for siteId.
    type: str
  productName:
    description:
      - >
        ProductName query parameter. Filter with network device product name. Supports
        partial case-insensitive
        search. A minimum of 3 characters are required for search.
    type: str
  offset:
    description:
      - >
        Offset query parameter. The first record to show for this page; the first
        record is numbered 1. The minimum
        value is 1.
    type: float
  limit:
    description:
      - >
        Limit query parameter. The number of records to show for this page. The minimum
        and maximum values are 1 and
        500, respectively.
    type: float
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Software Image Management (SWIM) ReturnsNetworkDeviceProductNamesForASiteV1
    description: Complete reference of the ReturnsNetworkDeviceProductNamesForASiteV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!returns-network-device-product-names-for-a-site
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.returns_network_device_product_names_for_a_site_v1,
  - Paths used are get /dna/intent/api/v1/siteWiseProductNames,
"""
EXAMPLES = r"""
- name: Get all Site Wise Product Names V1
  cisco.catalystcenter.site_wise_product_names_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    siteId: string
    productName: string
    offset: 0
    limit: 0
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "id": "string",
        "productNameOrdinal": 0,
        "productName": "string",
        "supervisorProductName": "string",
        "supervisorProductNameOrdinal": 0,
        "networkDeviceCount": 0,
        "imageSummary": {
          "installedImageCount": 0,
          "goldenImageCount": 0,
          "installedImageAdvisorCount": 0
        }
      },
      "version": "string"
    }
"""
