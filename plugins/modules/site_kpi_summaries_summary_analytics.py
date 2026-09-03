#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: site_kpi_summaries_summary_analytics
short_description: Resource module for Site Kpi Summaries Summary Analytics
description:
  - Manage operation create of the resource Site Kpi Summaries Summary Analytics.
  - Submits the task to get summary analytics data for a given site. For detailed.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  attributes:
    description: Site Kpi Summaries Summary Analytics's attributes.
    elements: str
    type: list
  endTime:
    description: Site Kpi Summaries Summary Analytics's endTime.
    type: int
  filters:
    description: Site Kpi Summaries Summary Analytics's filters.
    elements: dict
    suboptions:
      key:
        description: Site Kpi Summaries Summary Analytics's key.
        type: str
      operator:
        description: Site Kpi Summaries Summary Analytics's operator.
        type: str
      value:
        description: Site Kpi Summaries Summary Analytics's value.
        type: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  startTime:
    description: Site Kpi Summaries Summary Analytics's startTime.
    type: int
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Sites SubmitRequestForSiteAnalyticsSummaryData
    description: Complete reference of the SubmitRequestForSiteAnalyticsSummaryData API.
    link: https://developer.cisco.com/docs/dna-center/#!submit-request-for-site-analytics-summary-data
notes:
  - SDK Method used are
    sites.Sites.submit_request_for_site_analytics_summary_data,
  - Paths used are
    post /dna/data/api/v1/siteKpiSummaries/summaryAnalytics,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.site_kpi_summaries_summary_analytics:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    attributes:
      - string
    endTime: 0
    filters:
      - key: string
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
      "response": {
        "taskLocation": "string",
        "taskId": "string"
      },
      "version": "string"
    }
"""
