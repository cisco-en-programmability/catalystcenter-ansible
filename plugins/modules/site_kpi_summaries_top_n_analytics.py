#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: site_kpi_summaries_top_n_analytics
short_description: Resource module for Site Kpi Summaries Top N Analytics
description:
  - Manage operation create of the resource Site Kpi Summaries Top N Analytics.
  - Gets the Top N entites related based on site analytics for a given kpi type.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  endTime:
    description: Site Kpi Summaries Top N Analytics's endTime.
    type: int
  filters:
    description: Site Kpi Summaries Top N Analytics's filters.
    elements: dict
    suboptions:
      key:
        description: Site Kpi Summaries Top N Analytics's key.
        type: str
      operator:
        description: Site Kpi Summaries Top N Analytics's operator.
        type: str
      value:
        description: Site Kpi Summaries Top N Analytics's value.
        type: str
    type: list
  groupBy:
    description: Site Kpi Summaries Top N Analytics's groupBy.
    elements: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  startTime:
    description: Site Kpi Summaries Top N Analytics's startTime.
    type: int
  topN:
    description: Site Kpi Summaries Top N Analytics's topN.
    type: int
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Sites SubmitRequestForTopNEntitiesRelatedToSiteAnalytics
    description: Complete reference of the SubmitRequestForTopNEntitiesRelatedToSiteAnalytics API.
    link: https://developer.cisco.com/docs/dna-center/#!submit-request-for-top-n-entities-related-to-site-analytics
notes:
  - SDK Method used are
    sites.Sites.submit_request_for_top_n_entities_related_to_site_analytics,
  - Paths used are
    post /dna/data/api/v1/siteKpiSummaries/topNAnalytics,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.site_kpi_summaries_top_n_analytics:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    endTime: 0
    filters:
      - key: string
        operator: string
        value: string
    groupBy:
      - string
    headers: '{{my_headers | from_json}}'
    startTime: 0
    topN: 0
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
