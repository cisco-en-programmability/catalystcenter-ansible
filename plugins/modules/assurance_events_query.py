#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: assurance_events_query
short_description: Resource module for Assurance Events Query
description:
  - Manage operation create of the resource Assurance Events Query.
  - Returns the list of events discovered by Catalyst Center, determined by the.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  attributes:
    description: Assurance Events Query's attributes.
    elements: str
    type: list
  deviceFamily:
    description: Assurance Events Query's deviceFamily.
    elements: str
    type: list
  endTime:
    description: Assurance Events Query's endTime.
    type: int
  filters:
    description: Assurance Events Query's filters.
    elements: dict
    suboptions:
      key:
        description: Assurance Events Query's key.
        type: str
      operator:
        description: Assurance Events Query's operator.
        type: str
      value:
        description: Assurance Events Query's value.
        type: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  page:
    description: Assurance Events Query's page.
    suboptions:
      limit:
        description: Assurance Events Query's limit.
        type: int
      offset:
        description: Assurance Events Query's offset.
        type: int
      sortBy:
        description: Assurance Events Query's sortBy.
        elements: dict
        suboptions:
          name:
            description: Assurance Events Query's name.
            type: str
          order:
            description: Assurance Events Query's order.
            type: str
        type: list
    type: dict
  startTime:
    description: Assurance Events Query's startTime.
    type: int
  views:
    description: Assurance Events Query's views.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices QueryAssuranceEventsWithFilters
    description: Complete reference of the QueryAssuranceEventsWithFilters API.
    link: https://developer.cisco.com/docs/dna-center/#!query-assurance-events-with-filters
notes:
  - SDK Method used are
    devices.Devices.query_assurance_events_with_filters,
  - Paths used are
    post /dna/data/api/v1/assuranceEvents/query,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.assurance_events_query:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    attributes:
      - string
    deviceFamily:
      - string
    endTime: 0
    filters:
      - key: string
        operator: string
        value: string
    headers: '{{my_headers | from_json}}'
    page:
      limit: 0
      offset: 0
      sortBy:
        - name: string
          order: string
    startTime: 0
    views:
      - string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "oldRadioChannelWidth": "string",
          "clientMac": "string",
          "switchNumber": "string",
          "assocRssi": 0,
          "affectedClients": [
            "string"
          ],
          "isPrivateMac": true,
          "frequency": "string",
          "apRole": "string",
          "replacingDeviceSerialNumber": "string",
          "messageType": "string",
          "failureCategory": "string",
          "apSwitchName": "string",
          "apSwitchId": "string",
          "radioChannelUtilization": "string",
          "mnemonic": "string",
          "radioChannelSlot": 0,
          "details": "string",
          "id": "string",
          "lastApDisconnectReason": "string",
          "networkDeviceName": "string",
          "identifier": "string",
          "reasonDescription": "string",
          "vlanId": "string",
          "udnId": "string",
          "auditSessionId": "string",
          "apMac": "string",
          "deviceFamily": "string",
          "radioNoise": "string",
          "wlcName": "string",
          "apRadioOperationState": "string",
          "name": "string",
          "failureIpAddress": "string",
          "newRadioChannelList": "string",
          "duid": "string",
          "roamType": "string",
          "candidateAPs": [
            {
              "apId": "string",
              "apName": "string",
              "apMac": "string",
              "bssid": "string",
              "rssi": 0
            }
          ],
          "replacedDeviceSerialNumber": "string",
          "oldRadioChannelList": "string",
          "ssid": "string",
          "subReasonDescription": "string",
          "wirelessClientEventEndTime": 0,
          "ipv4": "string",
          "wlcId": "string",
          "ipv6": "string",
          "missingResponseAPs": [
            {
              "apId": "string",
              "apName": "string",
              "apMac": "string",
              "bssid": "string",
              "type": "string",
              "frameType": "string"
            }
          ],
          "timestamp": 0,
          "severity": 0,
          "currentRadioPowerLevel": 0,
          "newRadioChannelWidth": "string",
          "assocSnr": 0,
          "authServerIp": "string",
          "childEvents": [
            {
              "id": "string",
              "name": "string",
              "timestamp": 0,
              "wirelessEventType": 0,
              "details": "string",
              "reasonCode": "string",
              "reasonDescription": "string",
              "subReasonCode": "string",
              "subReasonDescription": "string",
              "resultStatus": "string",
              "failureCategory": "string"
            }
          ],
          "connectedInterfaceName": "string",
          "dhcpServerIp": "string",
          "managementIpAddress": "string",
          "previousRadioPowerLevel": 0,
          "resultStatus": "string",
          "radioInterference": "string",
          "networkDeviceId": "string",
          "siteHierarchy": "string",
          "eventStatus": "string",
          "wirelessClientEventStartTime": 0,
          "siteHierarchyId": "string",
          "udnName": "string",
          "facility": "string",
          "lastApResetType": "string",
          "invalidIeAPs": [
            {
              "apId": "string",
              "apName": "string",
              "apMac": "string",
              "bssid": "string",
              "type": "string",
              "frameType": "string",
              "ies": "string"
            }
          ],
          "username": "string"
        }
      ],
      "version": "string",
      "page": {
        "limit": 0,
        "offset": 0,
        "count": 0,
        "sortBy": [
          {
            "name": "string",
            "order": "string"
          }
        ]
      }
    }
"""
