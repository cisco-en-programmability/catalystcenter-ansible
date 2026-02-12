#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_policys_info
short_description: Information module for Compliance Policys
description:
  - Get all Compliance Policys.
  - Get Compliance Policys by id.
  - Retrieves the details of a specific compliance policy.
  - Retrieves the list of compliance policies.
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
      - PolicyId query parameter. The IDs of the compliance policies. The number of policyId(s) must not exceed 25.
    type: str
  name:
    description:
      - Name query parameter. Filter with policy name. Supports partial case-insensitive search.
    type: str
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
  limit:
    description:
      - >
        Limit query parameter. The number of records to show for this page. Default is 500 if not specified.
        Maximum allowed limit is 500.
    type: int
  id:
    description:
      - Id path parameter. The `id` of the compliance policy.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Compliance RetrieveASpecificPolicy
    description: Complete reference of the RetrieveASpecificPolicy API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-a-specific-policy
  - name: Cisco DNA Center documentation for Compliance RetrieveThePolicies
    description: Complete reference of the RetrieveThePolicies API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-policies
notes:
  - SDK Method used are
    compliance.Compliance.retrieve_a_specific_policy,
    compliance.Compliance.retrieve_the_policies,
  - Paths used are
    get /dna/intent/api/v1/compliancePolicys,
    get /dna/intent/api/v1/compliancePolicys/{id},
"""

EXAMPLES = r"""
---
- name: Get all Compliance Policys
  cisco.catalystcenter.compliance_policys_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    policyId: string
    name: string
    offset: 0
    limit: 0
  register: result
- name: Get Compliance Policys by id
  cisco.catalystcenter.compliance_policys_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "name": "string",
          "description": "string",
          "rulesCount": 0,
          "sitesCount": 0,
          "source": "string",
          "status": "string"
        }
      ],
      "version": "string"
    }
"""
