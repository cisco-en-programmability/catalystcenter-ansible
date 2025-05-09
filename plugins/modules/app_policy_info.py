#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: app_policy_info
short_description: Information module for App Policy Info
description:
  - This module represents an alias of the module app_policy_v1_info
version_added: '4.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  policyScope:
    description:
      - PolicyScope query parameter. Policy scope name.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Application Policy GetApplicationPolicyV1
    description: Complete reference of the GetApplicationPolicyV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-application-policy
notes:
  - SDK Method used are application_policy.ApplicationPolicy.get_application_policy_v1,
  - Paths used are get /dna/intent/api/v1/app-policy,
  - It should be noted that this module is an alias of app_policy_v1_info
"""
EXAMPLES = r"""
- name: Get all App Policy Info
  cisco.catalystcenter.app_policy_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    policyScope: string
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
            {}
          ],
          "type": "string",
          "cfsChangeInfo": [
            {}
          ],
          "customProvisions": [
            {}
          ],
          "deletePolicyStatus": "string",
          "internal": true,
          "isDeleted": true,
          "isEnabled": true,
          "isScopeStale": true,
          "iseReserved": true,
          "policyScope": "string",
          "policyStatus": "string",
          "priority": 0,
          "pushed": true,
          "advancedPolicyScope": {
            "id": "string",
            "instanceId": 0,
            "displayName": "string",
            "instanceCreatedOn": 0,
            "instanceUpdatedOn": 0,
            "instanceVersion": 0,
            "name": "string",
            "advancedPolicyScopeElement": [
              {
                "id": "string",
                "instanceId": 0,
                "displayName": "string",
                "instanceCreatedOn": 0,
                "instanceUpdatedOn": 0,
                "instanceVersion": 0,
                "groupId": [
                  "string"
                ],
                "ssid": [
                  {}
                ]
              }
            ]
          },
          "contractList": [
            {}
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
                "relevanceLevel": "string",
                "deviceRemovalBehavior": "string",
                "hostTrackingEnabled": true
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
          },
          "consumer": {
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
