#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: thousand_eyes_test_results_path_traces_info
short_description: Information module for Thousand Eyes Test Results Path Traces
description:
  - Get all Thousand Eyes Test Results Path Traces.
  - Retrieves the list of path traces for the given ThousandEyes test result.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Unique identifier of the test result.
    type: str
  clientMacAddress:
    description:
      - >
        ClientMacAddress query parameter. Optional client MAC address. If this is provided the the path trace
        would start from the given client, otherwise the path trace starts from the switch where ThousanEyes
        agent is running.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Applications RetrievesTheListOfPathTracesForTheGivenThousandEyesTestResult
    description: Complete reference of the RetrievesTheListOfPathTracesForTheGivenThousandEyesTestResult API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-path-traces-for-the-given-thousand-eyes-test-result
notes:
  - SDK Method used are
    applications.Applications.retrieves_the_list_of_path_traces_for_the_given_thousand_eyes_test_result,
  - Paths used are
    get /dna/data/api/v1/thousandEyesTestResults/{id}/pathTraces,
"""

EXAMPLES = r"""
---
- name: Get all Thousand Eyes Test Results Path Traces
  cisco.catalystcenter.thousand_eyes_test_results_path_traces_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    clientMacAddress: string
    id: string
  register: result
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
          "hops": [
            {
              "index": 0,
              "type": "string",
              "identifier": "string",
              "name": "string",
              "wlcId": "string",
              "ipAddress": "string",
              "location": "string",
              "network": "string",
              "responseTime": 0,
              "jitter": 0,
              "healthScore": 0,
              "traceTerminated": true
            }
          ]
        }
      ],
      "appLink": "string",
      "version": "string"
    }
"""
