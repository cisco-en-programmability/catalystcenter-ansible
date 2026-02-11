#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_settings_interfaces_count_info
short_description: Information module for Wireless Settings Interfaces Count
description:
  - Get all Wireless Settings Interfaces Count.
  - This API allows the user to get count of all interfaces.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Wireless GetInterfacesCount
    description: Complete reference of the GetInterfacesCount API.
    link: https://developer.cisco.com/docs/dna-center/#!get-interfaces-count
notes:
  - SDK Method used are
    wireless.Wireless.get_interfaces_count,
  - Paths used are
    get /intent/api/v1/wirelessSettings/interfaces/count,
"""

EXAMPLES = r"""
---
- name: Get all Wireless Settings Interfaces Count
  cisco.catalystcenter.wireless_settings_interfaces_count_info:
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
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "count": 0
      },
      "version": "string"
    }
"""
