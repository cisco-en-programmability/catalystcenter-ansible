#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: dns_services_query_count
short_description: Resource module for Dns Services Query Count
description:
  - Manage operation create of the resource Dns Services Query Count.
  - Retrieves the total number of DNS Services and offers complex filtering and.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  endTime:
    description: Dns Services Query Count's endTime.
    type: int
  filters:
    description: Dns Services Query Count's filters.
    elements: dict
    suboptions:
      key:
        description: Dns Services Query Count's key.
        type: str
      operator:
        description: Dns Services Query Count's operator.
        type: str
      value:
        description: Dns Services Query Count's value.
        elements: str
        type: list
    type: list
  headers:
    description: Additional headers.
    type: dict
  startTime:
    description: Dns Services Query Count's startTime.
    type: int
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices RetrievesTheTotalNumberOfDNSServicesForGivenSetOfComplexFilters
    description: Complete reference of the RetrievesTheTotalNumberOfDNSServicesForGivenSetOfComplexFilters API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-total-number-of-dns-services-for-given-set-of-complex-filters
notes:
  - SDK Method used are
    devices.Devices.retrieves_the_total_number_of_dns_services_for_given_set_of_complex_filters,
  - Paths used are
    post /dna/data/api/v1/dnsServices/query/count,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.dns_services_query_count:
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
