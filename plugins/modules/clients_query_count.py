#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: clients_query_count
short_description: Resource module for Clients Query Count
description:
  - Manage operation create of the resource Clients Query Count.
  - Retrieves the number of clients by applying complex filters. For detailed.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  endTime:
    description: Clients Query Count's endTime.
    type: int
  filters:
    description: Clients Query Count's filters.
    elements: dict
    suboptions:
      key:
        description: Clients Query Count's key.
        type: str
      operator:
        description: Clients Query Count's operator.
        type: str
      value:
        description: Clients Query Count's value.
        type: int
    type: list
  headers:
    description: Additional headers.
    type: dict
  startTime:
    description: Clients Query Count's startTime.
    type: int
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Clients RetrievesTheNumberOfClientsByApplyingComplexFilters
    description: Complete reference of the RetrievesTheNumberOfClientsByApplyingComplexFilters API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-number-of-clients-by-applying-complex-filters
notes:
  - SDK Method used are
    clients.Clients.retrieves_the_number_of_clients_by_applying_complex_filters,
  - Paths used are
    post /dna/data/api/v1/clients/query/count,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.clients_query_count:
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
        value: 0
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
