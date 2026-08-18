#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_sites_violations
short_description: Resource module for Compliance Sites Violations
description:
  - Manage operation update of the resource Compliance Sites Violations.
  - Updates the acknowledgement status of the compliance violation for a site.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  acknowledgementStatus:
    description: Acknowledgment status of the violation(s). If any violation is acknowledged, the overall status becomes `ACKNOWLEDGED`.
    type: str
  siteId:
    description: SiteId path parameter. The `id` of the site. Use the `GET /dna/intent/api/v1/sites` endpoint to retrieve
      the sites.
    type: str
  violationId:
    description: ViolationId path parameter. The `id` of the violation.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Compliance AcknowledgeOrUnacknowledgeComplianceViolationKnowYourNetwork
    description: Complete reference of the AcknowledgeOrUnacknowledgeComplianceViolationKnowYourNetwork API.
    link: https://developer.cisco.com/docs/dna-center/#!acknowledge-or-unacknowledge-compliance-violation-know-your-network
notes:
  - SDK Method used are
    compliance.Compliance.acknowledge_or_unacknowledge_compliance_violation_know_your_network,
  - Paths used are
    put /dna/intent/api/v1/compliance/sites/{siteId}/violations/{violationId},
"""

EXAMPLES = r"""
---
- name: Update by id
  cisco.catalystcenter.compliance_sites_violations:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    acknowledgementStatus: string
    siteId: b8eeb5e2-1eab-426c-be77-97ee81dcba07
    violationId: string
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
