#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: assurance_get_sensor_test_results_info
short_description: Information module for Assurance Get Sensor Test Results Info
description:
  - This module represents an alias of the module assurance_get_sensor_test_results_v1_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  siteId:
    description:
      - SiteId query parameter. Assurance site UUID.
    type: str
  startTime:
    description:
      - StartTime query parameter. The epoch time in milliseconds.
    type: float
  endTime:
    description:
      - EndTime query parameter. The epoch time in milliseconds.
    type: float
  testFailureBy:
    description:
      - >
        TestFailureBy query parameter. Obtain failure statistics group by "area",
        "building", or "floor" (case
        insensitive).
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless SensorTestResultsV1
    description: Complete reference of the SensorTestResultsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!sensor-test-results
notes:
  - SDK Method used are wireless.Wireless.sensor_test_results_v1,
  - Paths used are get /dna/intent/api/v1/AssuranceGetSensorTestResults,
  - It should be noted that this module is an alias of assurance_get_sensor_test_results_v1_info
"""
EXAMPLES = r"""
- name: Get all Assurance Get Sensor Test Results Info
  cisco.catalystcenter.assurance_get_sensor_test_results_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    siteId: string
    startTime: 0
    endTime: 0
    testFailureBy: string
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
      "response": {
        "summary": {
          "totalTestCount": 0,
          "ONBOARDING": {
            "AUTH": {
              "passCount": 0,
              "failCount": 0
            },
            "DHCP": {
              "passCount": 0,
              "failCount": 0
            },
            "ASSOC": {
              "passCount": 0,
              "failCount": 0
            }
          },
          "PERFORMANCE": {
            "IPSLASENDER": {
              "passCount": 0,
              "failCount": 0
            }
          },
          "NETWORK_SERVICES": {
            "DNS": {
              "passCount": 0,
              "failCount": 0
            }
          },
          "APP_CONNECTIVITY": {
            "HOST_REACHABILITY": {
              "passCount": 0,
              "failCount": 0
            },
            "WEBSERVER": {
              "passCount": 0,
              "failCount": 0
            },
            "FILETRANSFER": {
              "passCount": 0,
              "failCount": 0
            }
          },
          "RF_ASSESSMENT": {
            "DATA_RATE": {
              "passCount": 0,
              "failCount": 0
            },
            "SNR": {
              "passCount": 0,
              "failCount": 0
            }
          },
          "EMAIL": {
            "MAILSERVER": {
              "passCount": 0,
              "failCount": 0
            }
          }
        },
        "failureStats": [
          {
            "errorCode": 0,
            "errorTitle": "string",
            "testType": "string",
            "testCategory": "string"
          }
        ]
      }
    }
"""
