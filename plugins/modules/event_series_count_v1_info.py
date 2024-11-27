#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_series_count_v1_info
short_description: Information module for Event Series Count V1
description:
- Get all Event Series Count V1.
- Get the Count of Published Notifications.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  eventIds:
    description:
    - EventIds query parameter. The registered EventId should be provided.
    type: str
  startTime:
    description:
    - StartTime query parameter. Start Time in milliseconds.
    type: float
  endTime:
    description:
    - EndTime query parameter. End Time in milliseconds.
    type: float
  category:
    description:
    - Category query parameter.
    type: str
  type:
    description:
    - Type query parameter.
    type: str
  severity:
    description:
    - Severity query parameter.
    type: str
  domain:
    description:
    - Domain query parameter.
    type: str
  subDomain:
    description:
    - SubDomain query parameter. Sub Domain.
    type: str
  source:
    description:
    - Source query parameter.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Event Management CountOfNotificationsV1
  description: Complete reference of the CountOfNotificationsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!count-of-notifications
notes:
  - SDK Method used are
    event_management.EventManagement.count_of_notifications_v1,

  - Paths used are
    get /dna/intent/api/v1/event/event-series/count,

"""

EXAMPLES = r"""
- name: Get all Event Series Count V1
  cisco.catalystcenter.event_series_count_v1_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    eventIds: string
    startTime: 0
    endTime: 0
    category: string
    type: string
    severity: string
    domain: string
    subDomain: string
    source: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: str
  sample: >
    "string"
"""
