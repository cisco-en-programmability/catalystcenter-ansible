#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: flexible_report_schedule_v1_info
short_description: Information module for Flexible Report Schedule V1
description:
- Get Flexible Report Schedule V1 by id.
- Get flexible report schedule by report id.
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
requirements:
- catalystcentersdk >= 2.3.7.6
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Reports GetFlexibleReportScheduleByReportIdV1
  description: Complete reference of the GetFlexibleReportScheduleByReportIdV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-flexible-report-schedule-by-report-id
notes:
  - SDK Method used are
    reports.Reports.get_flexible_report_schedule_by_report_id_v1,

  - Paths used are
    get /dna/data/api/v1/flexible-report/schedule/{reportId},

"""

EXAMPLES = r"""
- name: Get Flexible Report Schedule V1 by id
  cisco.catalystcenter.flexible_report_schedule_v1_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    reportId: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "schedule": {}
    }
"""
