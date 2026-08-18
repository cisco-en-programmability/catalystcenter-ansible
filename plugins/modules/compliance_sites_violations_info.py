#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_sites_violations_info
short_description: Information module for Compliance Sites Violations
description:
  - Get all Compliance Sites Violations.
  - Get Compliance Sites Violations by id.
  - Retrieves details of a specific compliance violation for a site.
  - Retrieves the compliance violations for a site with filtering, sorting, and searching capabilities.
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
  violationId:
    description:
      - ViolationId path parameter. The `id` of the violation.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Compliance RetrieveASpecificViolation
    description: Complete reference of the RetrieveASpecificViolation API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-a-specific-violation
  - name: Cisco Catalyst Center documentation for Compliance RetrieveTheComplianceViolations
    description: Complete reference of the RetrieveTheComplianceViolations API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-compliance-violations
notes:
  - SDK Method used are
    compliance.Compliance.retrieve_a_specific_violation,
    compliance.Compliance.retrieve_the_compliance_violations,
  - Paths used are
    get /dna/intent/api/v1/compliance/sites/{siteId}/violations,
    get /dna/intent/api/v1/compliance/sites/{siteId}/violations/{violationId},
"""

EXAMPLES = r"""
---
- name: Get all Compliance Sites Violations
  cisco.catalystcenter.compliance_sites_violations_info:
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
    sortBy: severity
    order: desc
    offset: 1
    limit: 0
    siteId: b8eeb5e2-1eab-426c-be77-97ee81dcba07
  register: result
- name: Get Compliance Sites Violations by id
  cisco.catalystcenter.compliance_sites_violations_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    siteId: b8eeb5e2-1eab-426c-be77-97ee81dcba07
    violationId: string
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
        "ruleId": "string",
        "ruleName": "string",
        "conditionId": "string",
        "sequenceNumber": 0,
        "violationMessage": "string",
        "templateName": "string",
        "templateId": "string",
        "operation": "string",
        "feature": "string",
        "parameter": "string",
        "intendedValue": "string",
        "actualValue": "string"
      },
      "version": "string"
    }
"""
