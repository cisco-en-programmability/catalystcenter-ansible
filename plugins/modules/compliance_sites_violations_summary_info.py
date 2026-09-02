#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_sites_violations_summary_info
short_description: Information module for Compliance Sites Violations Summary
description:
  - Get all Compliance Sites Violations Summary.
  - Retrieves the summary of compliance violations for a site.
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
  complianceTypes:
    description:
      - >
        ComplianceTypes query parameter. The types of compliance. If not specified, all applicable types will be
        considered.
    elements: str
    type: list
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
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Compliance RetrieveTheViolationsSummary
    description: Complete reference of the RetrieveTheViolationsSummary API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-violations-summary
notes:
  - SDK Method used are
    compliance.Compliance.retrieve_the_violations_summary,
  - Paths used are
    get /dna/intent/api/v1/compliance/sites/{siteId}/violationsSummary,
"""

EXAMPLES = r"""
---
- name: Get all Compliance Sites Violations Summary
  cisco.catalystcenter.compliance_sites_violations_summary_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    complianceTypes: []
    subTypes: []
    acknowledgementStatus: UNACKNOWLEDGED
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
      "response": [
        {
          "complianceType": "string",
          "violationCount": 0,
          "networkDeviceCount": 0,
          "subTypes": [
            {
              "subType": "string",
              "acknowledgementStatus": "string",
              "violationCount": 0,
              "networkDeviceCount": 0
            }
          ]
        }
      ],
      "version": "string"
    }
"""
