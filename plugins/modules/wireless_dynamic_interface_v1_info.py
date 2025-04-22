#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: wireless_dynamic_interface_v1_info
short_description: Information module for Wireless Dynamic Interface V1
description:
  - Get all Wireless Dynamic Interface V1.
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
        Interface-name query parameter. Dynamic-interface name, if not specified all
        the existing dynamic interfaces
        will be retrieved.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless GetDynamicInterfaceV1
    description: Complete reference of the GetDynamicInterfaceV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-dynamic-interface
notes:
  - SDK Method used are wireless.Wireless.get_dynamic_interface_v1,
  - Paths used are get /dna/intent/api/v1/wireless/dynamic-interface,
"""
EXAMPLES = r"""
- name: Get all Wireless Dynamic Interface V1
  cisco.catalystcenter.wireless_dynamic_interface_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    interface_name: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
