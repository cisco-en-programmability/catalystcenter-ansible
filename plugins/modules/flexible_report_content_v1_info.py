#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: flexible_report_content_v1_info
short_description: Information module for Flexible Report Content V1
description:
- Get Flexible Report Content V1 by id.
- >
   This is used to download the flexible report. The API returns report content. Save the response to a file by
   converting the response data as a blob and setting the file format available from content-disposition response
   header.
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

"""

EXAMPLES = r"""
- name: Get Flexible Report Content V1 by id
  cisco.catalystcenter.flexible_report_content_v1_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
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
