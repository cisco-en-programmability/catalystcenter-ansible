#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: app_policy_queuing_profile_info
short_description: Information module for App Policy Queuing Profile
description:
  - Get all App Policy Queuing Profile.
  - Get all or by name, existing application policy queuing profiles.
version_added: '4.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  name:
    description:
      - Name query parameter. Queuing profile name.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Application Policy GetApplicationPolicyQueuingProfile
    description: Complete reference of the GetApplicationPolicyQueuingProfile API.
    link: https://developer.cisco.com/docs/dna-center/#!get-application-policy-queuing-profile
notes:
  - SDK Method used are
    application_policy.ApplicationPolicy.get_application_policy_queuing_profile,
  - Paths used are
    get /dna/intent/api/v1/app-policy-queuing-profile,
"""

EXAMPLES = r"""
---
- name: Get all App Policy Queuing Profile
  cisco.catalystcenter.app_policy_queuing_profile_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    name: string
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
          "description": "string",
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
          "genId": 0,
          "internal": true,
          "isDeleted": true,
          "iseReserved": true,
          "pushed": true,
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
              "isCommonBetweenAllInterfaceSpeeds": true,
              "interfaceSpeedBandwidthClauses": [
                {
                  "id": "string",
                  "instanceId": 0,
                  "displayName": "string",
                  "instanceCreatedOn": 0,
                  "instanceUpdatedOn": 0,
                  "instanceVersion": 0,
                  "interfaceSpeed": "string",
                  "tcBandwidthSettings": [
                    {
                      "id": "string",
                      "instanceId": 0,
                      "displayName": "string",
                      "instanceCreatedOn": 0,
                      "instanceUpdatedOn": 0,
                      "instanceVersion": 0,
                      "bandwidthPercentage": 0,
                      "trafficClass": "string"
                    }
                  ]
                }
              ],
              "tcDscpSettings": [
                {
                  "id": "string",
                  "instanceId": 0,
                  "displayName": "string",
                  "instanceCreatedOn": 0,
                  "instanceUpdatedOn": 0,
                  "instanceVersion": 0,
                  "dscp": "string",
                  "trafficClass": "string"
                }
              ]
            }
          ],
          "contractClassifier": [
            "string"
          ]
        }
      ],
      "version": "string"
    }
"""
