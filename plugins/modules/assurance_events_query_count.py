#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: assurance_events_query_count
short_description: Resource module for Assurance Events
  Query Count
description:
  - Manage operation create of the resource Assurance
    Events Query Count. - > API to fetch the count of
    assurance events for the given complex query. Please
    refer to the 'API Support Documentation' section
    to understand which fields are supported. For detailed
    information about the usage of the API, please refer
    to the Open API specification document - https //github.com/cisco-en-
    programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
    AssuranceEvents-1.0.0-resolved.yaml.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  deviceFamily:
    description: Device Family.
    elements: str
    type: list
  endTime:
    description: End Time.
    type: int
  filters:
    description: Assurance Events Query Count's filters.
    elements: dict
    suboptions:
      key:
        description: Key.
        type: str
      operator:
        description: Operator.
        type: str
      value:
        description: Value.
        type: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  startTime:
    description: Start Time.
    type: int
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices
      CountTheNumberOfEventsWithFilters
    description: Complete reference of the CountTheNumberOfEventsWithFilters
      API.
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
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
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
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
