#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: issues_enrichment_details_info
short_description: Information module for Issues Enrichment
  Details
description:
  - Get all Issues Enrichment Details. - > Enriches
    a given network issue context an issue id or end
    user's Mac Address with details about the issues,
    impacted hosts and suggested actions for remediation.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Issues
      GetIssueEnrichmentDetails
    description: Complete reference of the GetIssueEnrichmentDetails
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-issue-enrichment-details
notes:
  - SDK Method used are
    issues.Issues.get_issue_enrichment_details,
  - Paths used are
    get /dna/intent/api/v1/issue-enrichment-details,
"""

EXAMPLES = r"""
---
- name: Get all Issues Enrichment Details
  cisco.catalystcenter.issues_enrichment_details_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "issue": [
        {
          "issueId": "string",
          "issueSource": "string",
          "issueCategory": "string",
          "issueName": "string",
          "issueDescription": "string",
          "issueEntity": "string",
          "issueEntityValue": "string",
          "issueSeverity": "string",
          "issuePriority": "string",
          "issueSummary": "string",
          "issueTimestamp": 0,
          "suggestedActions": [
            {
              "message": "string",
              "steps": [
                {}
              ]
            }
          ],
          "impactedHosts": [
            {}
          ]
        }
      ]
    }
"""
