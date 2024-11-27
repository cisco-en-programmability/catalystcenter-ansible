#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: images_addon_images_count_v1_info
short_description: Information module for Images Addon Images Count V1
description:
- Get all Images Addon Images Count V1.
- >
   Count of add-on images available for the given software image identifier, `id` can be obtained from the response
   of API /dna/intent/api/v1/images?hasAddonImages=true .
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
    - Id path parameter. Software image identifier. Check API `/dna/intent/api/v1/images` for id from response.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Software Image Management (SWIM) ReturnsCountOfAddOnImagesV1
  description: Complete reference of the ReturnsCountOfAddOnImagesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!returns-count-of-add-on-images
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.returns_count_of_add_on_images_v1,

  - Paths used are
    get /dna/intent/api/v1/images/{id}/addonImages/count,

"""

EXAMPLES = r"""
- name: Get all Images Addon Images Count V1
  cisco.catalystcenter.images_addon_images_count_v1_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
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
