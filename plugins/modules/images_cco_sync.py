#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: images_cco_sync
short_description: Resource module for Images Cco Sync
description:
  - Manage operation create of the resource Images Cco
    Sync. - > Initiating the synchronization of the
    software images from Cisco.com. The latest and suggested
    images will be retrieved, along with the corresponding
    product name and PIDs for imported and retrieved
    images from Cisco.com. Once the task is completed,
    the API `/intent/api/v1/images?imported=false` will
    display all the images fetched from Cisco.com.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options: {}
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Software
      Image Management (SWIM) InitiatesSyncOfSoftwareImagesFromCiscoCom
    description: Complete reference of the InitiatesSyncOfSoftwareImagesFromCiscoCom
      API.
    link: https://developer.cisco.com/docs/dna-center/#!initiates-sync-of-software-images-from-cisco-com
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.initiates_sync_of_software_images_from_cisco_com,
  - Paths used are
    post /dna/intent/api/v1/images/ccoSync,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.images_cco_sync:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
