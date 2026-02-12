#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_policys_site_assignments
short_description: Resource module for Compliance Policys Site Assignments
description:
  - Manage operation update of the resource Compliance Policys Site Assignments. - > Use this API to assign new sites to the
    policy, update existing site allocations, or delete all site assignments by passing an empty list.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  policyId:
    description: PolicyId path parameter. The `id` of the compliance policy.
    type: str
  siteIds:
    description: An array of root site IDs linked to the policy. The `id` of the policy root site.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Compliance SetSiteAssignmentsForPolicy
    description: Complete reference of the SetSiteAssignmentsForPolicy API.
    link: https://developer.cisco.com/docs/dna-center/#!set-site-assignments-for-policy
notes:
  - SDK Method used are
    compliance.Compliance.set_site_assignments_for_policy,
  - Paths used are
    put /dna/intent/api/v1/compliancePolicys/{policyId}/siteAssignments,
"""

EXAMPLES = r"""
---
- name: Update all
  cisco.catalystcenter.compliance_policys_site_assignments:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    policyId: string
    siteIds:
      - string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
