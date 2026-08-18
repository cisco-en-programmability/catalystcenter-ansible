#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: energy_clients_query
short_description: Resource module for Energy Clients Query
description:
  - Manage operation create of the resource Energy Clients Query.
  - Retrieves a list of client devices along with their energy data for a.
version_added: '2.2.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  aggregateAttributes:
    description: Energy Clients Query's aggregateAttributes.
    elements: dict
    suboptions:
      function:
        description: Energy Clients Query's function.
        type: str
      name:
        description: Energy Clients Query's name.
        type: str
    type: list
  attributes:
    description: Energy Clients Query's attributes.
    elements: str
    type: list
  endTime:
    description: Energy Clients Query's endTime.
    type: int
  filters:
    description: Energy Clients Query's filters.
    elements: dict
    suboptions:
      filters:
        description: Energy Clients Query's filters.
        elements: dict
        suboptions:
          key:
            description: Energy Clients Query's key.
            type: str
          operator:
            description: Energy Clients Query's operator.
            type: str
          value:
            description: Energy Clients Query's value.
            elements: str
            type: list
        type: list
      logicalOperator:
        description: Energy Clients Query's logicalOperator.
        type: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  page:
    description: Energy Clients Query's page.
    suboptions:
      cursor:
        description: Energy Clients Query's cursor.
        type: str
      limit:
        description: Energy Clients Query's limit.
        type: int
      sortBy:
        description: Energy Clients Query's sortBy.
        elements: dict
        suboptions:
          function:
            description: Energy Clients Query's function.
            type: str
          name:
            description: Energy Clients Query's name.
            type: str
          order:
            description: Energy Clients Query's order.
            type: str
        type: list
    type: dict
  startTime:
    description: Energy Clients Query's startTime.
    type: int
  views:
    description: Energy Clients Query's views.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Clients QueryClientsEnergy
    description: Complete reference of the QueryClientsEnergy API.
    link: https://developer.cisco.com/docs/dna-center/#!query-clients-energy
notes:
  - SDK Method used are
    clients.Clients.query_clients_energy,
  - Paths used are
    post /dna/data/api/v1/energy/clients/query,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.energy_clients_query:
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
      cursor: string
      limit: 0
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
      "response": [
        {
          "id": "string",
          "deviceName": "string",
          "deviceCategory": "string",
          "deviceSubCategory": "string",
          "siteId": "string",
          "siteHierarchy": "string",
          "siteHierarchyId": "string",
          "energyConsumed": 0,
          "estimatedCost": 0,
          "estimatedEmission": 0,
          "carbonIntensity": 0,
          "connectedDeviceName": "string",
          "connectedInterfaceName": "string",
          "aggregateAttributes": [
            {
              "name": "string",
              "function": "string",
              "value": 0
            }
          ]
        }
      ],
      "page": {
        "limit": 0,
        "cursor": "string",
        "count": 0,
        "sortBy": [
          {
            "name": "string",
            "order": "string",
            "function": "string"
          }
        ]
      },
      "version": "string"
    }
"""
