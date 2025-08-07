#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: file_namespaces_info
short_description: Information module for File Namespaces
description:
  - Get all File Namespaces.
  - Returns list of available namespaces.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for File GetListOfAvailableNamespaces
    description: Complete reference of the GetListOfAvailableNamespaces
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-list-of-available-namespaces
notes:
  - SDK Method used are
    file.File.get_list_of_available_namespaces,
  - Paths used are
    get /dna/intent/api/v1/file/namespace,
"""

EXAMPLES = r"""
---
- name: Get all File Namespaces
  cisco.catalystcenter.file_namespaces_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
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
        "string"
      ],
      "version": "string"
    }
"""
