#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: images_download
short_description: Resource module for Images Download
description:
- This module represents an alias of the module images_download_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. Software image identifier. Check API `/dna/intent/api/v1/images`
      for `id` from response.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Software Image Management (SWIM) DownloadTheSoftwareImageV1
  description: Complete reference of the DownloadTheSoftwareImageV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!download-the-software-image
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.download_the_software_image_v1,

  - Paths used are
    post /dna/intent/api/v1/images/{id}/download,
  - It should be noted that this module is an alias of images_download_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.images_download:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    id: string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
