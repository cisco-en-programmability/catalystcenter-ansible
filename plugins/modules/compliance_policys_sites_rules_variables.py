#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_policys_sites_rules_variables
short_description: Resource module for Compliance Policys Sites Rules Variables
description:
  - Manage operation update of the resource Compliance Policys Sites Rules Variables.
  - Set site variable values for the specified rule within the compliance policy.
version_added: '2.3.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  inheritedSiteId:
    description: The Site Id of the site that this setting is inherited from.
    type: str
  inheritedSiteName:
    description: The name of the site that this setting is inherited from.
    type: str
  policyId:
    description: PolicyId path parameter. The `id` of the compliance policy.
    type: str
  ruleId:
    description: RuleId path parameter. The `id` of the rule within the compliance policy.
    type: str
  siteId:
    description: SiteId path parameter. The `id` of the site to which compliance policy is associated.
    type: str
  variableValues:
    description: An array of variable value assignments.
    elements: dict
    suboptions:
      id:
        description: The `id` of the variable.
        type: str
      values:
        description: List of variable values. The order of the list is preserved for compliance checks.
        elements: str
        type: list
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Compliance SetSiteVariables
    description: Complete reference of the SetSiteVariables API.
    link: https://developer.cisco.com/docs/dna-center/#!set-site-variables
notes:
  - SDK Method used are
    compliance.Compliance.set_site_variables,
  - Paths used are
    put /dna/intent/api/v1/compliancePolicys/{policyId}/sites/{siteId}/rules/{ruleId}/variables,
"""

EXAMPLES = r"""
---
- name: Update all
  cisco.catalystcenter.compliance_policys_sites_rules_variables:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    inheritedSiteId: string
    inheritedSiteName: string
    policyId: c9eef5e2-1eab-426c-be77-97ee81dcba05
    ruleId: e8eef5e2-1eab-426c-be77-97ee81dcba06
    siteId: b8eeb5e2-1eab-426c-be77-97ee81dcba07
    variableValues:
      - id: string
        values:
          - string
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
