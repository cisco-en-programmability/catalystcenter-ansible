#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_sites_policys_count_info
short_description: Information module for Compliance Sites Policys Count
description:
  - Get all Compliance Sites Policys Count.
  - Returns the count of compliance policies assigned to a site.
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
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Compliance RetrieveTheCountOfPoliciesKnowYourNetwork
    description: Complete reference of the RetrieveTheCountOfPoliciesKnowYourNetwork API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-count-of-policies-know-your-network
notes:
  - SDK Method used are
    compliance.Compliance.retrieve_the_count_of_policies_know_your_network,
  - Paths used are
    get /dna/intent/api/v1/compliance/sites/{siteId}/policys/count,
"""

EXAMPLES = r"""
---
- name: Get all Compliance Sites Policys Count
  cisco.catalystcenter.compliance_sites_policys_count_info:
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
    siteId: b8eeb5e2-1eab-426c-be77-97ee81dcba07
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
