#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: file_import
short_description: Resource module for File Import
description:
  - Manage operation create of the resource File Import.
  - Uploads a new file within a specific nameSpace.
version_added: '6.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  filePath:
    description: File absolute path.
    type: str
  nameSpace:
    description: NameSpace path parameter.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for File UploadFile
    description: Complete reference of the UploadFile
      API.
    link: https://developer.cisco.com/docs/dna-center/#!upload-file
notes:
  - SDK Method used are
    file.File.upload_file,
  - Paths used are
    post /dna/intent/api/v1/file/{nameSpace},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.file_import:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    filePath: /tmp/uploads/Test-242.bin
    nameSpace: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
