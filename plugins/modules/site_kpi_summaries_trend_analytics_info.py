#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: site_kpi_summaries_trend_analytics_info
short_description: Information module for Site Kpi Summaries Trend Analytics Info
description:
  - This module represents an alias of the module site_kpi_summaries_trend_analytics_v1_info
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  taskId:
    description:
      - >
        TaskId query parameter. Used to retrieve asynchronously processed & stored
        data. When this parameter is
        used, the rest of the request params will be ignored.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sites GetSiteAnalyticsTrendDataForTheGivenTaskIdV1
    description: Complete reference of the GetSiteAnalyticsTrendDataForTheGivenTaskIdV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-site-analytics-trend-data-for-the-given-task-id
notes:
  - SDK Method used are sites.Sites.get_site_analytics_trend_data_for_the_given_task_id_v1,
  - Paths used are get /dna/data/api/v1/siteKpiSummaries/trendAnalytics,
  - It should be noted that this module is an alias of site_kpi_summaries_trend_analytics_v1_info
"""
EXAMPLES = r"""
- name: Get all Site Kpi Summaries Trend Analytics Info
  cisco.catalystcenter.site_kpi_summaries_trend_analytics_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    taskId: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": [
        {
          "timestamp": 0,
          "attributes": [
            {
              "name": "string",
              "value": 0
            }
          ]
        }
      ],
      "page": {
        "limit": 0,
        "offset": 0,
        "count": 0,
        "timestampOrder": "string"
      }
    }
"""
