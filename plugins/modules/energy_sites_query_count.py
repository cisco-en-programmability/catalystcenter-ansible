#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: energy_sites_query_count
short_description: Resource module for Energy Sites Query Count
description:
  - Manage operation create of the resource Energy Sites Query Count.
  - Submits a request to retrieve the total count of sites that provide energy.
version_added: '2.2.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  aggregateAttributes:
    description: Energy Sites Query Count's aggregateAttributes.
    elements: dict
    suboptions:
      function:
        description: Energy Sites Query Count's function.
        type: str
      name:
        description: Energy Sites Query Count's name.
        type: str
    type: list
  attributes:
    description: Energy Sites Query Count's attributes.
    elements: str
    type: list
  endTime:
    description: Energy Sites Query Count's endTime.
    type: int
  filters:
    description: Energy Sites Query Count's filters.
    elements: dict
    suboptions:
      filters:
        description: Energy Sites Query Count's filters.
        elements: dict
        suboptions:
          key:
            description: Energy Sites Query Count's key.
            type: str
          operator:
            description: Energy Sites Query Count's operator.
            type: str
          value:
            description: Energy Sites Query Count's value.
            elements: str
            type: list
        type: list
      logicalOperator:
        description: Energy Sites Query Count's logicalOperator.
        type: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  page:
    description: Energy Sites Query Count's page.
    suboptions:
      limit:
        description: Energy Sites Query Count's limit.
        type: int
      offset:
        description: Energy Sites Query Count's offset.
        type: int
      sortBy:
        description: Energy Sites Query Count's sortBy.
        elements: dict
        suboptions:
          function:
            description: Energy Sites Query Count's function.
            type: str
          name:
            description: Energy Sites Query Count's name.
            type: str
          order:
            description: Energy Sites Query Count's order.
            type: str
        type: list
    type: dict
  startTime:
    description: Energy Sites Query Count's startTime.
    type: int
  taskId:
    description: TaskId query parameter. Used to retrieve asynchronously processed & stored data. When this parameter is used,
      the rest of the request params will be ignored.
    type: str
  views:
    description: Energy Sites Query Count's views.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Sites SubmitRequestToCountSitesEnergyFromQuery
    description: Complete reference of the SubmitRequestToCountSitesEnergyFromQuery API.
    link: https://developer.cisco.com/docs/dna-center/#!submit-request-to-count-sites-energy-from-query
notes:
  - SDK Method used are
    sites.Sites.submit_request_to_count_sites_energy_from_query,
  - Paths used are
    post /dna/data/api/v1/energy/sites/query/count,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.energy_sites_query_count:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    aggregateAttributes:
      - function: string
        name: string
    attributes:
      - string
    endTime: 0
    filters:
      - filters:
          - key: string
            operator: string
            value:
              - string
        logicalOperator: string
    headers: '{{my_headers | from_json}}'
    page:
      limit: 0
      offset: 0
      sortBy:
        - function: string
          name: string
          order: string
    startTime: 0
    taskId: string
    views:
      - string
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
