#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: flexible_report_content_info
short_description: Information module for Flexible Report Content
description:
  - Get Flexible Report Content by id. - > This is used to download the flexible report. The API returns report content. Save
    the response to a file by converting the response data as a blob and setting the file format available from content-disposition
    response header.
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
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Reports DownloadFlexibleReport
    description: Complete reference of the DownloadFlexibleReport API.
    link: https://developer.cisco.com/docs/dna-center/#!download-flexible-report
notes:
  - SDK Method used are
    reports.Reports.download_flexible_report,
  - Paths used are
    get /dna/data/api/v1/flexible-report/report/content/{reportId}/{executionId},
"""

EXAMPLES = r"""
---
- name: Get Flexible Report Content by id
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
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: str
  sample: >
    "'string'"
"""
