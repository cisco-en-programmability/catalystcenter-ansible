#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: client_health_info
short_description: Information module for Client Health
description:
  - Get all Client Health.
  - Returns Overall Client Health information by Client
    type Wired and Wireless for any given point of time.
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
      - Timestamp query parameter. Epoch time(in milliseconds)
        when the Client health data is required.
    type: float
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Clients
      GetOverallClientHealth
    description: Complete reference of the GetOverallClientHealth
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-overall-client-health
notes:
  - SDK Method used are
    clients.Clients.get_overall_client_health,
  - Paths used are
    get /dna/intent/api/v1/client-health,
"""

EXAMPLES = r"""
---
- name: Get all Client Health
  cisco.catalystcenter.client_health_info:
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
          "siteId": "string",
          "scoreDetail": [
            {
              "scoreCategory": {
                "scoreCategory": "string",
                "value": "string"
              },
              "scoreValue": 0,
              "clientCount": 0,
              "clientUniqueCount": 0,
              "maintenanceAffectedClientCount": 0,
              "randomMacCount": 0,
              "duidCount": 0,
              "starttime": 0,
              "endtime": 0,
              "connectedToUdnCount": 0,
              "unconnectedToUdnCount": 0,
              "scoreList": [
                {
                  "scoreCategory": {
                    "scoreCategory": "string",
                    "value": "string"
                  },
                  "scoreValue": 0,
                  "clientCount": 0,
                  "clientUniqueCount": 0,
                  "maintenanceAffectedClientCount": 0,
                  "randomMacCount": 0,
                  "duidCount": 0,
                  "starttime": 0,
                  "endtime": 0,
                  "connectedToUdnCount": 0,
                  "unconnectedToUdnCount": 0
                }
              ]
            }
          ]
        }
      ]
    }
"""
