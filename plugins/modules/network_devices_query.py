#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_devices_query
short_description: Resource module for Network Devices Query
description:
  - Manage operation create of the resource Network Devices Query.
  - Gets the list of Network Devices based on the provided complex filters and.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  aggregateAttributes:
    description: Network Devices Query's aggregateAttributes.
    elements: dict
    suboptions:
      function:
        description: Network Devices Query's function.
        type: str
      name:
        description: Network Devices Query's name.
        type: str
    type: list
  attributes:
    description: Network Devices Query's attributes.
    elements: str
    type: list
  endTime:
    description: Network Devices Query's endTime.
    type: int
  filters:
    description: Network Devices Query's filters.
    elements: dict
    suboptions:
      key:
        description: Network Devices Query's key.
        type: str
      operator:
        description: Network Devices Query's operator.
        type: str
      value:
        description: Network Devices Query's value.
        type: str
    type: list
  page:
    description: Network Devices Query's page.
    suboptions:
      count:
        description: Network Devices Query's count.
        type: int
      limit:
        description: Network Devices Query's limit.
        type: int
      offset:
        description: Network Devices Query's offset.
        type: int
      sortBy:
        description: Network Devices Query's sortBy.
        type: str
    type: dict
  startTime:
    description: Network Devices Query's startTime.
    type: int
  views:
    description: Network Devices Query's views.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices GetsTheListOfNetworkDevicesBasedOnTheProvidedComplexFiltersAndAggregationFunctions
    description: Complete reference of the GetsTheListOfNetworkDevicesBasedOnTheProvidedComplexFiltersAndAggregationFunctions
      API.
    link: https://developer.cisco.com/docs/dna-center/#!gets-the-list-of-network-devices-based-on-the-provided-complex-filters-and-aggregation-functions
notes:
  - SDK Method used are
    devices.Devices.gets_the_list_of_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions,
  - Paths used are
    post /dna/data/api/v1/networkDevices/query,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.network_devices_query:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    aggregateAttributes:
      - function: string
        name: string
    attributes:
      - string
    endTime: 0
    filters:
      - key: string
        operator: string
        value: string
    page:
      count: 0
      limit: 0
      offset: 0
      sortBy: string
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
          "id": "string",
          "name": "string",
          "managementIpAddress": "string",
          "platformId": "string",
          "deviceFamily": "string",
          "serialNumber": "string",
          "macAddress": "string",
          "deviceSeries": "string",
          "softwareVersion": "string",
          "productVendor": "string",
          "deviceRole": "string",
          "deviceType": "string",
          "communicationState": "string",
          "reachabilityHealthStatus": "string",
          "collectionStatus": "string",
          "haStatus": "string",
          "secureMode": "string",
          "lastBootTime": 0,
          "siteHierarchyId": "string",
          "siteHierarchy": "string",
          "siteId": "string",
          "deviceGroupHierarchyId": "string",
          "tagNames": [
            "string"
          ],
          "stackType": "string",
          "osType": "string",
          "ringStatus": true,
          "maintenanceModeEnabled": true,
          "upTime": 0,
          "ipv4Address": "string",
          "ipv6Address": "string",
          "redundancyMode": "string",
          "featureFlagList": [
            "string"
          ],
          "haLastResetReason": "string",
          "redundancyPeerStateDerived": "string",
          "redundancyPeerState": "string",
          "redundancyStateDerived": "string",
          "redundancyState": "string",
          "wiredClientCount": 0,
          "wirelessClientCount": 0,
          "portCount": 0,
          "physicalPortCount": 0,
          "virtualPortCount": 0,
          "clientCount": 0,
          "apDetails": {
            "connectedWlcName": "string",
            "policyTagName": "string",
            "apOperationalState": "string",
            "powerSaveMode": "string",
            "operationalMode": "string",
            "resetReason": "string",
            "protocol": "string",
            "powerMode": "string",
            "connectedTime": 0,
            "ledFlashEnabled": true,
            "ledFlashSeconds": 0,
            "subMode": "string",
            "homeApEnabled": true,
            "powerType": "string",
            "apType": "string",
            "adminState": "string",
            "icapCapability": "string",
            "regulatoryDomain": "string",
            "ethernetMac": "string",
            "rfTagName": "string",
            "siteTagName": "string",
            "powerSaveModeCapable": "string",
            "powerProfile": "string",
            "flexGroup": "string",
            "powerCalendarProfile": "string",
            "apGroup": "string",
            "radios": [
              {
                "id": "string",
                "band": "string",
                "noise": 0,
                "airQuality": 0,
                "interference": 0,
                "trafficUtil": 0,
                "utilization": 0,
                "clientCount": 0
              }
            ]
          },
          "metricsDetails": {
            "overallHealthScore": 0,
            "cpuUtilization": 0,
            "cpuScore": 0,
            "memoryUtilization": 0,
            "memoryScore": 0,
            "avgTemperature": 0,
            "maxTemperature": 0,
            "discardScore": 0,
            "discardInterfaces": [
              "string"
            ],
            "errorScore": 0,
            "errorInterfaces": [
              "string"
            ],
            "interDeviceLinkScore": 0,
            "interDeviceConnectedDownInterfaces": [
              "string"
            ],
            "linkUtilizationScore": 0,
            "highLinkUtilizationInterfaces": [
              "string"
            ],
            "freeTimerScore": 0,
            "freeTimer": 0,
            "packetPoolScore": 0,
            "packetPool": 0,
            "freeMemoryBufferScore": 0,
            "freeMemoryBuffer": 0,
            "wqePoolScore": 0,
            "wqePool": 0,
            "apCount": 0,
            "noiseScore": 0,
            "utilizationScore": 0,
            "interferenceScore": 0,
            "airQualityScore": 0
          },
          "fabricDetails": {
            "fabricRole": [
              "string"
            ],
            "fabricSiteName": "string",
            "transitFabrics": [
              "string"
            ],
            "l2Vns": [
              "string"
            ],
            "l3Vns": [
              "string"
            ],
            "fabricSiteId": "string",
            "networkProtocol": "string"
          },
          "switchPoeDetails": {
            "portCount": 0,
            "usedPortCount": 0,
            "freePortCount": 0,
            "powerConsumed": 0,
            "poePowerConsumed": 0,
            "systemPowerConsumed": 0,
            "powerBudget": 0,
            "poePowerAllocated": 0,
            "systemPowerAllocated": 0,
            "powerRemaining": 0,
            "poeVersion": "string",
            "chassisCount": 0,
            "moduleCount": 0,
            "moduleDetails": [
              {
                "moduleId": "string",
                "chassisId": "string",
                "modulePortCount": 0,
                "moduleUsedPortCount": 0,
                "moduleFreePortCount": 0,
                "modulePowerConsumed": 0,
                "modulePoePowerConsumed": 0,
                "moduleSystemPowerConsumed": 0,
                "modulePowerBudget": 0,
                "modulePoePowerAllocated": 0,
                "moduleSystemPowerAllocated": 0,
                "modulePowerRemaining": 0,
                "interfacePowerMax": 0
              }
            ]
          },
          "fabricMetricsDetails": {
            "overallFabricScore": 0,
            "fabricTransitScore": 0,
            "fabricSiteScore": 0,
            "fabricVnScore": 0,
            "fabsiteFcpScore": 0,
            "fabsiteInfraScore": 0,
            "fabsiteFsconnScore": 0,
            "vnExitScore": 0,
            "vnFcpScore": 0,
            "vnStatusScore": 0,
            "vnServiceScore": 0,
            "transitControlPlaneScore": 0,
            "transitServicesScore": 0,
            "tcpConnScore": 0,
            "bgpBgpSiteScore": 0,
            "vniStatusScore": 0,
            "pubsubTransitConnScore": 0,
            "bgpPeerInfraVnScore": 0,
            "internetAvailScore": 0,
            "bgpEvpnScore": 0,
            "lispTransitConnScore": 0,
            "ctsEnvDataDownloadScore": 0,
            "pubsubInfraVnScore": 0,
            "peerScore": 0,
            "bgpPeerScore": 0,
            "remoteInternetAvailScore": 0,
            "bgpTcpScore": 0,
            "pubsubSessionScore": 0,
            "aaaStatusScore": 0,
            "lispCpConnScore": 0,
            "bgpPubsubSiteScore": 0,
            "mcastScore": 0,
            "portChannelScore": 0
          },
          "aggregateAttributes": [
            {
              "name": "string",
              "function": "string",
              "value": 0
            }
          ]
        }
      ],
      "page": {
        "limit": 0,
        "offset": 0,
        "count": 0,
        "sortBy": "string",
        "order": "string"
      },
      "version": "string"
    }
"""
