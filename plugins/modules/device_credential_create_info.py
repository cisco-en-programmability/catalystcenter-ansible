#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_credential_create_info
short_description: Information module for Device Credential Create
description:
- Get all Device Credential Create.
- >
   API to get device credential details. This API has been deprecated and will not be available in a Cisco CATALYST Center
   release after August 1st 2024 23 59 59 GMT. Please refer new Intent API Get All Global Credentials V2.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  siteId:
    description:
    - SiteId query parameter. Site id to retrieve the credential details associated with the site.
    type: str
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Network Settings GetDeviceCredentialDetailsV1
  description: Complete reference of the GetDeviceCredentialDetailsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-device-credential-details-v-1
notes:
  - SDK Method used are
    network_settings.NetworkSettings.get_device_credential_details_v1,

  - Paths used are
    get /dna/intent/api/v1/device-credential,

"""

EXAMPLES = r"""
- name: Get all Device Credential Create
  cisco.catalystcenter.device_credential_create_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    siteId: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "snmp_v3": [
        {
          "username": "string",
          "authPassword": "string",
          "authType": "string",
          "privacyPassword": "string",
          "privacyType": "string",
          "snmpMode": "string",
          "comments": "string",
          "description": "string",
          "credentialType": "string",
          "instanceUuid": "string",
          "instanceTenantId": "string",
          "id": "string"
        }
      ],
      "http_read": [
        {
          "secure": "string",
          "username": "string",
          "password": "string",
          "port": "string",
          "comments": "string",
          "description": "string",
          "credentialType": "string",
          "instanceUuid": "string",
          "instanceTenantId": "string",
          "id": "string"
        }
      ],
      "http_write": [
        {
          "secure": "string",
          "username": "string",
          "password": "string",
          "port": "string",
          "comments": "string",
          "description": "string",
          "credentialType": "string",
          "instanceUuid": "string",
          "instanceTenantId": "string",
          "id": "string"
        }
      ],
      "snmp_v2_write": [
        {
          "writeCommunity": "string",
          "comments": "string",
          "description": "string",
          "credentialType": "string",
          "instanceUuid": "string",
          "instanceTenantId": "string",
          "id": "string"
        }
      ],
      "snmp_v2_read": [
        {
          "readCommunity": "string",
          "comments": "string",
          "description": "string",
          "credentialType": "string",
          "instanceUuid": "string",
          "instanceTenantId": "string",
          "id": "string"
        }
      ],
      "cli": [
        {
          "username": "string",
          "enablePassword": "string",
          "password": "string",
          "comments": "string",
          "description": "string",
          "credentialType": "string",
          "instanceUuid": "string",
          "instanceTenantId": "string",
          "id": "string"
        }
      ]
    }
"""
