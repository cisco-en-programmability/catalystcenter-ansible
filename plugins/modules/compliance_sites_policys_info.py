#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_sites_policys_info
short_description: Information module for Compliance Sites Policys
description:
  - Get all Compliance Sites Policys.
  - Get Compliance Sites Policys by id.
  - Retrieves a specific compliance policy assigned to a site.
  - Retrieves the compliance policies assigned to a site.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  siteId:
    description:
      - >
        SiteId path parameter. The `id` of the site. Use the `GET /dna/intent/api/v1/sites` endpoint to retrieve
        the sites.
    type: str
  policyId:
    description:
      - PolicyId path parameter. The `id` of the compliance policy.
    type: str
  status:
    description:
      - Status query parameter. The compliance result status of the policy.
    elements: str
    type: list
  policyName:
    description:
      - >
        PolicyName query parameter. The name of the policy. Default behaviour is case-insensitive exact match.
        This field supports wildcard (`*`) character search. E.g. `*Vlan*`, `password*policy`, `Traffic*`. Use
        the `GET /dna/intent/api/v1/compliancePolicys` endpoint to retrieve the policies.
    type: str
  sortBy:
    description:
      - SortBy query parameter. Field to sort the results by.
    type: str
  order:
    description:
      - Order query parameter. Whether ascending or descending order should be used to sort the response.
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
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Compliance RetrieveASpecificPolicyKnowYourNetwork
    description: Complete reference of the RetrieveASpecificPolicyKnowYourNetwork API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-a-specific-policy-know-your-network
  - name: Cisco Catalyst Center documentation for Compliance RetrieveThePoliciesKnowYourNetwork
    description: Complete reference of the RetrieveThePoliciesKnowYourNetwork API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-policies-know-your-network
notes:
  - SDK Method used are
    compliance.Compliance.retrieve_a_specific_policy_know_your_network,
    compliance.Compliance.retrieve_the_policies_know_your_network,
  - Paths used are
    get /dna/intent/api/v1/compliance/sites/{siteId}/policys,
    get /dna/intent/api/v1/compliance/sites/{siteId}/policys/{policyId},
"""

EXAMPLES = r"""
---
- name: Get all Compliance Sites Policys
  cisco.catalystcenter.compliance_sites_policys_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    status: []
    policyName: string
    sortBy: maxSeverity
    order: desc
    offset: 1
    limit: 0
    siteId: b8eeb5e2-1eab-426c-be77-97ee81dcba07
  register: result
- name: Get Compliance Sites Policys by id
  cisco.catalystcenter.compliance_sites_policys_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    siteId: b8eeb5e2-1eab-426c-be77-97ee81dcba07
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
      "response": {
        "policyId": "string",
        "policyName": "string",
        "policyDescription": "string",
        "maxSeverity": {},
        "violationsCount": 0,
        "errorCount": 0,
        "lastComplianceRunTime": 0,
        "status": "string",
        "networkDeviceCount": 0
      },
      "version": "string"
    }
"""
