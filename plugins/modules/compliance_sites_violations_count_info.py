#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_sites_violations_count_info
short_description: Information module for Compliance Sites Violations Count
description:
  - Get all Compliance Sites Violations Count.
  - Returns the total count of compliance violations for a site based on the specified filters.
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
  complianceType:
    description:
      - ComplianceType query parameter. The type of compliance.
    type: str
  subTypes:
    description:
      - >
        SubTypes query parameter. Specify the compliance sub-types. If not specified, all applicable sub-types
        will be considered.
    elements: str
    type: list
  acknowledgementStatus:
    description:
      - >
        AcknowledgementStatus query parameter. The acknowledgement status of the violation. If not specified,
        all violations will be considered regardless of their acknowledgement status.
    type: str
  feature:
    description:
      - >
        Feature query parameter. The feature that has the violation. Default behaviour is case-insensitive exact
        match. This field supports wildcard (`*`) character search. E.g. `*Wlan*`, `*SSID`, `Wireless*Config`,
        `*/Guest-SSID`.
    type: str
  parameter:
    description:
      - >
        Parameter query parameter. The parameter name that has the violation. Default behaviour is case-
        insensitive exact match. This field supports wildcard (`*`) character search. E.g. `*interface*`,
        `*ssid`, `server*`, `admin*status`.
    type: str
  operation:
    description:
      - Operation query parameter. Represents the type of configuration operation performed.
    type: str
  templateName:
    description:
      - >
        TemplateName query parameter. The name of the CLI template that has the violation. Default behaviour is
        case-insensitive exact match. This field supports wildcard (`*`) character search. E.g. `*Vlan*`,
        `*route`, `ACL*`, `interface*template`. Use the `GET /dna/intent/api/v2/template-programmer/template`
        endpoint to retrieve the templates.
    type: str
  policyName:
    description:
      - >
        PolicyName query parameter. The name of the policy. Default behaviour is case-insensitive exact match.
        This field supports wildcard (`*`) character search. E.g. `*Vlan*`, `password*policy`, `Traffic*`. Use
        the `GET /dna/intent/api/v1/compliancePolicys` endpoint to retrieve the policies.
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
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Compliance RetrieveTheCountOfViolations
    description: Complete reference of the RetrieveTheCountOfViolations API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-count-of-violations
notes:
  - SDK Method used are
    compliance.Compliance.retrieve_the_count_of_violations,
  - Paths used are
    get /dna/intent/api/v1/compliance/sites/{siteId}/violations/count,
"""

EXAMPLES = r"""
---
- name: Get all Compliance Sites Violations Count
  cisco.catalystcenter.compliance_sites_violations_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    complianceType: NETWORK_SETTINGS
    subTypes: []
    acknowledgementStatus: UNACKNOWLEDGED
    feature: string
    parameter: string
    operation: CHANGED
    templateName: string
    policyName: string
    ruleName: string
    violationMessage: string
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
