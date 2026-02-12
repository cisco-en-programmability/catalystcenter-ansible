#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: app_policy_default_info
short_description: Information module for App Policy Default
description:
  - Get all App Policy Default.
  - Get default application policy.
version_added: '4.0.0'
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
  - name: Cisco DNA Center documentation for Application Policy GetApplicationPolicyDefault
    description: Complete reference of the GetApplicationPolicyDefault API.
    link: https://developer.cisco.com/docs/dna-center/#!get-application-policy-default
notes:
  - SDK Method used are
    application_policy.ApplicationPolicy.get_application_policy_default,
  - Paths used are
    get /dna/intent/api/v1/app-policy-default,
"""

EXAMPLES = r"""
---
- name: Get all App Policy Default
  cisco.catalystcenter.app_policy_default_info:
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
      "response": [
        {
          "id": "string",
          "instanceId": 0,
          "displayName": "string",
          "instanceCreatedOn": 0,
          "instanceUpdatedOn": 0,
          "instanceVersion": 0,
          "createTime": 0,
          "deployed": true,
          "isSeeded": true,
          "isStale": true,
          "lastUpdateTime": 0,
          "name": "string",
          "namespace": "string",
          "provisioningState": "string",
          "qualifier": "string",
          "resourceVersion": 0,
          "targetIdList": [
            "string"
          ],
          "type": "string",
          "cfsChangeInfo": [
            "string"
          ],
          "customProvisions": [
            "string"
          ],
          "deletePolicyStatus": "string",
          "internal": true,
          "isDeleted": true,
          "isEnabled": true,
          "isScopeStale": true,
          "iseReserved": true,
          "policyStatus": "string",
          "priority": 0,
          "pushed": true,
          "contractList": [
            "string"
          ],
          "exclusiveContract": {
            "id": "string",
            "instanceId": 0,
            "displayName": "string",
            "instanceCreatedOn": 0,
            "instanceUpdatedOn": 0,
            "instanceVersion": 0,
            "clause": [
              {
                "id": "string",
                "instanceId": 0,
                "displayName": "string",
                "instanceCreatedOn": 0,
                "instanceUpdatedOn": 0,
                "instanceVersion": 0,
                "priority": 0,
                "type": "string",
                "relevanceLevel": "string"
              }
            ]
          },
          "identitySource": {
            "id": "string",
            "instanceId": 0,
            "displayName": "string",
            "instanceCreatedOn": 0,
            "instanceUpdatedOn": 0,
            "instanceVersion": 0,
            "state": "string",
            "type": "string"
          },
          "producer": {
            "id": "string",
            "instanceId": 0,
            "displayName": "string",
            "instanceCreatedOn": 0,
            "instanceUpdatedOn": 0,
            "instanceVersion": 0,
            "scalableGroup": [
              {
                "idRef": "string"
              }
            ]
          }
        }
      ],
      "version": "string"
    }
"""
