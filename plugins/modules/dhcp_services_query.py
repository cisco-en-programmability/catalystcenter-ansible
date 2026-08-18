#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: dhcp_services_query
short_description: Resource module for Dhcp Services Query
description:
  - Manage operation create of the resource Dhcp Services Query.
  - Retrieves the list of DHCP Services and offers complex filtering and sorting.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  endTime:
    description: Dhcp Services Query's endTime.
    type: int
  filters:
    description: Dhcp Services Query's filters.
    elements: dict
    suboptions:
      key:
        description: Dhcp Services Query's key.
        type: str
      operator:
        description: Dhcp Services Query's operator.
        type: str
      value:
        description: Dhcp Services Query's value.
        elements: str
        type: list
    type: list
  headers:
    description: Additional headers.
    type: dict
  page:
    description: Dhcp Services Query's page.
    suboptions:
      limit:
        description: Dhcp Services Query's limit.
        type: int
      offset:
        description: Dhcp Services Query's offset.
        type: int
      sortBy:
        description: Dhcp Services Query's sortBy.
        elements: dict
        suboptions:
          name:
            description: Dhcp Services Query's name.
            type: str
          order:
            description: Dhcp Services Query's order.
            type: str
        type: list
    type: dict
  startTime:
    description: Dhcp Services Query's startTime.
    type: int
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices RetrievesTheListOfDHCPServicesForGivenSetOfComplexFilters
    description: Complete reference of the RetrievesTheListOfDHCPServicesForGivenSetOfComplexFilters API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-dhcp-services-for-given-set-of-complex-filters
notes:
  - SDK Method used are
    devices.Devices.retrieves_the_list_of_dhcp_services_for_given_set_of_complex_filters,
  - Paths used are
    post /dna/data/api/v1/dhcpServices/query,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.dhcp_services_query:
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
    page:
      limit: 0
      offset: 0
      sortBy:
        - name: string
          order: string
    startTime: 0
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
          "serverIp": "string",
          "deviceId": "string",
          "deviceName": "string",
          "deviceFamily": "string",
          "deviceSiteHierarchy": "string",
          "deviceSiteId": "string",
          "deviceSiteHierarchyId": "string",
          "transactions": 0,
          "failedTransactions": 0,
          "successfulTransactions": 0,
          "latency": 0,
          "discoverOfferLatency": 0,
          "requestAcknowledgeLatency": 0
        }
      ],
      "page": {
        "limit": 0,
        "offset": 0,
        "count": 0,
        "sortBy": [
          {
            "name": "string",
            "order": "string"
          }
        ]
      },
      "version": "string"
    }
"""
