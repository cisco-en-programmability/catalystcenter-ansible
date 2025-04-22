#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: client_health_v1_info
short_description: Information module for Client Health V1
description:
  - Get all Client Health V1.
  - Returns Overall Client Health information by Client type Wired and Wireless for
    any given point of time.
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
      - Timestamp query parameter. Epoch time(in milliseconds) when the Client health
        data is required.
    type: float
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Clients GetOverallClientHealthV1
    description: Complete reference of the GetOverallClientHealthV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-overall-client-health
notes:
  - SDK Method used are clients.Clients.get_overall_client_health_v1,
  - Paths used are get /dna/intent/api/v1/client-health,
"""
EXAMPLES = r"""
- name: Get all Client Health V1
  cisco.catalystcenter.client_health_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    timestamp: 0
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
