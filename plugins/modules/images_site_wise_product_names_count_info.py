#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: images_site_wise_product_names_count_info
short_description: Information module for Images Site
  Wise Product Names Count
description:
  - Get all Images Site Wise Product Names Count. -
    > Returns count of assigned network device product
    for a given image identifier. Refer `/dna/intent/api/v1/images`
    API for obtaining `imageId`.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  imageId:
    description:
      - ImageId path parameter. Software image identifier.
        Refer `/dna/intent/api/v/images` API for obtaining
        `imageId`.
    type: str
  productName:
    description:
      - >
        ProductName query parameter. Filter with network
        device product name. Supports partial case-insensitive
        search. A minimum of 3 characters are required
        for search.
    type: str
  productId:
    description:
      - ProductId query parameter. Filter with product
        ID (PID).
    type: str
  recommended:
    description:
      - >
        Recommended query parameter. Filter with recommended
        source. If `CISCO` then the network device product
        assigned was recommended by Cisco and `USER`
        then the user has manually assigned. Available
        values CISCO, USER.
    type: str
  assigned:
    description:
      - >
        Assigned query parameter. Filter with the assigned/unassigned,
        `ASSIGNED` option will filter network device
        products that are associated with the given
        image. The `NOT_ASSIGNED` option will filter
        network device products that have not yet been
        associated with the given image but apply to
        it. Available values ASSIGNED, NOT_ASSIGNED.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Software
      Image Management (SWIM) RetrievesTheCountOfAssignedNetworkDeviceProducts
    description: Complete reference of the RetrievesTheCountOfAssignedNetworkDeviceProducts
      API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-count-of-assigned-network-device-products
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.retrieves_the_count_of_assigned_network_device_products,
  - Paths used are
    get /dna/intent/api/v1/images/{imageId}/siteWiseProductNames/count,
"""

EXAMPLES = r"""
---
- name: Get all Images Site Wise Product Names Count
  cisco.catalystcenter.images_site_wise_product_names_count_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
    productName: string
    productId: string
    recommended: string
    assigned: string
    imageId: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
