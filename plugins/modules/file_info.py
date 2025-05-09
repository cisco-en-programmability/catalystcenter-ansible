#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: file_info
short_description: Information module for File Info
description:
  - This module represents an alias of the module file_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  fileId:
    description:
      - FileId path parameter. File Identification number.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for File DownloadAFileByFileIdV1
    description: Complete reference of the DownloadAFileByFileIdV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!download-a-file-by-file-id
notes:
  - SDK Method used are file.File.download_a_file_by_fileid,
  - Paths used are get /dna/intent/api/v1/file/{fileId},
  - It should be noted that this module is an alias of file_v1_info
"""
EXAMPLES = r"""
- name: Get File Info by id
  cisco.catalystcenter.file_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    fileId: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "data": "filecontent",
      "filename": "filename",
      "dirpath": "download/directory",
      "path": "download/directory/filename"
    }
"""
