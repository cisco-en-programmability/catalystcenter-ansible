#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_device_by_serial_number_v1_info
short_description: Information module for Network Device By Serial Number V1
description:
  - Get Network Device By Serial Number V1 by id.
  - Returns the network device with given serial number.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  serialNumber:
    description:
      - SerialNumber path parameter. Device serial number.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices GetDeviceBySerialNumberV1
    description: Complete reference of the GetDeviceBySerialNumberV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-device-by-serial-number
notes:
  - SDK Method used are devices.Devices.get_device_by_serial_number_v1,
  - Paths used are get /dna/intent/api/v1/network-device/serial-number/{serialNumber},
"""
EXAMPLES = r"""
- name: Get Network Device By Serial Number V1 by id
  cisco.catalystcenter.network_device_by_serial_number_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    serialNumber: string
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
        "apManagerInterfaceIp": "string",
        "associatedWlcIp": "string",
        "bootDateTime": "string",
        "collectionInterval": "string",
        "collectionStatus": "string",
        "errorCode": "string",
        "errorDescription": "string",
        "family": "string",
        "hostname": "string",
        "id": "string",
        "instanceTenantId": "string",
        "instanceUuid": "string",
        "interfaceCount": "string",
        "inventoryStatusDetail": "string",
        "lastUpdateTime": 0,
        "lastUpdated": "string",
        "lineCardCount": "string",
        "lineCardId": "string",
        "location": "string",
        "locationName": "string",
        "macAddress": "string",
        "managementIpAddress": "string",
        "memorySize": "string",
        "platformId": "string",
        "reachabilityFailureReason": "string",
        "reachabilityStatus": "string",
        "role": "string",
        "roleSource": "string",
        "serialNumber": "string",
        "series": "string",
        "snmpContact": "string",
        "snmpLocation": "string",
        "softwareType": "string",
        "softwareVersion": "string",
        "tagCount": "string",
        "tunnelUdpPort": "string",
        "type": "string",
        "upTime": "string",
        "waasDeviceMode": "string",
        "dnsResolvedManagementAddress": "string",
        "apEthernetMacAddress": "string",
        "vendor": "string",
        "reasonsForPendingSyncRequests": "string",
        "pendingSyncRequestsCount": "string",
        "reasonsForDeviceResync": "string",
        "lastDeviceResyncStartTime": "string",
        "uptimeSeconds": 0,
        "managedAtleastOnce": true,
        "deviceSupportLevel": "string",
        "managementState": "string",
        "description": "string"
      },
      "version": "string"
    }
"""
