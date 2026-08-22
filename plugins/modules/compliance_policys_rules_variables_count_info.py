#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_policys_rules_variables_count_info
short_description: Information module for Compliance Policys Rules Variables Count
description:
  - Get all Compliance Policys Rules Variables Count.
  - Retrieves the count of variables under the specified compliance policy and rule.
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
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Compliance RetrieveTheCountOfVariables
    description: Complete reference of the RetrieveTheCountOfVariables API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-count-of-variables
notes:
  - SDK Method used are
    compliance.Compliance.retrieve_the_count_of_variables,
  - Paths used are
    get /dna/intent/api/v1/compliancePolicys/{policyId}/rules/{ruleId}/variables/count,
"""

EXAMPLES = r"""
---
- name: Get all Compliance Policys Rules Variables Count
  cisco.catalystcenter.compliance_policys_rules_variables_count_info:
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
        "count": 0
      },
      "version": "string"
    }
"""
