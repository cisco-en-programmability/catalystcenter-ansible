#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: discovery_info
short_description: Information module for Discovery Info
description:
  - This module represents an alias of the module discovery_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Discovery ID.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Discovery GetDiscoveryByIdV1
    description: Complete reference of the GetDiscoveryByIdV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-discovery-by-id
notes:
  - SDK Method used are discovery.Discovery.get_discovery_by_id_v1,
  - Paths used are get /dna/intent/api/v1/discovery/{id},
  - It should be noted that this module is an alias of discovery_v1_info
"""
EXAMPLES = r"""
- name: Get Discovery Info by id
  cisco.catalystcenter.discovery_info:
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
        "attributeInfo": {},
        "cdpLevel": 0,
        "deviceIds": "string",
        "discoveryCondition": "string",
        "discoveryStatus": "string",
        "discoveryType": "string",
        "enablePasswordList": "string",
        "globalCredentialIdList": [
          "string"
        ],
        "httpReadCredential": {
          "comments": "string",
          "credentialType": "string",
          "description": "string",
          "id": "string",
          "instanceTenantId": "string",
          "instanceUuid": "string",
          "password": "string",
          "port": 0,
          "secure": true,
          "username": "string"
        },
        "httpWriteCredential": {
          "comments": "string",
          "credentialType": "string",
          "description": "string",
          "id": "string",
          "instanceTenantId": "string",
          "instanceUuid": "string",
          "password": "string",
          "port": 0,
          "secure": true,
          "username": "string"
        },
        "id": "string",
        "ipAddressList": "string",
        "ipFilterList": "string",
        "isAutoCdp": true,
        "lldpLevel": 0,
        "name": "string",
        "netconfPort": "string",
        "numDevices": 0,
        "parentDiscoveryId": "string",
        "passwordList": "string",
        "preferredMgmtIPMethod": "string",
        "protocolOrder": "string",
        "retryCount": 0,
        "snmpAuthPassphrase": "string",
        "snmpAuthProtocol": "string",
        "snmpMode": "string",
        "snmpPrivPassphrase": "string",
        "snmpPrivProtocol": "string",
        "snmpRoCommunity": "string",
        "snmpRoCommunityDesc": "string",
        "snmpRwCommunity": "string",
        "snmpRwCommunityDesc": "string",
        "snmpUserName": "string",
        "timeOut": 0,
        "updateMgmtIp": true,
        "userNameList": "string"
      },
      "version": "string"
    }
"""
