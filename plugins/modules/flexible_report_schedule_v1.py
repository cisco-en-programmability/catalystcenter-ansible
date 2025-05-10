#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: flexible_report_schedule_v1
short_description: Resource module for Flexible Report Schedule V1
description:
  - Manage operation update of the resource Flexible Report Schedule V1.
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
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Reports UpdateScheduleOfFlexibleReportV1
    description: Complete reference of the UpdateScheduleOfFlexibleReportV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!update-schedule-of-flexible-report
notes:
  - SDK Method used are reports.Reports.update_schedule_of_flexible_report_v1,
  - Paths used are put /dna/data/api/v1/flexible-report/schedule/{reportId},
"""
EXAMPLES = r"""
- name: Update by id
  cisco.catalystcenter.flexible_report_schedule_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    state: present
    reportId: string
    schedule: {}
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
