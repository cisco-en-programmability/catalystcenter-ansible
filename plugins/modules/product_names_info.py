#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: product_names_info
short_description: Information module for Product Names Info
description:
- This module represents an alias of the module product_names_v1_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  productName:
    description:
    - >
      ProductName query parameter. Filter with network device product name. Supports partial case-insensitive
      search. A minimum of 3 characters are required for search.
    type: str
  productId:
    description:
    - ProductId query parameter. Filter with product ID (PID).
    type: str
  offset:
    description:
    - >
      Offset query parameter. The first record to show for this page; the first record is numbered 1. The minimum
      value is 1.
    type: float
  limit:
    description:
    - >
      Limit query parameter. The number of records to show for this page. The minimum and maximum values are 1 and
      500, respectively.
    type: float
  productNameOrdinal:
    description:
    - ProductNameOrdinal path parameter. Product name ordinal is unique value for each network device product.
    type: float
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Software Image Management (SWIM) RetrieveNetworkDeviceProductNameV1
  description: Complete reference of the RetrieveNetworkDeviceProductNameV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!retrieve-network-device-product-name
- name: Cisco DNA Center documentation for Software Image Management (SWIM) RetrievesTheListOfNetworkDeviceProductNamesV1  # noqa: E501
  description: Complete reference of the RetrievesTheListOfNetworkDeviceProductNamesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-network-device-product-names
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.retrieve_network_device_product_name_v1,
    software_image_management_swim.SoftwareImageManagementSwim.retrieves_the_list_of_network_device_product_names_v1,

  - Paths used are
    get /dna/intent/api/v1/productNames,
    get /dna/intent/api/v1/productNames/{productNameOrdinal},
  - It should be noted that this module is an alias of product_names_v1_info

"""

EXAMPLES = r"""
- name: Get all Product Names Info
  cisco.catalystcenter.product_names_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    productName: string
    productId: string
    offset: 0
    limit: 0
  register: result

- name: Get Product Names Info by name
  cisco.catalystcenter.product_names_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    productNameOrdinal: 0
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
        "productName": "string",
        "productNameOrdinal": 0,
        "productIds": [
          "string"
        ]
      },
      "version": "string"
    }
"""
