#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: images_transfer_protocol_settings_info
short_description: Information module for Images Transfer Protocol Settings
description:
  - Get all Images Transfer Protocol Settings.
  - This API is used to fetch the preferred protocols used to distribute software images to network devices.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Software Image Management (SWIM) ImageTransferProtocolSettings
    description: Complete reference of the ImageTransferProtocolSettings API.
    link: https://developer.cisco.com/docs/dna-center/#!image-transfer-protocol-settings
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.image_transfer_protocol_settings,
  - Paths used are
    get /dna/intent/api/v1/images/transferProtocolSettings,
"""

EXAMPLES = r"""
---
- name: Get all Images Transfer Protocol Settings
  cisco.catalystcenter.images_transfer_protocol_settings_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "imageCopyProtocolOrder": [
            "string"
          ],
          "wlcToApImageCopyProtocol": [
            "string"
          ]
        }
      ],
      "version": "string"
    }
"""
