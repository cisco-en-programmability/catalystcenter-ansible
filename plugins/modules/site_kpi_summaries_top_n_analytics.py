#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: site_kpi_summaries_top_n_analytics
short_description: Resource module for Site Kpi Summaries Top N Analytics
description:
- This module represents an alias of the module site_kpi_summaries_top_n_analytics_v1
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  endTime:
    description: End Time.
    type: int
  filters:
    description: Site Kpi Summaries Top N Analytics's filters.
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
  groupBy:
    description: Group By.
    elements: str
    type: list
  startTime:
    description: Start Time.
    type: int
  topN:
    description: Top N.
    type: int
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Sites SubmitRequestForTopNEntitiesRelatedToSiteAnalyticsV1
  description: Complete reference of the SubmitRequestForTopNEntitiesRelatedToSiteAnalyticsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!submit-request-for-top-n-entities-related-to-site-analytics
notes:
  - SDK Method used are
    sites.Sites.submit_request_for_top_n_entities_related_to_site_analytics_v1,

  - Paths used are
    post /dna/data/api/v1/siteKpiSummaries/topNAnalytics,
  - It should be noted that this module is an alias of site_kpi_summaries_top_n_analytics_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.site_kpi_summaries_top_n_analytics:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    state: present
    endTime: 0
    filters:
    - key: string
      operator: string
      value: string
    groupBy:
    - string
    startTime: 0
    topN: 0

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
