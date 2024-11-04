#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: global_credential_v2_info
short_description: Information module for Global Credential V2
description:
- Get all Global Credential V2.
- >
   API to get device credentials' details. It fetches all global credentials of all types at once, without the need
   to pass any input parameters.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Discovery GetAllGlobalCredentialsV2
  description: Complete reference of the GetAllGlobalCredentialsV2 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-all-global-credentials-v-2
notes:
  - SDK Method used are
    discovery.Discovery.get_all_global_credentials_v2,

  - Paths used are
    get /dna/intent/api/v2/global-credential,

"""

EXAMPLES = r"""
- name: Get all Global Credential V2
  cisco.catalystcenter.global_credential_v2_info:
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
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "cliCredential": [
          {
            "password": "string",
            "username": "string",
            "enablePassword": "string",
            "description": "string",
            "comments": "string",
            "credentialType": "string",
            "instanceTenantId": "string",
            "instanceUuid": "string",
            "id": "string"
          }
        ],
        "snmpV2cRead": [
          {
            "readCommunity": "string",
            "description": "string",
            "comments": "string",
            "credentialType": "string",
            "instanceTenantId": "string",
            "instanceUuid": "string",
            "id": "string"
          }
        ],
        "snmpV2cWrite": [
          {
            "writeCommunity": "string",
            "description": "string",
            "comments": "string",
            "credentialType": "string",
            "instanceTenantId": "string",
            "instanceUuid": "string",
            "id": "string"
          }
        ],
        "httpsRead": [
          {
            "password": "string",
            "port": 0,
            "username": "string",
            "secure": true,
            "description": "string",
            "comments": "string",
            "credentialType": "string",
            "instanceTenantId": "string",
            "instanceUuid": "string",
            "id": "string"
          }
        ],
        "httpsWrite": [
          {
            "password": "string",
            "port": 0,
            "username": "string",
            "secure": true,
            "description": "string",
            "comments": "string",
            "credentialType": "string",
            "instanceTenantId": "string",
            "instanceUuid": "string",
            "id": "string"
          }
        ],
        "snmpV3": [
          {
            "username": "string",
            "authPassword": "string",
            "authType": "string",
            "privacyPassword": "string",
            "privacyType": "string",
            "snmpMode": "string",
            "description": "string",
            "comments": "string",
            "credentialType": "string",
            "instanceTenantId": "string",
            "instanceUuid": "string",
            "id": "string"
          }
        ]
      },
      "version": "string"
    }
"""
