#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: topology_network_health_info
short_description: Information module for Topology Network
  Health
description:
  - Get all Topology Network Health. - > Returns Overall
    Network Health information by Device category Access,
    Distribution, Core, Router, Wireless for any given
    point of time.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  timestamp:
    description:
      - Timestamp query parameter. UTC timestamp of
        network health data in milliseconds.
    type: float
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Topology
      GetOverallNetworkHealth
    description: Complete reference of the GetOverallNetworkHealth
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-overall-network-health
notes:
  - SDK Method used are
    topology.Topology.get_overall_network_health,
  - Paths used are
    get /dna/intent/api/v1/network-health,
"""

EXAMPLES = r"""
---
- name: Get all Topology Network Health
  cisco.catalystcenter.topology_network_health_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
    timestamp: 0
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": [
        {
          "time": "string",
          "healthScore": 0,
          "totalCount": 0,
          "goodCount": 0,
          "noHealthCount": 0,
          "unmonCount": 0,
          "fairCount": 0,
          "badCount": 0,
          "maintenanceModeCount": 0,
          "entity": "string",
          "timeinMillis": 0
        }
      ],
      "measuredBy": "string",
      "latestMeasuredByEntity": "string",
      "latestHealthScore": 0,
      "monitoredDevices": 0,
      "monitoredHealthyDevices": 0,
      "monitoredUnHealthyDevices": 0,
      "unMonitoredDevices": 0,
      "noHealthDevices": 0,
      "totalDevices": 0,
      "monitoredPoorHealthDevices": 0,
      "monitoredFairHealthDevices": 0,
      "healthContributingDevices": 0,
      "healthDistirubution": [
        {
          "category": "string",
          "totalCount": 0,
          "healthScore": 0,
          "goodPercentage": 0,
          "badPercentage": 0,
          "fairPercentage": 0,
          "noHealthPercentage": 0,
          "unmonPercentage": 0,
          "goodCount": 0,
          "badCount": 0,
          "fairCount": 0,
          "noHealthCount": 0,
          "unmonCount": 0,
          "thirdPartyDeviceCount": 0,
          "kpiMetrics": [
            {
              "key": "string",
              "value": "string"
            }
          ]
        }
      ]
    }
"""
