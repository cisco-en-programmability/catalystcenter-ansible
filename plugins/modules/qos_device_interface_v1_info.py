#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: qos_device_interface_v1_info
short_description: Information module for Qos Device Interface V1
description:
  - Get all Qos Device Interface V1.
  - Get all or by network device id, existing qos device interface infos.
version_added: '4.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  networkDeviceId:
    description:
      - NetworkDeviceId query parameter. Network device id.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Application Policy GetQosDeviceInterfaceInfoV1
    description: Complete reference of the GetQosDeviceInterfaceInfoV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-qos-device-interface-info
notes:
  - SDK Method used are application_policy.ApplicationPolicy.get_qos_device_interface_info_v1,
  - Paths used are get /dna/intent/api/v1/qos-device-interface-info,
"""
EXAMPLES = r"""
- name: Get all Qos Device Interface V1
  cisco.catalystcenter.qos_device_interface_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    networkDeviceId: string
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
          "excludedInterfaces": [
            "string"
          ],
          "isExcluded": true,
          "networkDeviceId": "string",
          "qosDeviceInterfaceInfo": [
            {
              "id": "string",
              "instanceId": 0,
              "displayName": "string",
              "instanceCreatedOn": 0,
              "instanceUpdatedOn": 0,
              "instanceVersion": 0,
              "dmvpnRemoteSitesBw": [
                0
              ],
              "downloadBW": 0,
              "interfaceId": "string",
              "interfaceName": "string",
              "label": "string",
              "role": "string",
              "uploadBW": 0
            }
          ]
        }
      ],
      "version": "string"
    }
"""
