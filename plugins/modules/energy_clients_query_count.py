#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: energy_clients_query_count
short_description: Resource module for Energy Clients Query Count
description:
  - Manage operation create of the resource Energy Clients Query Count. - > Retrieves the total count of client devices based
    on the specified complex filters. For detailed information about the usage of the API, please refer to the Open API specification
    document - https //github.com/cisco-en- programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
    deviceEnergy_1.0-1.0.1-resolved.yaml.
version_added: '2.2.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  aggregateAttributes:
    description: Energy Clients Query Count's aggregateAttributes.
    elements: dict
    suboptions:
      function:
        description: Energy Clients Query Count's function.
        type: str
      name:
        description: Energy Clients Query Count's name.
        type: str
    type: list
  attributes:
    description: Energy Clients Query Count's attributes.
    elements: str
    type: list
  endTime:
    description: Energy Clients Query Count's endTime.
    type: int
  filters:
    description: Energy Clients Query Count's filters.
    elements: dict
    suboptions:
      filters:
        description: Energy Clients Query Count's filters.
        elements: dict
        suboptions:
          key:
            description: Energy Clients Query Count's key.
            type: str
          operator:
            description: Energy Clients Query Count's operator.
            type: str
          value:
            description: Energy Clients Query Count's value.
            elements: str
            type: list
        type: list
      logicalOperator:
        description: Energy Clients Query Count's logicalOperator.
        type: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  page:
    description: Energy Clients Query Count's page.
    suboptions:
      limit:
        description: Energy Clients Query Count's limit.
        type: int
      offset:
        description: Energy Clients Query Count's offset.
        type: int
      sortBy:
        description: Energy Clients Query Count's sortBy.
        elements: dict
        suboptions:
          function:
            description: Energy Clients Query Count's function.
            type: str
          name:
            description: Energy Clients Query Count's name.
            type: str
          order:
            description: Energy Clients Query Count's order.
            type: str
        type: list
    type: dict
  startTime:
    description: Energy Clients Query Count's startTime.
    type: int
  views:
    description: Energy Clients Query Count's views.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Clients CountClientsEnergyFromQuery
    description: Complete reference of the CountClientsEnergyFromQuery API.
    link: https://developer.cisco.com/docs/dna-center/#!count-clients-energy-from-query
notes:
  - SDK Method used are
    clients.Clients.count_clients_energy_from_query,
  - Paths used are
    post /dna/data/api/v1/energy/clients/query/count,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.energy_clients_query_count:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
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
