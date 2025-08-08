#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: floors_upload_image
short_description: Resource module for Floors Upload
  Image
description:
  - Manage operation create of the resource Floors Upload
    Image.
  - Uploads floor image.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. Floor Id.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Site Design
      UploadsFloorImageV2
    description: Complete reference of the UploadsFloorImageV2
      API.
    link: https://developer.cisco.com/docs/dna-center/#!uploads-floor-image-v-2
notes:
  - SDK Method used are
    site_design.SiteDesign.uploads_floor_image_v2,
  - Paths used are
    post /dna/intent/api/v2/floors/{id}/uploadImage,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.floors_upload_image:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    id: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
