#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: issue_enrichment_details_v3_info
short_description: Information module for Issue Enrichment Details V3
description:
  - Get all Issue Enrichment Details V3. - > Enriches a given network issue context an issue id or end user's Mac Address
    with details about the issues, impacted hosts and suggested actions for remediation.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Issues IssueEnrichmentDetails
    description: Complete reference of the IssueEnrichmentDetails API.
    link: https://developer.cisco.com/docs/dna-center/#!issue-enrichment-details
notes:
  - SDK Method used are
    issues.Issues.issue_enrichment_details,
  - Paths used are
    get /dna/intent/api/v1/issueEnrichmentDetails,
"""

EXAMPLES = r"""
---
- name: Get all Issue Enrichment Details V3
  cisco.catalystcenter.issue_enrichment_details_v3_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
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
          "issueDetails": {
            "issues": [
              {
                "id": "string",
                "issueSource": "string",
                "issueCategory": "string",
                "issueName": "string",
                "issueDescription": "string",
                "issueEntity": "string",
                "issueEntityValue": "string",
                "issueSeverity": "string",
                "issuePriority": "string",
                "issueSummary": "string",
                "createdTimestamp": 0,
                "suggestedActions": [
                  {
                    "message": "string",
                    "steps": [
                      {}
                    ]
                  }
                ],
                "impactedHosts": [
                  {
                    "hostType": "string",
                    "hostName": "string",
                    "hostOs": "string",
                    "ssId": "string",
                    "connectedInterface": "string",
                    "macAddress": "string",
                    "failedAttempts": 0,
                    "location": {
                      "siteId": "string",
                      "siteType": "string",
                      "area": "string",
                      "building": "string",
                      "floor": "string"
                    },
                    "createdTimestamp": 0
                  }
                ],
                "deviceId": "string",
                "issueStatus": "string"
              }
            ]
          }
        }
      ],
      "version": "string"
    }
"""
