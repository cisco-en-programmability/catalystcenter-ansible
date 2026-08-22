#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_sites_violations_acknowledge_bulk_create
short_description: Resource module for Compliance Sites Violations Acknowledge Bulk Create
description:
  - Manage operation create of the resource Compliance Sites Violations Acknowledge Bulk Create.
  - Updates the acknowledgement status of compliance violations for a site.
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
  violations:
    description: List of violations with their target devices.
    elements: dict
    suboptions:
      networkDeviceIds:
        description: List of device IDs for the specific violation. If not provided or if an empty list is provided, the acknowledgement
          status will be updated for all devices at the site that have this violation.
        elements: str
        type: list
      violationId:
        description: The `id` of the violation to update.
        type: str
    type: list
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Compliance AcknowledgeOrUnacknowledgeComplianceViolations
    description: Complete reference of the AcknowledgeOrUnacknowledgeComplianceViolations API.
    link: https://developer.cisco.com/docs/dna-center/#!acknowledge-or-unacknowledge-compliance-violations
notes:
  - SDK Method used are
    compliance.Compliance.acknowledge_or_unacknowledge_compliance_violations,
  - Paths used are
    post /dna/intent/api/v1/compliance/sites/{siteId}/violations/acknowledge/bulk,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.compliance_sites_violations_acknowledge_bulk_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    acknowledgementStatus: string
    siteId: b8eeb5e2-1eab-426c-be77-97ee81dcba07
    violations:
      - networkDeviceIds:
          - string
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
