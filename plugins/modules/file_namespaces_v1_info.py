#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: file_namespaces_v1_info
short_description: Information module for File Namespaces V1
description:
- Get all File Namespaces V1.
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
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for File GetListOfAvailableNamespacesV1
  description: Complete reference of the GetListOfAvailableNamespacesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-list-of-available-namespaces
notes:
  - SDK Method used are
    file.File.get_list_of_available_namespaces_v1,

  - Paths used are
    get /dna/intent/api/v1/file/namespace,

"""

EXAMPLES = r"""
- name: Get all File Namespaces V1
  cisco.catalystcenter.file_namespaces_v1_info:
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
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
