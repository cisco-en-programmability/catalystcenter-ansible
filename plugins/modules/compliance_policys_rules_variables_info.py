#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_policys_rules_variables_info
short_description: Information module for Compliance Policys Rules Variables
description:
  - Get all Compliance Policys Rules Variables.
  - Get Compliance Policys Rules Variables by id.
  - Retrieves a specific variable within the specified compliance policy and rule.
  - Retrieves the list of all variables within the specified compliance policy and rule.
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
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: int
  id:
    description:
      - Id path parameter. The `id` of the variable.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Compliance RetrieveASpecificVariable
    description: Complete reference of the RetrieveASpecificVariable API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-a-specific-variable
  - name: Cisco Catalyst Center documentation for Compliance RetrieveTheVariables
    description: Complete reference of the RetrieveTheVariables API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-variables
notes:
  - SDK Method used are
    compliance.Compliance.retrieve_a_specific_variable,
    compliance.Compliance.retrieve_the_variables,
  - Paths used are
    get /dna/intent/api/v1/compliancePolicys/{policyId}/rules/{ruleId}/variables,
    get /dna/intent/api/v1/compliancePolicys/{policyId}/rules/{ruleId}/variables/{id},
"""

EXAMPLES = r"""
---
- name: Get all Compliance Policys Rules Variables
  cisco.catalystcenter.compliance_policys_rules_variables_info:
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
- name: Get Compliance Policys Rules Variables by id
  cisco.catalystcenter.compliance_policys_rules_variables_info:
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
    id: 7aa85f96-fac2-49c0-89a5-b6c2df2bfa48
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {},
      "version": "string"
    }
"""
