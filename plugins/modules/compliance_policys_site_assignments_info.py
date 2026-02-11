#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_policys_site_assignments_info
short_description: Information module for Compliance Policys Site Assignments
description:
  - Get all Compliance Policys Site Assignments.
  - Retrieve the list of site IDs to which the compliance policy is assigned.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  policyId:
    description:
      - PolicyId path parameter. The `id` of the compliance policy.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Compliance RetrieveSiteAssignmentsForPolicy
    description: Complete reference of the RetrieveSiteAssignmentsForPolicy API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-site-assignments-for-policy
notes:
  - SDK Method used are
    compliance.Compliance.retrieve_site_assignments_for_policy,
  - Paths used are
    get /dna/intent/api/v1/compliancePolicys/{policyId}/siteAssignments,
"""

EXAMPLES = r"""
---
- name: Get all Compliance Policys Site Assignments
  cisco.catalystcenter.compliance_policys_site_assignments_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    policyId: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "siteIds": [
          "string"
        ]
      },
      "version": "string"
    }
"""
