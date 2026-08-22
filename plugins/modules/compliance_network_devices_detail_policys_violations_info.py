#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_network_devices_detail_policys_violations_info
short_description: Information module for Compliance Network Devices Detail Policys Violations
description:
  - Get all Compliance Network Devices Detail Policys Violations.
  - Retrieve the violation details of the compliance policy for the network device.
version_added: '2.3.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  networkDeviceId:
    description:
      - NetworkDeviceId path parameter. The `id` of the network device.
    type: str
  policyId:
    description:
      - PolicyId path parameter. The `id` of the compliance policy.
    type: str
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: int
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Compliance RetrieveThePolicyViolations
    description: Complete reference of the RetrieveThePolicyViolations API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-policy-violations
notes:
  - SDK Method used are
    compliance.Compliance.retrieve_the_policy_violations,
  - Paths used are
    get /dna/intent/api/v1/compliance/networkDevices/{networkDeviceId}/detail/policys/{policyId}/violations,
"""

EXAMPLES = r"""
---
- name: Get all Compliance Network Devices Detail Policys Violations
  cisco.catalystcenter.compliance_network_devices_detail_policys_violations_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    offset: 1
    limit: 0
    networkDeviceId: 0003e9dc-4eaf-41bc-a0e4-bcaaf78e6302
    policyId: c9eef5e2-1eab-426c-be77-97ee81dcba05
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
          "ruleId": "string",
          "ruleName": "string",
          "ruleDescription": "string",
          "ruleSuggestedFix": "string",
          "violations": [
            {
              "sequenceNumber": 0,
              "conditionId": "string",
              "violationMessage": "string",
              "severity": "string"
            }
          ],
          "errors": [
            {
              "sequenceNumber": 0,
              "conditionId": "string",
              "errorCode": "string",
              "errorMessage": "string"
            }
          ],
          "maxSeverity": {},
          "errorCount": 0
        }
      ],
      "version": "string"
    }
"""
