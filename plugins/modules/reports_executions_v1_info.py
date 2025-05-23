#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: reports_executions_v1_info
short_description: Information module for Reports Executions V1
description:
  - Get all Reports Executions V1.
  - Get Reports Executions V1 by id.
  - Get details of all executions for a given report.
  - >
    Returns report content. Save the response to a file by converting the response
    data as a blob and setting the file
    format available from content-disposition response header.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  reportId:
    description:
      - ReportId path parameter. ReportId of report.
    type: str
  executionId:
    description:
      - ExecutionId path parameter. ExecutionId of report execution.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Reports DownloadReportContentV1
    description: Complete reference of the DownloadReportContentV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!download-report-content
  - name: Cisco DNA Center documentation for Reports GetAllExecutionDetailsForAGivenReportV1
    description: Complete reference of the GetAllExecutionDetailsForAGivenReportV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-all-execution-details-for-a-given-report
notes:
  - SDK Method used are reports.Reports.download_report_content_v1, reports.Reports.get_all_execution_details_for_a_given_report_v1,
  - Paths used are get /dna/intent/api/v1/data/reports/{reportId}/executions, get
    /dna/intent/api/v1/data/reports/{reportId}/executions/{executionId},
"""
EXAMPLES = r"""
- name: Get all Reports Executions V1
  cisco.catalystcenter.reports_executions_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    reportId: string
  register: result
- name: Get Reports Executions V1 by id
  cisco.catalystcenter.reports_executions_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
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
