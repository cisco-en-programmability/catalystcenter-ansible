#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: authentication_policy_servers_info
short_description: Information module for Authentication Policy Servers Info
description:
- This module represents an alias of the module authentication_policy_servers_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  isIseEnabled:
    description:
    - IsIseEnabled query parameter. Valid values are true, false.
    type: bool
  state_:
    description:
    - State query parameter. Valid values are ACTIVE, DELETED, FAILED, INACTIVE, INPROGRESS, RBAC-FAILURE, RBAC-SUCCESS.
    type: str
  role:
    description:
    - Role query parameter. Authentication and Policy Server Role (Example primary, secondary).
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for System Settings GetAuthenticationAndPolicyServersV1
  description: Complete reference of the GetAuthenticationAndPolicyServersV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-authentication-and-policy-servers
notes:
  - SDK Method used are
    system_settings.SystemSettings.get_authentication_and_policy_servers_v1,

  - Paths used are
    get /dna/intent/api/v1/authentication-policy-servers,
  - It should be noted that this module is an alias of authentication_policy_servers_v1_info

"""

EXAMPLES = r"""
- name: Get all Authentication Policy Servers Info
  cisco.catalystcenter.authentication_policy_servers_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    isIseEnabled: True
    state_: string
    role: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "ipAddress": "string",
          "sharedSecret": "string",
          "protocol": "string",
          "role": "string",
          "port": 0,
          "authenticationPort": 0,
          "accountingPort": 0,
          "retries": 0,
          "timeoutSeconds": 0,
          "isIseEnabled": true,
          "instanceUuid": "string",
          "state": "string",
          "ciscoIseDtos": [
            {
              "subscriberName": "string",
              "description": "string",
              "password": "string",
              "userName": "string",
              "fqdn": "string",
              "ipAddress": "string",
              "trustState": "string",
              "instanceUuid": "string",
              "sshkey": "string",
              "type": "string",
              "failureReason": "string",
              "role": "string",
              "externalCiscoIseIpAddrDtos": {
                "type": "string",
                "externalCiscoIseIpAddresses": [
                  {
                    "externalIpAddress": "string"
                  }
                ]
              }
            }
          ],
          "encryptionScheme": "string",
          "messageKey": "string",
          "encryptionKey": "string",
          "useDnacCertForPxgrid": true,
          "iseEnabled": true,
          "pxgridEnabled": true,
          "rbacUuid": "string",
          "multiDnacEnabled": true
        }
      ],
      "version": "string"
    }
"""
