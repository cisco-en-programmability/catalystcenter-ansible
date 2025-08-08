#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: flexible_report_schedule
short_description: Resource module for Flexible Report
  Schedule
description:
  - Manage operation update of the resource Flexible
    Report Schedule.
  - Update schedule of flexible report.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  reportId:
    description: ReportId path parameter. Id of the
      report.
    type: str
  schedule:
    description: Schedule information.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Reports
      UpdateScheduleOfFlexibleReport
    description: Complete reference of the UpdateScheduleOfFlexibleReport
      API.
    link: https://developer.cisco.com/docs/dna-center/#!update-schedule-of-flexible-report
notes:
  - SDK Method used are
    reports.Reports.update_schedule_of_flexible_report,
  - Paths used are
    put /dna/data/api/v1/flexible-report/schedule/{reportId},
"""

EXAMPLES = r"""
---
- name: Update by id
  cisco.catalystcenter.flexible_report_schedule:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    state: present
    reportId: string
    schedule: {}
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "schedule": {}
    }
"""
