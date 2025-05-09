#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: wireless_settings_interfaces_v1_info
short_description: Information module for Wireless Settings Interfaces V1
description:
  - Get all Wireless Settings Interfaces V1.
  - Get Wireless Settings Interfaces V1 by id.
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
      - >
        Limit query parameter. The number of records to show for this page. Default
        is 500 if not specified. Maximum
        allowed limit is 500.
    type: float
  offset:
    description:
      - Offset query parameter. The first record to show for this page. The first
        record is numbered 1.
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
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless GetInterfaceByIDV1
    description: Complete reference of the GetInterfaceByIDV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-interface-by-id
  - name: Cisco DNA Center documentation for Wireless GetInterfacesV1
    description: Complete reference of the GetInterfacesV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-interfaces
notes:
  - SDK Method used are wireless.Wireless.get_interface_by_id_v1, wireless.Wireless.get_interfaces_v1,
  - Paths used are get /dna/intent/api/v1/wirelessSettings/interfaces, get /dna/intent/api/v1/wirelessSettings/interfaces/{id},
"""
EXAMPLES = r"""
- name: Get all Wireless Settings Interfaces V1
  cisco.catalystcenter.wireless_settings_interfaces_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    limit: 0
    offset: 0
    interfaceName: string
    vlanId: 0
  register: result
- name: Get Wireless Settings Interfaces V1 by id
  cisco.catalystcenter.wireless_settings_interfaces_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
