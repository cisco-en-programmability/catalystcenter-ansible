#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: global_credentials_count_info
short_description: Information module for Global Credentials Count
description:
  - Get all Global Credentials Count.
  - API to get count of the global credentials based on the given filter.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  type:
    description:
      - Type query parameter. Returns count of global credentials for the given credential type.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Network Settings GetCountOfTheGlobalCredentials
    description: Complete reference of the GetCountOfTheGlobalCredentials API.
    link: https://developer.cisco.com/docs/dna-center/#!get-count-of-the-global-credentials
notes:
  - SDK Method used are
    network_settings.NetworkSettings.get_count_of_the_global_credentials,
  - Paths used are
    get /dna/intent/api/v1/globalCredentials/count,
"""

EXAMPLES = r"""
---
- name: Get all Global Credentials Count
  cisco.catalystcenter.global_credentials_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    type: string
  register: result
"""
RETURN = r"""
dnac_response:
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
