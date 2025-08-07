#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_dynamic_interface_info
short_description: Information module for Wireless Dynamic
  Interface
description:
  - Get all Wireless Dynamic Interface.
  - Get one or all dynamic interfaces.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  interface_name:
    description:
      - >
        Interface-name query parameter. Dynamic-interface
        name, if not specified all the existing dynamic
        interfaces will be retrieved.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless
      GetDynamicInterface
    description: Complete reference of the GetDynamicInterface
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-dynamic-interface
notes:
  - SDK Method used are
    wireless.Wireless.get_dynamic_interface,
  - Paths used are
    get /dna/intent/api/v1/wireless/dynamic-interface,
"""

EXAMPLES = r"""
---
- name: Get all Wireless Dynamic Interface
  cisco.catalystcenter.wireless_dynamic_interface_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    interface_name: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "interfaceName": "string",
        "vlanId": 0
      }
    ]
"""
