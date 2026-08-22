#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: user_enrichment_details_v3_info
short_description: Information module for User Enrichment Details V3
description:
  - Get all User Enrichment Details V3. - > Enriches a given network End User context a network user-id or end user's device
    Mac Address with details about the user and devices that the user is connected to.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Users UserEnrichmentDetails
    description: Complete reference of the UserEnrichmentDetails API.
    link: https://developer.cisco.com/docs/dna-center/#!user-enrichment-details
notes:
  - SDK Method used are
    users.Users.user_enrichment_details,
  - Paths used are
    get /dna/intent/api/v1/userEnrichmentDetails,
"""

EXAMPLES = r"""
---
- name: Get all User Enrichment Details V3
  cisco.catalystcenter.user_enrichment_details_v3_info:
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
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "response": [
          {
            "userDetails": {
              "id": "string",
              "connectionStatus": "string",
              "tracked": "string",
              "hostType": "string",
              "userId": "string",
              "duId": "string",
              "identifier": "string",
              "hostName": "string",
              "hostOs": "string",
              "hostVersion": "string",
              "subType": "string",
              "lastUpdatedTime": 0,
              "firmwareVersion": "string",
              "deviceVendor": "string",
              "deviceForm": "string",
              "salesCode": "string",
              "countryCode": "string",
              "healthScore": [
                {
                  "healthType": "string",
                  "reason": "string",
                  "score": 0
                }
              ],
              "hostMac": "string",
              "hostIpV4": "string",
              "hostIpV6": [
                "string"
              ],
              "authType": "string",
              "vlanId": 0,
              "l3VirtualNetwork": "string",
              "l2VirtualNetwork": "string",
              "vnId": "string",
              "upnId": "string",
              "upnName": "string",
              "ssId": "string",
              "frequency": "string",
              "channel": "string",
              "apGroup": "string",
              "location": "string",
              "clientConnection": "string",
              "connectedDevice": [
                {
                  "type": "string",
                  "name": "string",
                  "mac": "string",
                  "id": "string",
                  "ipAddress": "string",
                  "mgmtIp": "string",
                  "band": "string",
                  "mode": "string"
                }
              ],
              "issueCount": 0,
              "rssi": "string",
              "rssiThreshold": "string",
              "rssiIsInclude": "string",
              "avgRssi": "string",
              "snr": "string",
              "snrThreshold": "string",
              "snrIsInclude": "string",
              "avgSnr": "string",
              "dataRate": "string",
              "txBytes": "string",
              "rxBytes": "string",
              "dnsResponse": "string",
              "dnsRequest": "string",
              "onboarding": {
                "averageRunDuration": "string",
                "maxRunDuration": "string",
                "averageAssocDuration": "string",
                "maxAssocDuration": "string",
                "averageAuthDuration": "string",
                "maxAuthDuration": "string",
                "averageDhcpDuration": "string",
                "maxDhcpDuration": "string",
                "aaaServerIp": "string",
                "dhcpServerIp": "string",
                "authDoneTime": 0,
                "assocDoneTime": 0,
                "dhcpDoneTime": 0,
                "dhcpRootCauseList": [
                  "string"
                ],
                "latestRootCauseList": [
                  "string"
                ]
              },
              "clientType": "string",
              "onboardingTime": 0,
              "port": "string",
              "iosCapable": true,
              "usage": 0,
              "linkSpeed": 0,
              "linkThreshold": "string",
              "remoteEndDuplexMode": "string",
              "txLinkError": 0,
              "rxLinkError": 0,
              "txRate": 0,
              "rxRate": 0,
              "rxRetryPct": "string",
              "versionTime": "string",
              "dot11Protocol": "string",
              "slotId": 0,
              "dot11ProtocolCapability": "string",
              "privateMac": true,
              "dhcpServerIp": "string",
              "aaaServerIp": "string",
              "aaaServerTransaction": "string",
              "aaaServerFailedTransaction": "string",
              "aaaServerSuccessTransaction": "string",
              "aaaServerLatency": "string",
              "aaaServerMABLatency": "string",
              "aaaServerEAPLatency": "string",
              "dhcpServerTransaction": "string",
              "dhcpServerFailedTransaction": "string",
              "dhcpServerSuccessTransaction": "string",
              "dhcpServerLatency": "string",
              "dhcpServerDOLatency": "string",
              "dhcpServerRALatency": "string",
              "maxRoamingDuration": "string",
              "upnOwner": "string",
              "connectedUpn": "string",
              "connectedUpnOwner": "string",
              "connectedUpnId": "string",
              "isGuestUPNEndpoint": true,
              "wlcName": "string",
              "wlcUuid": "string",
              "sessionDuration": "string",
              "intelCapable": true,
              "hwModel": "string",
              "powerType": "string",
              "modelName": "string",
              "bridgeVMMode": "string",
              "dhcpNakIp": "string",
              "dhcpDeclineIp": "string",
              "portDescription": "string",
              "latencyVoice": 0,
              "latencyVideo": 0,
              "latencyBg": 0,
              "latencyBe": 0,
              "trustScore": "string",
              "trustDetails": "string"
            },
            "connectedDevice": [
              {
                "deviceDetails": {
                  "family": "string",
                  "type": "string",
                  "location": {},
                  "errorCode": "string",
                  "macAddress": "string",
                  "role": "string",
                  "apManagerInterfaceIp": "string",
                  "associatedWlcIp": "string",
                  "bootDateTime": "string",
                  "collectionStatus": "string",
                  "interfaceCount": "string",
                  "lineCardCount": "string",
                  "lineCardId": "string",
                  "managementIpAddress": "string",
                  "memorySize": "string",
                  "platformId": "string",
                  "reachabilityFailureReason": "string",
                  "reachabilityStatus": "string",
                  "snmpContact": "string",
                  "snmpLocation": "string",
                  "tunnelUdpPort": {},
                  "waasDeviceMode": {},
                  "series": "string",
                  "inventoryStatusDetail": "string",
                  "collectionInterval": "string",
                  "serialNumber": "string",
                  "softwareVersion": "string",
                  "roleSource": "string",
                  "hostname": "string",
                  "upTime": "string",
                  "lastUpdatedTime": 0,
                  "errorDescription": "string",
                  "locationName": {},
                  "tagCount": "string",
                  "createdDateTime": "string",
                  "id": "string",
                  "neighborTopology": {
                    "nodes": [
                      {
                        "role": "string",
                        "name": "string",
                        "id": "string",
                        "description": "string",
                        "deviceType": "string",
                        "platformId": "string",
                        "family": "string",
                        "ip": "string",
                        "softwareVersion": "string",
                        "userId": {},
                        "nodeType": "string",
                        "radioFrequency": {},
                        "clients": {},
                        "count": {},
                        "healthScore": 0,
                        "level": 0,
                        "fabricGroup": {},
                        "connectedDevice": {},
                        "fabricRole": [
                          "string"
                        ],
                        "stackType": "string",
                        "additionalInfo": {}
                      }
                    ],
                    "links": [
                      {
                        "source": "string",
                        "label": [
                          {}
                        ],
                        "target": "string",
                        "id": {},
                        "portUtilization": {},
                        "linkStatus": "string",
                        "sourcelinkStatus": "string",
                        "targetlinkStatus": "string",
                        "sourceInterfaceName": "string",
                        "targetInterfaceName": "string",
                        "sourceDuplexInfo": "string",
                        "targetDuplexInfo": "string",
                        "sourcePortMode": "string",
                        "targetPortMode": "string",
                        "sourceAdminStatus": "string",
                        "targetAdminStatus": "string",
                        "apRadioAdminStatus": "string",
                        "apRadioOperStatus": "string",
                        "sourcePortVLANInfo": "string",
                        "targetPortVLANInfo": "string"
                      }
                    ]
                  }
                }
              }
            ]
          }
        ],
        "version": "string"
      }
    ]
"""
