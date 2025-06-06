#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: site_health_v1_info
short_description: Information module for Site Health V1
description:
  - Get all Site Health V1.
  - Returns Overall Health information for all sites.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  siteType:
    description:
      - SiteType query parameter. Site type AREA or BUILDING (case insensitive).
    type: str
  offset:
    description:
      - Offset query parameter. Offset of the first returned data set entry (Multiple
        of 'limit' + 1).
    type: float
  limit:
    description:
      - Limit query parameter. Max number of data entries in the returned data set
        1,50. Default is 25.
    type: float
  timestamp:
    description:
      - Timestamp query parameter. Epoch time(in milliseconds) when the Site Hierarchy
        data is required.
    type: float
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sites GetSiteHealthV1
    description: Complete reference of the GetSiteHealthV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-site-health
notes:
  - SDK Method used are sites.Sites.get_site_health_v1,
  - Paths used are get /dna/intent/api/v1/site-health,
"""
EXAMPLES = r"""
- name: Get all Site Health V1
  cisco.catalystcenter.site_health_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    siteType: string
    offset: 0
    limit: 0
    timestamp: 0
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "siteName": "string",
        "siteId": "string",
        "parentSiteId": "string",
        "parentSiteName": "string",
        "siteType": "string",
        "latitude": 0,
        "longitude": 0,
        "healthyNetworkDevicePercentage": 0,
        "healthyClientsPercentage": 0,
        "clientHealthWired": 0,
        "clientHealthWireless": 0,
        "numberOfClients": 0,
        "numberOfNetworkDevice": 0,
        "networkHealthAverage": 0,
        "networkHealthAccess": 0,
        "networkHealthCore": 0,
        "networkHealthDistribution": 0,
        "networkHealthRouter": 0,
        "networkHealthWireless": 0,
        "networkHealthAP": 0,
        "networkHealthWLC": 0,
        "networkHealthSwitch": 0,
        "networkHealthOthers": 0,
        "numberOfWiredClients": 0,
        "numberOfWirelessClients": 0,
        "totalNumberOfConnectedWiredClients": 0,
        "totalNumberOfActiveWirelessClients": 0,
        "wiredGoodClients": 0,
        "wirelessGoodClients": 0,
        "overallGoodDevices": 0,
        "accessGoodCount": 0,
        "accessTotalCount": 0,
        "coreGoodCount": 0,
        "coreTotalCount": 0,
        "distributionGoodCount": 0,
        "distributionTotalCount": 0,
        "routerGoodCount": 0,
        "routerTotalCount": 0,
        "wirelessDeviceGoodCount": 0,
        "wirelessDeviceTotalCount": 0,
        "apDeviceGoodCount": 0,
        "apDeviceTotalCount": 0,
        "wlcDeviceGoodCount": 0,
        "wlcDeviceTotalCount": 0,
        "switchDeviceGoodCount": 0,
        "switchDeviceTotalCount": 0,
        "applicationHealth": 0,
        "applicationHealthInfo": [
          {
            "trafficClass": "string",
            "bytesCount": 0,
            "healthScore": 0
          }
        ],
        "applicationGoodCount": 0,
        "applicationTotalCount": 0,
        "applicationBytesTotalCount": 0,
        "dnacInfo": {
          "uuid": "string",
          "ip": "string",
          "status": "string"
        },
        "usage": 0,
        "applicationHealthStats": {
          "appTotalCount": 0,
          "businessRelevantAppCount": {
            "poor": 0,
            "fair": 0,
            "good": 0
          },
          "businessIrrelevantAppCount": {
            "poor": 0,
            "fair": 0,
            "good": 0
          },
          "defaultHealthAppCount": {
            "poor": 0,
            "fair": 0,
            "good": 0
          }
        }
      }
    ]
"""
