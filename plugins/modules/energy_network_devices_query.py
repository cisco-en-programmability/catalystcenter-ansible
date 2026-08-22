#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: energy_network_devices_query
short_description: Resource module for Energy Network Devices Query
description:
  - Manage operation create of the resource Energy Network Devices Query.
  - Retrieves a list of network devices along with their energy data for a.
version_added: '2.2.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  aggregateAttributes:
    description: Energy Network Devices Query's aggregateAttributes.
    elements: dict
    suboptions:
      function:
        description: Energy Network Devices Query's function.
        type: str
      name:
        description: Energy Network Devices Query's name.
        type: str
    type: list
  attributes:
    description: Energy Network Devices Query's attributes.
    elements: str
    type: list
  endTime:
    description: Energy Network Devices Query's endTime.
    type: int
  filters:
    description: Energy Network Devices Query's filters.
    elements: dict
    suboptions:
      filters:
        description: Energy Network Devices Query's filters.
        elements: dict
        suboptions:
          key:
            description: Energy Network Devices Query's key.
            type: str
          operator:
            description: Energy Network Devices Query's operator.
            type: str
          value:
            description: Energy Network Devices Query's value.
            elements: str
            type: list
        type: list
      logicalOperator:
        description: Energy Network Devices Query's logicalOperator.
        type: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  page:
    description: Energy Network Devices Query's page.
    suboptions:
      cursor:
        description: Energy Network Devices Query's cursor.
        type: str
      limit:
        description: Energy Network Devices Query's limit.
        type: int
      sortBy:
        description: Energy Network Devices Query's sortBy.
        elements: dict
        suboptions:
          function:
            description: Energy Network Devices Query's function.
            type: str
          name:
            description: Energy Network Devices Query's name.
            type: str
          order:
            description: Energy Network Devices Query's order.
            type: str
        type: list
    type: dict
  startTime:
    description: Energy Network Devices Query's startTime.
    type: int
  views:
    description: Energy Network Devices Query's views.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices QueryDevicesEnergy
    description: Complete reference of the QueryDevicesEnergy API.
    link: https://developer.cisco.com/docs/dna-center/#!query-devices-energy
notes:
  - SDK Method used are
    devices.Devices.query_devices_energy,
  - Paths used are
    post /dna/data/api/v1/energy/networkDevices/query,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.energy_network_devices_query:
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
