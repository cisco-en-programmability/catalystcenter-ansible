#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: file_import_v1
short_description: Resource module for File Import V1
description:
- Manage operation create of the resource File Import V1.
- Uploads a new file within a specific nameSpace.
version_added: '6.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  nameSpace:
    description: NameSpace path parameter.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for File UploadFileV1
  description: Complete reference of the UploadFileV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!upload-file
notes:
  - SDK Method used are
    file.File.upload_file_v1,

  - Paths used are
    post /dna/intent/api/v1/file/{nameSpace},

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.file_import_v1:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    nameSpace: string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
