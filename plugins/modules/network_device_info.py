#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_device_info
short_description: Information module for Network Device Info
description:
  - This module represents an alias of the module network_device_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  hostname:
    description:
      - Hostname query parameter.
    elements: str
    type: list
  managementIpAddress:
    description:
      - ManagementIpAddress query parameter.
    elements: str
    type: list
  macAddress:
    description:
      - MacAddress query parameter.
    elements: str
    type: list
  locationName:
    description:
      - LocationName query parameter.
    elements: str
    type: list
  serialNumber:
    description:
      - SerialNumber query parameter.
    elements: str
    type: list
  location:
    description:
      - Location query parameter.
    elements: str
    type: list
  family:
    description:
      - Family query parameter.
    elements: str
    type: list
  type:
    description:
      - Type query parameter.
    elements: str
    type: list
  series:
    description:
      - Series query parameter.
    elements: str
    type: list
  collectionStatus:
    description:
      - CollectionStatus query parameter.
    elements: str
    type: list
  collectionInterval:
    description:
      - CollectionInterval query parameter.
    elements: str
    type: list
  notSyncedForMinutes:
    description:
      - NotSyncedForMinutes query parameter.
    elements: str
    type: list
  errorCode:
    description:
      - ErrorCode query parameter.
    elements: str
    type: list
  errorDescription:
    description:
      - ErrorDescription query parameter.
    elements: str
    type: list
  softwareVersion:
    description:
      - SoftwareVersion query parameter.
    elements: str
    type: list
  softwareType:
    description:
      - SoftwareType query parameter.
    elements: str
    type: list
  platformId:
    description:
      - PlatformId query parameter.
    elements: str
    type: list
  role:
    description:
      - Role query parameter.
    elements: str
    type: list
  reachabilityStatus:
    description:
      - ReachabilityStatus query parameter.
    elements: str
    type: list
  upTime:
    description:
      - UpTime query parameter.
    elements: str
    type: list
  associatedWlcIp:
    description:
      - AssociatedWlcIp query parameter.
    elements: str
    type: list
  license_name:
    description:
      - License.name query parameter.
    elements: str
    type: list
  license_type:
    description:
      - License.type query parameter.
    elements: str
    type: list
  license_status:
    description:
      - License.status query parameter.
    elements: str
    type: list
  module_name:
    description:
      - Module+name query parameter.
    elements: str
    type: list
  module_equpimenttype:
    description:
      - Module+equpimenttype query parameter.
    elements: str
    type: list
  module_servicestate:
    description:
      - Module+servicestate query parameter.
    elements: str
    type: list
  module_vendorequipmenttype:
    description:
      - Module+vendorequipmenttype query parameter.
    elements: str
    type: list
  module_partnumber:
    description:
      - Module+partnumber query parameter.
    elements: str
    type: list
  module_operationstatecode:
    description:
      - Module+operationstatecode query parameter.
    elements: str
    type: list
  id:
    description:
      - >
        Id query parameter. Accepts comma separated ids and return list of network-devices
        for the given ids. If
        invalid or not-found ids are provided, null entry will be returned in the
        list.
    type: str
  deviceSupportLevel:
    description:
      - DeviceSupportLevel query parameter.
    type: str
  offset:
    description:
      - Offset query parameter. Offset >= 1 X gives results from Xth device onwards.
    type: int
  limit:
    description:
      - Limit query parameter. The number of records to show for this page. Min 1,
        Max 500.
    type: int
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices GetDeviceByIDV1
    description: Complete reference of the GetDeviceByIDV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-device-by-id
  - name: Cisco DNA Center documentation for Devices GetDeviceListV1
    description: Complete reference of the GetDeviceListV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-device-list
notes:
  - SDK Method used are devices.Devices.get_device_by_id_v1, devices.Devices.get_device_list_v1,
  - Paths used are get /dna/intent/api/v1/network-device, get /dna/intent/api/v1/network-device/{id},
  - It should be noted that this module is an alias of network_device_v1_info
"""
EXAMPLES = r"""
- name: Get all Network Device Info
  cisco.catalystcenter.network_device_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    hostname: []
    managementIpAddress: []
    macAddress: []
    locationName: []
    serialNumber: []
    location: []
    family: []
    type: []
    series: []
    collectionStatus: []
    collectionInterval: []
    notSyncedForMinutes: []
    errorCode: []
    errorDescription: []
    softwareVersion: []
    softwareType: []
    platformId: []
    role: []
    reachabilityStatus: []
    upTime: []
    associatedWlcIp: []
    license_name: []
    license_type: []
    license_status: []
    module_name: []
    module_equpimenttype: []
    module_servicestate: []
    module_vendorequipmenttype: []
    module_partnumber: []
    module_operationstatecode: []
    id: string
    deviceSupportLevel: string
    offset: 0
    limit: 0
  register: result
- name: Get Network Device Info by id
  cisco.catalystcenter.network_device_info:
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
