#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wirelessSettings_interfaces_info
short_description: Information module for Wirelesssettings Interfaces
description:
- Get all Wirelesssettings Interfaces.
- Get Wirelesssettings Interfaces by id.
- This API allows the user to get all Interfaces.
- This API allows the user to get an interface by ID.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  limit:
    description:
    - Limit query parameter.
    type: float
  offset:
    description:
    - Offset query parameter.
    type: float
  id:
    description:
    - Id path parameter. Interface ID.
    type: str
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Wireless GetInterfaceByIDV1
  description: Complete reference of the GetInterfaceByIDV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-interface-by-id-v-1
- name: Cisco CATALYST Center documentation for Wireless GetInterfacesV1
  description: Complete reference of the GetInterfacesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-interfaces-v-1
notes:
  - SDK Method used are
    wireless.Wireless.get_interface_by_id_v1,
    wireless.Wireless.get_interfaces_v1,

  - Paths used are
    get /dna/intent/api/v1/wirelessSettings/interfaces,
    get /dna/intent/api/v1/wirelessSettings/interfaces/{id},

"""

EXAMPLES = r"""
- name: Get all Wirelesssettings Interfaces
  cisco.catalystcenter.wirelessSettings_interfaces_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    limit: 0
    offset: 0
  register: result

- name: Get Wirelesssettings Interfaces by id
  cisco.catalystcenter.wirelessSettings_interfaces_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "interfaceName": "string",
        "vlanId": 0,
        "id": "string"
      },
      "version": "string"
    }
"""
