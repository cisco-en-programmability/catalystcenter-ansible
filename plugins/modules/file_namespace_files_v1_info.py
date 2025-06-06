#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: file_namespace_files_v1_info
short_description: Information module for File Namespace Files V1
description:
  - Get File Namespace Files V1 by name.
  - Returns list of files under a specific namespace.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  nameSpace:
    description:
      - NameSpace path parameter. A listing of fileId's.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for File GetListOfFilesV1
    description: Complete reference of the GetListOfFilesV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-list-of-files
notes:
  - SDK Method used are file.File.get_list_of_files_v1,
  - Paths used are get /dna/intent/api/v1/file/namespace/{nameSpace},
"""
EXAMPLES = r"""
- name: Get File Namespace Files V1 by name
  cisco.catalystcenter.file_namespace_files_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    nameSpace: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "attributeInfo": {},
          "downloadPath": "string",
          "encrypted": true,
          "fileFormat": "string",
          "fileSize": "string",
          "id": "string",
          "md5Checksum": "string",
          "name": "string",
          "nameSpace": "string",
          "sftpServerList": [
            {}
          ],
          "sha1Checksum": "string",
          "taskId": "string"
        }
      ],
      "version": "string"
    }
"""
