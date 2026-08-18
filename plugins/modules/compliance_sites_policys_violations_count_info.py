#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_sites_policys_violations_count_info
short_description: Information module for Compliance Sites Policys Violations Count
description:
  - Get all Compliance Sites Policys Violations Count.
  - Returns the count of violations for a specific compliance policy for a site.
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
  ruleId:
    description:
      - RuleId query parameter. The `id` of the rule within the compliance policy.
    type: str
  ruleName:
    description:
      - >
        RuleName query parameter. The name of the rule that has the violation. Default behaviour is case-
        insensitive exact match. This field supports wildcard (`*`) character search. E.g. `*Vlan*`,
        `*password`, `traffic*`, `*SMU*installed`. Use the `GET
        /dna/intent/api/v1/compliancePolicys/{policyId}/rules` endpoint to retrieve the rules.
    type: str
  violationMessage:
    description:
      - >
        ViolationMessage query parameter. Message describing the violation. Default behaviour is case-
        insensitive exact match. This field supports wildcard (`*`) character search. E.g. `*Vlan*`, `*ssid`,
        `GigabitEthernet*`, `interface*has no acl*`. Use the `GET
        /dna/intent/api/v1/compliancePolicys/{policyId}/rules/{ruleId}/conditions` endpoint to retrieve the
        conditions.
    type: str
  hostname:
    description:
      - >
        Hostname query parameter. Hostname of the network device. Default behaviour is case-insensitive exact
        match. This field supports wildcard (`*`) character search. E.g. `*9800*`, `*.cisco.com`, `switch*`,
        `switch.*.lab.cisco.com`. Use the `GET /dna/intent/api/v1/network-device` endpoint to retrieve the
        network devices.
    type: str
  managementAddress:
    description:
      - >
        ManagementAddress query parameter. Management address of the network device. Default behaviour is case-
        insensitive exact match. This field supports wildcard (`*`) character search. E.g. `*10.104*`, `*.42`,
        `172.10.*`, `172.10.*.4`. Use the `GET /dna/intent/api/v1/network-device` endpoint to retrieve the
        network devices.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Compliance RetrieveTheCountOfViolationsKnowYourNetwork
    description: Complete reference of the RetrieveTheCountOfViolationsKnowYourNetwork API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-count-of-violations-know-your-network
notes:
  - SDK Method used are
    compliance.Compliance.retrieve_the_count_of_violations_know_your_network,
  - Paths used are
    get /dna/intent/api/v1/compliance/sites/{siteId}/policys/{policyId}/violations/count,
"""

EXAMPLES = r"""
---
- name: Get all Compliance Sites Policys Violations Count
  cisco.catalystcenter.compliance_sites_policys_violations_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    ruleId: e8eef5e2-1eab-426c-be77-97ee81dcba06
    ruleName: string
    violationMessage: string
    hostname: string
    managementAddress: string
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
        "count": 0
      },
      "version": "string"
    }
"""
