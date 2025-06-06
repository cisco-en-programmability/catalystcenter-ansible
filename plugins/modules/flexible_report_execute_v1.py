#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: flexible_report_execute_v1
short_description: Resource module for Flexible Report Execute V1
description:
  - Manage operation create of the resource Flexible Report Execute V1.
  - This API is used for executing the report.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  reportId:
    description: ReportId path parameter. Id of the Report.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Reports ExecutingTheFlexibleReportV1
    description: Complete reference of the ExecutingTheFlexibleReportV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!executing-the-flexible-report
notes:
  - SDK Method used are reports.Reports.executing_the_flexible_report_v1,
  - Paths used are post /dna/data/api/v1/flexible-report/report/{reportId}/execute,
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.flexible_report_execute_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    reportId: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "startTime": 0,
      "endTime": 0,
      "requestStatus": "string",
      "errors": [
        "string"
      ],
      "warnings": [
        {}
      ]
    }
"""
