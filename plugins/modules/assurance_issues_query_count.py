#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: assurance_issues_query_count
short_description: Resource module for Assurance Issues Query Count
description:
  - Manage operation create of the resource Assurance Issues Query Count.
  - Returns the total number issues for given set of filters. If there is no start.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  endTime:
    description: Assurance Issues Query Count's endTime.
    type: int
  filters:
    description: Assurance Issues Query Count's filters.
    elements: dict
    suboptions:
      filters:
        description: Assurance Issues Query Count's filters.
        elements: dict
        suboptions:
          key:
            description: Assurance Issues Query Count's key.
            type: str
          operator:
            description: Assurance Issues Query Count's operator.
            type: str
          value:
            description: Assurance Issues Query Count's value.
            type: str
        type: list
      key:
        description: Assurance Issues Query Count's key.
        type: str
      logicalOperator:
        description: Assurance Issues Query Count's logicalOperator.
        type: str
      operator:
        description: Assurance Issues Query Count's operator.
        type: str
      value:
        description: Assurance Issues Query Count's value.
        type: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  startTime:
    description: Assurance Issues Query Count's startTime.
    type: int
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Issues GetTheTotalNumberOfIssuesForGivenSetOfFilters
    description: Complete reference of the GetTheTotalNumberOfIssuesForGivenSetOfFilters API.
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
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
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
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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
