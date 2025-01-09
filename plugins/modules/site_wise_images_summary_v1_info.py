#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: site_wise_images_summary_v1_info
short_description: Information module for Site Wise Images Summary V1
description:
- Get all Site Wise Images Summary V1.
- >
   Returns aggregate counts of network device product names, golden and non-golden tagged products, imported images,
   golden images tagged, and advisor for a specific site provide, the default value of `siteId` is set to global.
version_added: '6.17.0'
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
      SiteId query parameter. Site identifier to get the aggreagte counts products under the site. The default
      value is global site id. See https //developer.cisco.com/docs/dna-center(#!get-site) for `siteId`.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Software Image Management (SWIM) ReturnsTheImageSummaryForTheGivenSiteV1
  description: Complete reference of the ReturnsTheImageSummaryForTheGivenSiteV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!returns-the-image-summary-for-the-given-site
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.returns_the_image_summary_for_the_given_site_v1,

  - Paths used are
    get /dna/intent/api/v1/siteWiseImagesSummary,

"""

EXAMPLES = r"""
- name: Get all Site Wise Images Summary V1
  cisco.catalystcenter.site_wise_images_summary_v1_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    siteId: string
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
        "importedImageCount": 0,
        "installedImageCount": 0,
        "goldenImageCount": 0,
        "nonGoldenImageCount": 0,
        "installedImageAdvisorCount": 0,
        "productCount": 0,
        "productsWithGoldenCount": 0,
        "productsWithoutGoldenCount": 0
      },
      "version": "string"
    }
"""
