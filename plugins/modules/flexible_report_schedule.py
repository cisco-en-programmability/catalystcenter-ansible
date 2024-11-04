#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: flexible_report_schedule
short_description: Resource module for Flexible Report Schedule
description:
- Manage operation update of the resource Flexible Report Schedule.
- Update schedule of flexible report.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  reportId:
    description: ReportId path parameter. Id of the report.
    type: str
  schedule:
    description: Schedule information.
    type: dict
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Reports UpdateScheduleOfFlexibleReportV1
  description: Complete reference of the UpdateScheduleOfFlexibleReportV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!update-schedule-of-flexible-report-v-1
notes:
  - SDK Method used are
    reports.Reports.update_schedule_of_flexible_report_v1,

  - Paths used are
    put /dna/data/api/v1/flexible-report/schedule/{reportId},

"""

EXAMPLES = r"""
- name: Update by id
  cisco.catalystcenter.flexible_report_schedule:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    reportId: string
    schedule: {}

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "schedule": {}
    }
"""
