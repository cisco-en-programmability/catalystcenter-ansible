#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: aaa_services_query_count
short_description: Resource module for Aaa Services Query Count
description:
  - Manage operation create of the resource Aaa Services Query Count.
  - Retrieves the total number of AAA Services and offers complex filtering and.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  endTime:
    description: Aaa Services Query Count's endTime.
    type: int
  filters:
    description: Aaa Services Query Count's filters.
    elements: dict
    suboptions:
      key:
        description: Aaa Services Query Count's key.
        type: str
      operator:
        description: Aaa Services Query Count's operator.
        type: str
      value:
        description: Aaa Services Query Count's value.
        elements: str
        type: list
    type: list
  headers:
    description: Additional headers.
    type: dict
  startTime:
    description: Aaa Services Query Count's startTime.
    type: int
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices RetrievesTheTotalNumberOfAAAServicesForGivenSetOfComplexFilters
    description: Complete reference of the RetrievesTheTotalNumberOfAAAServicesForGivenSetOfComplexFilters API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-total-number-of-aaa-services-for-given-set-of-complex-filters
notes:
  - SDK Method used are
    devices.Devices.retrieves_the_total_number_of_aaa_services_for_given_set_of_complex_filters,
  - Paths used are
    post /dna/data/api/v1/aaaServices/query/count,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.aaa_services_query_count:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    endTime: 0
    filters:
      - key: string
        operator: string
        value:
          - string
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
