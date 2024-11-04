#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: images_siteWiseProductNames_info
short_description: Information module for Images Sitewiseproductnames
description:
- Get all Images Sitewiseproductnames.
- >
   Returns a list of network device product names and associated sites for a given image identifier. Refer
   `/dna/intent/api/v1/images` API for obtaining `imageId`.
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
    - ImageId path parameter. Software image identifier. Refer `/dna/intent/api/v1/images` API for obtaining `imageId`.
    type: str
  productName:
    description:
    - >
      ProductName query parameter. Filter with network device product name. Supports partial case-insensitive
      search. A minimum of 3 characters is required for the search.
    type: str
  productId:
    description:
    - ProductId query parameter. Filter with product ID (PID).
    type: str
  recommended:
    description:
    - >
      Recommended query parameter. Filter with recommended source. If `CISCO` then the network device product
      assigned was recommended by Cisco and `USER` then the user has manually assigned. Available values CISCO,
      USER.
    type: str
  assigned:
    description:
    - >
      Assigned query parameter. Filter with the assigned/unassigned, `ASSIGNED` option will filter network device
      products that are associated with the given image. The `NOT_ASSIGNED` option will filter network device
      products that have not yet been associated with the given image but apply to it. Available values ASSIGNED,
      NOT_ASSIGNED.
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
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Software Image Management (SWIM) RetrievesNetworkDeviceProductNamesAssignedToASoftwareImageV1
  description: Complete reference of the RetrievesNetworkDeviceProductNamesAssignedToASoftwareImageV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!retrieves-network-device-product-names-assigned-to-a-software-image-v-1
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.retrieves_network_device_product_names_assigned_to_a_software_image_v1,

  - Paths used are
    get /dna/intent/api/v1/images/{imageId}/siteWiseProductNames,

"""

EXAMPLES = r"""
- name: Get all Images Sitewiseproductnames
  cisco.catalystcenter.images_siteWiseProductNames_info:
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
    recommended: string
    assigned: string
    offset: 0
    limit: 0
    imageId: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "productName": "string",
          "productNameOrdinal": 0,
          "productIds": [
            "string"
          ],
          "siteIds": [
            "string"
          ],
          "recommended": "string"
        }
      ],
      "version": "string"
    }
"""
