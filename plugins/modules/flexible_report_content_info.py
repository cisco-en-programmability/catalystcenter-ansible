#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: flexible_report_content_info
short_description: Information module for Flexible Report Content Info
description:
- This module represents an alias of the module flexible_report_content_v1_info
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  reportId:
    description:
    - ReportId path parameter. Id of the report.
    type: str
  executionId:
    description:
    - ExecutionId path parameter. Id of execution.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Reports DownloadFlexibleReportV1
  description: Complete reference of the DownloadFlexibleReportV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!download-flexible-report
notes:
  - SDK Method used are
    reports.Reports.download_flexible_report_v1,

  - Paths used are
    get /dna/data/api/v1/flexible-report/report/content/{reportId}/{executionId},
  - It should be noted that this module is an alias of flexible_report_content_v1_info

"""

EXAMPLES = r"""
- name: Get Flexible Report Content Info by id
  cisco.catalystcenter.flexible_report_content_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    reportId: string
    executionId: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: str
  sample: >
    "'string'"
"""
