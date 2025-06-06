#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: sda_fabric_border_device_v1_info
short_description: Information module for Sda Fabric Border Device V1
description:
  - Get all Sda Fabric Border Device V1.
  - Get border device detail from SDA Fabric.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deviceManagementIpAddress:
    version_added: "4.0.0"
    description:
      - DeviceManagementIpAddress query parameter.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA GetBorderDeviceDetailFromSDAFabricV1
    description: Complete reference of the GetBorderDeviceDetailFromSDAFabricV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-border-device-detail-from-sda-fabric
notes:
  - SDK Method used are sda.Sda.gets_border_device_detail,
  - Paths used are get /dna/intent/api/v1/business/sda/border-device,
"""
EXAMPLES = r"""
- name: Get all Sda Fabric Border Device V1
  cisco.catalystcenter.sda_fabric_border_device_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    deviceManagementIpAddress: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "status": "string",
      "description": "string",
      "payload": {
        "id": "string",
        "instanceId": 0,
        "authEntityId": 0,
        "displayName": "string",
        "authEntityClass": 0,
        "instanceTenantId": "string",
        "deployPending": "string",
        "instanceVersion": 0,
        "createTime": 0,
        "deployed": true,
        "isSeeded": true,
        "isStale": true,
        "lastUpdateTime": 0,
        "name": "string",
        "namespace": "string",
        "provisioningState": "string",
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
        "configs": [
          {}
        ],
        "managedSites": [
          {}
        ],
        "networkDeviceId": "string",
        "roles": [
          "string"
        ],
        "saveWanConnectivityDetailsOnly": true,
        "siteId": "string",
        "akcSettingsCfs": [
          {}
        ],
        "deviceInterfaceInfo": [
          {}
        ],
        "deviceSettings": {
          "id": "string",
          "instanceId": 0,
          "displayName": "string",
          "instanceTenantId": "string",
          "deployPending": "string",
          "instanceVersion": 0,
          "connectedTo": [
            {}
          ],
          "cpu": 0,
          "dhcpEnabled": true,
          "externalConnectivityIpPool": "string",
          "externalDomainRoutingProtocol": "string",
          "internalDomainProtocolNumber": "string",
          "memory": 0,
          "nodeType": [
            "string"
          ],
          "storage": 0,
          "extConnectivitySettings": [
            {
              "id": "string",
              "instanceId": 0,
              "displayName": "string",
              "instanceTenantId": "string",
              "deployPending": "string",
              "instanceVersion": 0,
              "externalDomainProtocolNumber": "string",
              "interfaceUuid": "string",
              "policyPropagationEnabled": true,
              "policySgtTag": 0,
              "l2Handoff": [
                {}
              ],
              "l3Handoff": [
                {
                  "id": "string",
                  "instanceId": 0,
                  "displayName": "string",
                  "instanceTenantId": "string",
                  "deployPending": "string",
                  "instanceVersion": 0,
                  "localIpAddress": "string",
                  "remoteIpAddress": "string",
                  "vlanId": 0,
                  "virtualNetwork": {
                    "idRef": "string"
                  }
                }
              ]
            }
          ]
        },
        "networkWideSettings": {
          "id": "string",
          "instanceId": 0,
          "displayName": "string",
          "instanceTenantId": "string",
          "deployPending": "string",
          "instanceVersion": 0,
          "aaa": [
            {}
          ],
          "cmx": [
            {}
          ],
          "dhcp": [
            {
              "id": "string",
              "ipAddress": {
                "id": "string",
                "paddedAddress": "string",
                "addressType": "string",
                "address": "string"
              }
            }
          ],
          "dns": [
            {
              "id": "string",
              "domainName": "string",
              "ip": {
                "id": "string",
                "paddedAddress": "string",
                "addressType": "string",
                "address": "string"
              }
            }
          ],
          "ldap": [
            {}
          ],
          "nativeVlan": [
            {}
          ],
          "netflow": [
            {}
          ],
          "ntp": [
            {}
          ],
          "snmp": [
            {}
          ],
          "syslogs": [
            {}
          ]
        },
        "otherDevice": [
          {}
        ],
        "transitNetworks": [
          {
            "idRef": "string"
          }
        ],
        "virtualNetwork": [
          {}
        ],
        "wlan": [
          {}
        ]
      }
    }
"""
