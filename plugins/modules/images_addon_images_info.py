#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: images_addon_images_info
short_description: Information module for Images Addon
  Images
description:
  - Get all Images Addon Images. - > Retrieves the list
    of applicable add-on images if available for the
    given software image. `id` can be obtained from
    the response of API /dna/intent/api/v1/images?hasAddonImages=true
    .
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - >
        Id path parameter. Software image identifier.
        Check `/dna/intent/api/v1/images?hasAddonImages=true`
        API to get the same.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Software
      Image Management (SWIM) RetrieveApplicableAddOnImagesForTheGivenSoftwareImage
    description: Complete reference of the RetrieveApplicableAddOnImagesForTheGivenSoftwareImage
      API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-applicable-add-on-images-for-the-given-software-image
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.retrieve_applicable_add_on_images_for_the_given_software_image,
  - Paths used are
    get /dna/intent/api/v1/images/{id}/addonImages,
"""

EXAMPLES = r"""
---
- name: Get all Images Addon Images
  cisco.catalystcenter.images_addon_images_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "imported": true,
          "name": "string",
          "version": "string",
          "imageType": "string",
          "recommended": "string",
          "ciscoLatest": true,
          "integrityStatus": "string",
          "isAddonImage": true,
          "hasAddonImages": true,
          "goldenTaggingDetails": [
            {
              "deviceRoles": [
                "string"
              ],
              "deviceTags": [
                "string"
              ],
              "inheritedSiteId": "string",
              "inheritedSiteName": "string"
            }
          ],
          "productNames": [
            {
              "id": "string",
              "productName": "string",
              "productNameOrdinal": 0,
              "supervisorProductName": "string",
              "supervisorProductNameOrdinal": 0
            }
          ],
          "isGoldenTagged": true
        }
      ],
      "version": "string"
    }
"""
