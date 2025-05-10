#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: issues_v1_info
short_description: Information module for Issues V1
description:
  - Get all Issues V1.
  - >
    Intent API to get a list of global issues, issues for a specific device, or issue
    for a specific client device's
    MAC address.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  startTime:
    description:
      - StartTime query parameter. Starting epoch time in milliseconds of query time
        window.
    type: float
  endTime:
    description:
      - EndTime query parameter. Ending epoch time in milliseconds of query time window.
    type: float
  siteId:
    description:
      - SiteId query parameter. Assurance UUID value of the site in the issue content.
    type: str
  deviceId:
    description:
      - DeviceId query parameter. Assurance UUID value of the device in the issue
        content.
    type: str
  macAddress:
    description:
      - MacAddress query parameter. Client's device MAC address of the issue (format
        xx xx xx xx xx xx).
    type: str
  priority:
    description:
      - >
        Priority query parameter. The issue's priority value P1, P2, P3, or P4 (case
        insensitive) (Use only when
        macAddress and deviceId are not provided).
    type: str
  issueStatus:
    description:
      - IssueStatus query parameter. The issue's status value ACTIVE, IGNORED, RESOLVED
        (case insensitive).
    type: str
  aiDriven:
    description:
      - >
        AiDriven query parameter. The issue's AI driven value YES or NO (case insensitive)
        (Use only when macAddress
        and deviceId are not provided).
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Issues IssuesV1
    description: Complete reference of the IssuesV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!issues
notes:
  - SDK Method used are issues.Issues.issues_v1,
  - Paths used are get /dna/intent/api/v1/issues,
"""
EXAMPLES = r"""
- name: Get all Issues V1
  cisco.catalystcenter.issues_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    startTime: 0
    endTime: 0
    siteId: string
    deviceId: string
    macAddress: string
    priority: string
    issueStatus: string
    aiDriven: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "totalCount": "string",
      "response": [
        {
          "issueId": "string",
          "name": "string",
          "siteId": "string",
          "deviceId": "string",
          "deviceRole": "string",
          "aiDriven": "string",
          "clientMac": "string",
          "issue_occurence_count": 0,
          "status": "string",
          "priority": "string",
          "category": "string",
          "last_occurence_time": 0
        }
      ]
    }
"""
