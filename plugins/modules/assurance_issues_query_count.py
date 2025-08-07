#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: assurance_issues_query_count
short_description: Resource module for Assurance Issues
  Query Count
description:
  - Manage operation create of the resource Assurance
    Issues Query Count. - > Returns the total number
    issues for given set of filters. If there is no
    start and/or end time, then end time will be defaulted
    to current time and start time will be defaulted
    to 24-hours ago from end time. For detailed information
    about the usage of the API, please refer to the
    Open API specification document - https //github.com/cisco-en-programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
    IssuesList-1.0.0-resolved.yaml.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  endTime:
    description: End Time.
    type: int
  filters:
    description: Assurance Issues Query Count's filters.
    elements: dict
    suboptions:
      filters:
        description: Assurance Issues Query Count's
          filters.
        elements: dict
        suboptions:
          key:
            description: Key.
            type: str
          operator:
            description: Operator.
            type: str
          value:
            description: Value.
            type: str
        type: list
      key:
        description: Key.
        type: str
      logicalOperator:
        description: Logical Operator.
        type: str
      operator:
        description: Operator.
        type: str
      value:
        description: Value.
        type: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  startTime:
    description: Start Time.
    type: int
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Issues
      GetTheTotalNumberOfIssuesForGivenSetOfFilters
    description: Complete reference of the GetTheTotalNumberOfIssuesForGivenSetOfFilters
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-the-total-number-of-issues-for-given-set-of-filters
notes:
  - SDK Method used are
    issues.Issues.get_the_total_number_of_issues_for_given_set_of_filters,
  - Paths used are
    post /dna/data/api/v1/assuranceIssues/query/count,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.assurance_issues_query_count:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    endTime: 0
    filters:
      - filters:
          - key: string
            operator: string
            value: string
        key: string
        logicalOperator: string
        operator: string
        value: string
    headers: '{{my_headers | from_json}}'
    startTime: 0
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "filters": [
        {
          "key": "string",
          "value": "string",
          "operator": "string"
        }
      ]
    }
"""
