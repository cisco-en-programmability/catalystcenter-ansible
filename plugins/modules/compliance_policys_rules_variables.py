#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_policys_rules_variables
short_description: Resource module for Compliance Policys Rules Variables
description:
  - Manage operations create, update and delete of the resource Compliance Policys Rules Variables.
  - This API operation creates a new variable within the specified compliance policy and rule.
  - Deletes a specific variable within the specified compliance policy and rule.
  - Updates an existing compliance variable within the specified compliance policy and rule.
version_added: '2.3.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  dataType:
    description: The data type of the variable. IP mask is supported in IP address form (e.g., 255.255.255.0) only. Interface
      names must be provided in their full form, such as GigabitEthernet1/0/1.
    type: str
  defaultValue:
    description: The default value for the variable. This is applicable when `inputType` is `SINGLE_TEXT` or `MULTI_TEXT`.
      Ensure that any type of data is formatted as a string, but it must match the required format for the data type and adhere
      to any provided constraints.
    type: str
  description:
    description: A brief description of the variable.
    type: str
  id:
    description: The `id` of the variable.
    type: str
  identifier:
    description: This is the identifier of the variable. Variables are referenced using the identifier enclosed in angle brackets.
      Update operation cannot be used to change the identifier.
    type: str
  inputType:
    description: The input type of the variable. - `SINGLE_SELECT` The variable allows for the selection of a single value
      from a predefined list of options specified in the `selectionList`. It is applicable only when the `dataType` is `STRING`,
      `INTEGER`, or `BOOLEAN`. - `MULTI_SELECT` The variable permits the selection of multiple values from a predefined list
      of options specified in the `selectionList`. It is applicable only when the `dataType` is `STRING` or `INTEGER`. - `SINGLE_TEXT`
      The variable accepts a single text input from the user after policy assignment. - `MULTI_TEXT` The variable allows the
      user to enter multiple text inputs after policy assignment. It is not applicable when the `dataType` is `BOOLEAN`.
    type: str
  mandatory:
    description: Indicates if the variable is mandatory.
    type: bool
  maxLength:
    description: The maximum length constraint for the `STRING` values. This is only applicable when the `inputType` is `SINGLE_TEXT`
      or `MULTI_TEXT`.
    type: int
  maxValue:
    description: The maximum value constraint for the `INTEGER` variable. This is only applicable when the `inputType` is
      `SINGLE_TEXT` or `MULTI_TEXT`.
    type: int
  minValue:
    description: The minimum value constraint for the `INTEGER` variable. This is only applicable when the `inputType` is
      `SINGLE_TEXT` or `MULTI_TEXT`.
    type: int
  name:
    description: This is the name of the variable. It should be a concise and descriptive title that clearly identifies the
      variable. The name must be unique within the specified rule.
    type: str
  policyId:
    description: PolicyId path parameter. The `id` of the compliance policy.
    type: str
  ruleId:
    description: RuleId path parameter. The `id` of the rule within the compliance policy.
    type: str
  selectionList:
    description: A list of selection options from which to choose a value. This is applicable when the `dataType` is `STRING`,
      `INTEGER`, or `BOOLEAN`, and it is required when the `inputType` is either `SINGLE_SELECT` or `MULTI_SELECT`.
    elements: dict
    suboptions:
      default:
        description: Indicates whether this selection option is the default. Depending on the `inputType`, either only one
          or multiple selection options can be set as default.
        type: bool
      key:
        description: The key for the selection option, which uniquely identifies the value.
        type: str
      value:
        description: This is the value for the selection option. Ensure that any type of data is formatted as a string, but
          it must match the required format for the data type and adhere to any provided constraints.
        type: str
    type: list
  sequenceNumber:
    description: The sequence number of the variable that determines the display order, helping to provide values in a structured
      manner.
    type: int
  usedByConditions:
    description: An array of condition IDs that are using this variable.
    elements: str
    type: list
  validationRegex:
    description: A regular expression pattern for constraining `STRING` values. This is only applicable when the `inputType`
      is `SINGLE_TEXT` or `MULTI_TEXT`.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Compliance CreateANewVariable
    description: Complete reference of the CreateANewVariable API.
    link: https://developer.cisco.com/docs/dna-center/#!create-a-new-variable
  - name: Cisco Catalyst Center documentation for Compliance DeleteASpecificVariable
    description: Complete reference of the DeleteASpecificVariable API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-a-specific-variable
  - name: Cisco Catalyst Center documentation for Compliance UpdateAnExistingVariable
    description: Complete reference of the UpdateAnExistingVariable API.
    link: https://developer.cisco.com/docs/dna-center/#!update-an-existing-variable
notes:
  - SDK Method used are
    compliance.Compliance.create_a_new_variable,
    compliance.Compliance.delete_a_specific_variable,
    compliance.Compliance.update_an_existing_variable,
  - Paths used are
    post /dna/intent/api/v1/compliancePolicys/{policyId}/rules/{ruleId}/variables,
    delete /dna/intent/api/v1/compliancePolicys/{policyId}/rules/{ruleId}/variables/{id},
    put /dna/intent/api/v1/compliancePolicys/{policyId}/rules/{ruleId}/variables/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.compliance_policys_rules_variables:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    dataType: string
    defaultValue: string
    description: string
    id: string
    identifier: string
    inputType: string
    mandatory: true
    maxLength: 0
    maxValue: 0
    minValue: 0
    name: string
    policyId: c9eef5e2-1eab-426c-be77-97ee81dcba05
    ruleId: e8eef5e2-1eab-426c-be77-97ee81dcba06
    selectionList:
      - default: true
        key: string
        value: string
    sequenceNumber: 0
    usedByConditions:
      - string
    validationRegex: string
- name: Update by id
  cisco.catalystcenter.compliance_policys_rules_variables:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    dataType: string
    defaultValue: string
    description: string
    id: string
    inputType: string
    mandatory: true
    maxLength: 0
    maxValue: 0
    minValue: 0
    name: string
    policyId: c9eef5e2-1eab-426c-be77-97ee81dcba05
    ruleId: e8eef5e2-1eab-426c-be77-97ee81dcba06
    selectionList:
      - default: true
        key: string
        value: string
    sequenceNumber: 0
    validationRegex: string
- name: Delete by id
  cisco.catalystcenter.compliance_policys_rules_variables:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: 7aa85f96-fac2-49c0-89a5-b6c2df2bfa48
    policyId: c9eef5e2-1eab-426c-be77-97ee81dcba05
    ruleId: e8eef5e2-1eab-426c-be77-97ee81dcba06
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
