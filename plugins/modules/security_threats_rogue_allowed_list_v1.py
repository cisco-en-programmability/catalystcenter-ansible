#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: security_threats_rogue_allowed_list_v1
short_description: Resource module for Security Threats Rogue Allowed List V1
description:
  - Manage operations create and delete of the resource Security Threats Rogue Allowed
    List V1.
  - Intent API to add the threat mac address to allowed list.
  - Intent API to remove the threat mac address from allowed list.
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  macAddress:
    description: MacAddress path parameter. Threat mac address which needs to be removed
      from the allowed list. Multiple mac addresses will be removed if provided as
      comma separated values (example 00 2A 10 51 22 43,00 2A 10 51 22 44). Note In
      one request, maximum 100 mac addresses can be removed.
    type: str
  payload:
    description: Security Threats Rogue Allowed List's payload.
    elements: dict
    suboptions:
      category:
        description: Category.
        type: int
      macAddress:
        description: Mac Address.
        type: str
    type: list
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices AddAllowedMacAddressV1
    description: Complete reference of the AddAllowedMacAddressV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!add-allowed-mac-address
  - name: Cisco DNA Center documentation for Devices RemoveAllowedMacAddressV1
    description: Complete reference of the RemoveAllowedMacAddressV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!remove-allowed-mac-address
notes:
  - SDK Method used are devices.Devices.add_allowed_mac_address_v1, devices.Devices.remove_allowed_mac_address_v1,
  - Paths used are post /dna/intent/api/v1/security/threats/rogue/allowed-list, delete
    /dna/intent/api/v1/security/threats/rogue/allowed-list/{macAddress},
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.security_threats_rogue_allowed_list_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    state: present
    payload:
      - category: 0
        macAddress: string
- name: Delete by id
  cisco.catalystcenter.security_threats_rogue_allowed_list_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    state: absent
    macAddress: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": "string",
      "error": {}
    }
"""
