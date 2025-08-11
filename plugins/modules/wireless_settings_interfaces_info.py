#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_settings_interfaces_info
short_description: Information module for Wireless Settings
  Interfaces
description:
  - Get all Wireless Settings Interfaces.
  - Get Wireless Settings Interfaces by id.
  - This API allows the user to get all Interfaces.
  - This API allows the user to get an interface by
    ID.
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
      - >
        Limit query parameter. The number of records
        to show for this page. Default is 500 if not
        specified. Maximum allowed limit is 500.
    type: float
  offset:
    description:
      - Offset query parameter. The first record to
        show for this page. The first record is numbered
        1.
    type: float
  interfaceName:
    description:
      - InterfaceName query parameter. Interface Name.
    type: str
  vlanId:
    description:
      - VlanId query parameter. Vlan Id.
    type: float
  id:
    description:
      - Id path parameter. Interface ID.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless
      GetInterfaceByID
    description: Complete reference of the GetInterfaceByID
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-interface-by-id
  - name: Cisco DNA Center documentation for Wireless
      GetInterfaces
    description: Complete reference of the GetInterfaces
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-interfaces
notes:
  - SDK Method used are
    wireless.Wireless.get_interface_by_id,
    wireless.Wireless.get_interfaces,
  - Paths used are
    get /dna/intent/api/v1/wirelessSettings/interfaces,
    get /dna/intent/api/v1/wirelessSettings/interfaces/{id},
"""

EXAMPLES = r"""
---
- name: Get all Wireless Settings Interfaces
  cisco.catalystcenter.wireless_settings_interfaces_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    limit: 0
    offset: 0
    interfaceName: string
    vlanId: 0
  register: result
- name: Get Wireless Settings Interfaces by id
  cisco.catalystcenter.wireless_settings_interfaces_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
"""
RETURN = r"""
dnac_response:
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
