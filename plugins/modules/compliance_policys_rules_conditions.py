#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_policys_rules_conditions
short_description: Resource module for Compliance Policys Rules Conditions
description:
  - Manage operations create, update and delete of the resource Compliance Policys Rules Conditions.
  - This API operation creates a new condition within the specified compliance policy and rule.
  - Deletes a specific condition within the specified compliance policy and rule.
  - Updates an existing compliance condition within the specified compliance policy and rule.
version_added: '2.3.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  action:
    description: Specifies actions based on condition outcomes, guiding subsequent operational steps.
    suboptions:
      doesNotMatchAction:
        description: Action to take when the condition does not match. The choice of action influences whether a violation
          is logged and whether further conditions are evaluated. Options include - `DO_NOT_RAISE_VIOLATION_AND_CONTINUE`
          No violation is raised, and processing continues. - `DO_NOT_RAISE_VIOLATION_AND_STOP` No violation is raised, and
          processing stops. - `RAISE_VIOLATION_AND_CONTINUE` A violation is raised, but processing continues. - `RAISE_VIOLATION_AND_STOP`
          A violation is raised, and processing stops. Additionally, depending on `matchAction`, value must satisfy following
          criteria - `doesNotMatchAction` cannot be same as `matchAction`. - Both `doesNotMatchAction` and `matchAction` cannot
          raise violation in a single condition.
        type: str
      doesNotMatchViolationMessage:
        description: Specify the custom violation message to be used to report violations when the condition does not match
          and raises violation. This field is applicable and required when `doesNotMatchViolationMessageType` is `CUSTOM_MESSAGE`.
          Custom variables and automatically generated regular expression group variables can both be used in this field,
          similar to how they are used in the `value` field.
        type: str
      doesNotMatchViolationMessageType:
        description: The type of message to display when the condition does not match and results in a violation. This provides
          context about the violation. This field is applicable and required when `doesNotMatchAction` is either `RAISE_VIOLATION_AND_CONTINUE`
          or ` RAISE_VIOLATION_AND_STOP`. Options include - `DEFAULT_MESSAGE` Use the automatic violation message generated
          by the system based on condition scope, operator, and value. - `CUSTOM_MESSAGE` Use the violation message specified
          by the user in `matchViolationMessage` field.
        type: str
      doesNotMatchViolationSeverity:
        description: The severity level of the violation.
        type: str
      matchAction:
        description: Action to take when the condition matches. The choice of action influences whether a violation is logged
          and whether further conditions are evaluated. Options include - `DO_NOT_RAISE_VIOLATION_AND_CONTINUE` No violation
          is raised, and processing continues. - `DO_NOT_RAISE_VIOLATION_AND_STOP` No violation is raised, and processing
          stops. - `RAISE_VIOLATION_AND_CONTINUE` A violation is raised, but processing continues. - `RAISE_VIOLATION_AND_STOP`
          A violation is raised, and processing stops.
        type: str
      matchViolationMessage:
        description: Specify the custom violation message to be used to report violations when the condition matches and raises
          violation. This field is applicable and required when `matchViolationMessageType` is `CUSTOM_MESSAGE`. Custom variables
          and automatically generated regular expression group variables can both be used in this field, similar to how they
          are used in the `value` field.
        type: str
      matchViolationMessageType:
        description: The type of message to display when the condition matches and results in a violation. This provides context
          about the violation. This field is applicable and required when `matchAction` is either `RAISE_VIOLATION_AND_CONTINUE`
          or ` RAISE_VIOLATION_AND_STOP`. Options include - `DEFAULT_MESSAGE` Use the automatic violation message generated
          by the system based on condition scope, operator, and value. - `CUSTOM_MESSAGE` Use the violation message specified
          by the user in `matchViolationMessage` field.
        type: str
      matchViolationSeverity:
        description: The severity level of the violation.
        type: str
    type: dict
  blockEndExpression:
    description: The regular expression defining the end of a block. If not specified, block parsing will continue until new
      section starts in the configuration. This is applicable only when `parseAsBlocks` is set. This is an optional field.
      The value, when provided, must be a valid regular expression.
    type: str
  blockStartExpression:
    description: The regular expression defining the start of a block. This is used to identify the beginning of relevant
      configuration sections. This is applicable and required only when `parseAsBlocks` is set. The value must be a valid
      regular expression.
    type: str
  blockViolationCriteria:
    description: Criteria determining when a violation is raised based on block evaluation results. This allows for flexible
      compliance checks depending on whether a single failure or all failures should trigger a violation. Options are - `RAISE_FOR_EACH_VIOLATION`
      Violations are raised for each block that fails the evaluation criteria. - `RAISE_SINGLE_FOR_ANY_VIOLATION` A single
      violation is raised if any one of the blocks fails the evaluation criteria. Further processing of blocks is stopped
      as soon as a violation is detected and raised. - `RAISE_IF_ALL_VIOLATED` A single violation is raised only if all the
      blocks fail the evaluation criteria.
    type: str
  deviceProperty:
    description: The specific device property to consider as source for the condition. This is applicable and required when
      scope is `DEVICE_PROPERTIES`. Possible values include - `DEVICE_NAME` Hostname of the device. - `IP_ADDRESS` IP address
      of the device. - `OS_NAME` Name of the operating system of the device. - `OS_VERSION` Version of the operating system
      running on the device.
    type: str
  id:
    description: Id path parameter. The `id` of the condition.
    type: str
  name:
    description: The auto-generated name of the condition, summarizing its scope, operator, and value.
    type: str
  operator:
    description: The operation used to evaluate the condition. String, regular expression, and expressions required for the
      operator to work are provided in `value` attribute. Options include - `CONTAINS_STRING` Checks if the specified string
      is present within the source of the condition. - `DOES_NOT_CONTAIN_STRING` Ensures the string is absent from the source
      of the condition. - `MATCHES_EXPRESSION` Evaluates whether there is a match for the regular expression within the source
      of the condition. - `DOES_NOT_MATCH_EXPRESSION` Ensures there is no match for the regular expression within the source
      of the condition. - `EVALUATE_EXPRESSION` Performs custom expression evaluation. When this is selected, the `value`
      field must contain three parts separated by a space `<left-hand-operand> <evaluate-operator> <right-hand-operand>` Available
      evaluation operators are `>`, `>=`, `<`, `<=`, `==`, and `matches`. Use `matches` to find case-sensitive exact match
      for string and IP address values. Example - To check if the custom variable `_STRING` is matching `TestString` use `<_STRING>
      matches TestString` in the `value` field. - Similarly, `<_IP_ADDR> matches 3.3.3.3` will check if the custom variable
      `_IP_ADDR` has the value `3.3.3.3`.
    type: str
  parseAsBlocks:
    description: An optional param that indicates whether to parse the configuration as discrete blocks for evaluation. Useful
      for conditions that apply to specific sections of a configuration file. This is applicable for all condition scopes
      except `DEVICE_PROPERTIES`. When scope is `PREVIOUSLY_MATCHED_BLOCKS`, this helps extract sub-blocks or portion of the
      blocks. When this is set, `blockStartExpression` must be provided. Optionally, `blockEndExpression` can be provided
      to customise blocks further.
    type: bool
  policyId:
    description: PolicyId path parameter. The `id` of the compliance policy.
    type: str
  regexViolationCriteria:
    description: Criteria determining when a violation is raised based on regular expression evaluation results. This allows
      for flexible compliance checks depending on whether a single failure or all failures should trigger a violation. Options
      are - `RAISE_FOR_EACH_VIOLATION` Violations are raised for each regular expression match instance that fails the evaluation
      criteria. - `RAISE_SINGLE_FOR_ANY_VIOLATION` A single violation is raised if any one of the regular expression match
      instances fails the evaluation criteria. Further processing of match instances is stopped as soon as a violation is
      detected and raised. - `RAISE_IF_ALL_VIOLATED` A single violation is raised only if all the regular expression match
      instances fail the evaluation criteria.
    type: str
  ruleId:
    description: RuleId path parameter. The `id` of the rule within the compliance policy.
    type: str
  scope:
    description: The source of data for the evaluation of the condition. Possible values include - `CONFIGURATION` Evaluates
      conditions against the running configuration of the device. - `DEVICE_PROPERTIES` Checks the condition based on specific
      properties of the device. Device property is specified using the `deviceProperty` attribute. - `DEVICE_COMMAND_OUTPUT`
      Evaluates based on custom command output. Custom command is specified using the `showCommand` attribute. - `PREVIOUSLY_MATCHED_BLOCKS`
      Evaluates the current condition only on passed configuration blocks from previous condition. First condition within
      the rule cannot have this as scope. The condition previous to the one being created must either have `parseAsBlocks`
      set or must use `PREVIOUSLY_MATCHED_BLOCKS` as scope.
    type: str
  sequenceNumber:
    description: The sequence number of the condition, indicating its order in the evaluation process.
    type: int
  showCommand:
    description: The command executed on the device to retrieve output for evaluation. This is applicable and required when
      the scope is `DEVICE_COMMAND_OUTPUT`.
    type: str
  value:
    description: The value or pattern used in the condition evaluation. Custom variables and automatically generated regular
      expression group variables can both be used in this field. To use variables, enclose the variable identifiers within
      `<` and `>`. During compliance check, these will be replaced with their corresponding values. If an invalid variable
      is specified, it will not be replaced and considered as a string. Example - To use custom variable with identifier _snmp_community_name,
      input `<_snmp_community_name>` in the value field. - To use the value of fourth matching group from second condition,
      input `<2.4>` in the value field. The value must satisfy the following requirements - When the `operator` is `MATCHES_EXPRESSION`
      or `DOES_NOT_MATCH_EXPRESSION`, the value must be a valid regular expression. - When the `operator` is `EVALUATE_EXPRESSION`,
      the value must contain a valid expression as mentioned in `EVALUATE_EXPRESSION` description.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Compliance CreateANewCondition
    description: Complete reference of the CreateANewCondition API.
    link: https://developer.cisco.com/docs/dna-center/#!create-a-new-condition
  - name: Cisco Catalyst Center documentation for Compliance DeleteASpecificCondition
    description: Complete reference of the DeleteASpecificCondition API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-a-specific-condition
  - name: Cisco Catalyst Center documentation for Compliance UpdateAnExistingCondition
    description: Complete reference of the UpdateAnExistingCondition API.
    link: https://developer.cisco.com/docs/dna-center/#!update-an-existing-condition
notes:
  - SDK Method used are
    compliance.Compliance.create_a_new_condition,
    compliance.Compliance.delete_a_specific_condition,
    compliance.Compliance.update_an_existing_condition,
  - Paths used are
    post /dna/intent/api/v1/compliancePolicys/{policyId}/rules/{ruleId}/conditions,
    delete /dna/intent/api/v1/compliancePolicys/{policyId}/rules/{ruleId}/conditions/{id},
    put /dna/intent/api/v1/compliancePolicys/{policyId}/rules/{ruleId}/conditions/{id},
"""

EXAMPLES = r"""
---
- name: Delete by id
  cisco.catalystcenter.compliance_policys_rules_conditions:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: 1d78e50b-acd7-423b-bc5e-5f4c106eaa8f
    policyId: c9eef5e2-1eab-426c-be77-97ee81dcba05
    ruleId: e8eef5e2-1eab-426c-be77-97ee81dcba06
- name: Update by id
  cisco.catalystcenter.compliance_policys_rules_conditions:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    action:
      doesNotMatchAction: string
      doesNotMatchViolationMessage: string
      doesNotMatchViolationMessageType: string
      doesNotMatchViolationSeverity: {}
      matchAction: string
      matchViolationMessage: string
      matchViolationMessageType: string
      matchViolationSeverity: {}
    blockEndExpression: string
    blockStartExpression: string
    blockViolationCriteria: string
    deviceProperty: string
    id: string
    name: string
    operator: string
    parseAsBlocks: true
    policyId: c9eef5e2-1eab-426c-be77-97ee81dcba05
    regexViolationCriteria: string
    ruleId: e8eef5e2-1eab-426c-be77-97ee81dcba06
    scope: string
    sequenceNumber: 0
    showCommand: string
    value: string
- name: Create
  cisco.catalystcenter.compliance_policys_rules_conditions:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    action:
      doesNotMatchAction: string
      doesNotMatchViolationMessage: string
      doesNotMatchViolationMessageType: string
      doesNotMatchViolationSeverity: {}
      matchAction: string
      matchViolationMessage: string
      matchViolationMessageType: string
      matchViolationSeverity: {}
    blockEndExpression: string
    blockStartExpression: string
    blockViolationCriteria: string
    deviceProperty: string
    id: string
    name: string
    operator: string
    parseAsBlocks: true
    policyId: c9eef5e2-1eab-426c-be77-97ee81dcba05
    regexViolationCriteria: string
    ruleId: e8eef5e2-1eab-426c-be77-97ee81dcba06
    scope: string
    sequenceNumber: 0
    showCommand: string
    value: string
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
