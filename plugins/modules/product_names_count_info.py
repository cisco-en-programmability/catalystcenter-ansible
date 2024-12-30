#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: product_names_count_info
short_description: Information module for Product Names Count Info
description:
- This module represents an alias of the module product_names_count_v1_info
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
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Software Image Management (SWIM) CountOfNetworkProductNamesV1
  description: Complete reference of the CountOfNetworkProductNamesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!count-of-network-product-names
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.count_of_network_product_names_v1,

  - Paths used are
    get /dna/intent/api/v1/productNames/count,
  - It should be noted that this module is an alias of product_names_count_v1_info

"""

EXAMPLES = r"""
- name: Get all Product Names Count Info
  cisco.catalystcenter.product_names_count_info:
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
        "count": 0
      },
      "version": "string"
    }
"""
