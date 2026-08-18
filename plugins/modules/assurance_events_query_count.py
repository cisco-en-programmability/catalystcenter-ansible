#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: assurance_events_query_count
short_description: Resource module for Assurance Events Query Count
description:
  - Manage operation create of the resource Assurance Events Query Count.
  - API to fetch the count of assurance events for the given complex query. Please.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  deviceFamily:
    description: Assurance Events Query Count's deviceFamily.
    elements: str
    type: list
  endTime:
    description: Assurance Events Query Count's endTime.
    type: int
  filters:
    description: Assurance Events Query Count's filters.
    elements: dict
    suboptions:
      key:
        description: Assurance Events Query Count's key.
        type: str
      operator:
        description: Assurance Events Query Count's operator.
        type: str
      value:
        description: Assurance Events Query Count's value.
        type: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  startTime:
    description: Assurance Events Query Count's startTime.
    type: int
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices CountTheNumberOfEventsWithFilters
    description: Complete reference of the CountTheNumberOfEventsWithFilters API.
    link: https://developer.cisco.com/docs/dna-center/#!count-the-number-of-events-with-filters
notes:
  - SDK Method used are
    devices.Devices.count_the_number_of_events_with_filters,
  - Paths used are
    post /dna/data/api/v1/assuranceEvents/query/count,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.assurance_events_query_count:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    deviceFamily:
      - string
    endTime: 0
    filters:
      - key: string
        operator: string
        value: string
    headers: '{{my_headers | from_json}}'
    startTime: 0
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "count": 0
      },
      "version": "string"
    }
"""
