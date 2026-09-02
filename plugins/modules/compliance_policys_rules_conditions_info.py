#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_policys_rules_conditions_info
short_description: Information module for Compliance Policys Rules Conditions
description:
  - Get all Compliance Policys Rules Conditions.
  - Get Compliance Policys Rules Conditions by id.
  - Retrieves a specific condition within the specified compliance policy and rule.
  - Retrieves the list of all conditions within the specified compliance policy and rule.
version_added: '2.3.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  policyId:
    description:
      - PolicyId path parameter. The `id` of the compliance policy.
    type: str
  ruleId:
    description:
      - RuleId path parameter. The `id` of the rule within the compliance policy.
    type: str
  id:
    description:
      - Id path parameter. The `id` of the condition.
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
  - name: Cisco Catalyst Center documentation for Compliance RetrieveASpecificCondition
    description: Complete reference of the RetrieveASpecificCondition API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-a-specific-condition
  - name: Cisco Catalyst Center documentation for Compliance RetrieveTheConditions
    description: Complete reference of the RetrieveTheConditions API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-conditions
notes:
  - SDK Method used are
    compliance.Compliance.retrieve_a_specific_condition,
    compliance.Compliance.retrieve_the_conditions,
  - Paths used are
    get /dna/intent/api/v1/compliancePolicys/{policyId}/rules/{ruleId}/conditions,
    get /dna/intent/api/v1/compliancePolicys/{policyId}/rules/{ruleId}/conditions/{id},
"""

EXAMPLES = r"""
---
- name: Get all Compliance Policys Rules Conditions
  cisco.catalystcenter.compliance_policys_rules_conditions_info:
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
    policyId: c9eef5e2-1eab-426c-be77-97ee81dcba05
    ruleId: e8eef5e2-1eab-426c-be77-97ee81dcba06
  register: result
- name: Get Compliance Policys Rules Conditions by id
  cisco.catalystcenter.compliance_policys_rules_conditions_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    policyId: c9eef5e2-1eab-426c-be77-97ee81dcba05
    ruleId: e8eef5e2-1eab-426c-be77-97ee81dcba06
    id: 1d78e50b-acd7-423b-bc5e-5f4c106eaa8f
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "id": "string",
        "sequenceNumber": 0,
        "name": "string",
        "scope": "string",
        "deviceProperty": "string",
        "showCommand": "string",
        "parseAsBlocks": true,
        "blockStartExpression": "string",
        "blockEndExpression": "string",
        "blockViolationCriteria": "string",
        "operator": "string",
        "regexViolationCriteria": "string",
        "value": "string",
        "action": {
          "matchAction": "string",
          "matchViolationSeverity": {},
          "matchViolationMessageType": "string",
          "matchViolationMessage": "string",
          "doesNotMatchAction": "string",
          "doesNotMatchViolationSeverity": {},
          "doesNotMatchViolationMessageType": "string",
          "doesNotMatchViolationMessage": "string"
        }
      },
      "version": "string"
    }
"""
