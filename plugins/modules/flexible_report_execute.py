#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: flexible_report_execute
short_description: Resource module for Flexible Report Execute
description:
- Manage operation create of the resource Flexible Report Execute.
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
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Reports ExecutingTheFlexibleReportV1
  description: Complete reference of the ExecutingTheFlexibleReportV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!executing-the-flexible-report-v-1
notes:
  - SDK Method used are
    reports.Reports.executing_the_flexible_report_v1,

  - Paths used are
    post /dna/data/api/v1/flexible-report/report/{reportId}/execute,

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.flexible_report_execute:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    reportId: string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
