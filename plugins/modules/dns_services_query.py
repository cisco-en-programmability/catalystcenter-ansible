#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: dns_services_query
short_description: Resource module for Dns Services Query
description:
  - Manage operation create of the resource Dns Services Query.
  - Retrieves the list of DNS Services and offers complex filtering and sorting.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  endTime:
    description: Dns Services Query's endTime.
    type: int
  filters:
    description: Dns Services Query's filters.
    elements: dict
    suboptions:
      key:
        description: Dns Services Query's key.
        type: str
      operator:
        description: Dns Services Query's operator.
        type: str
      value:
        description: Dns Services Query's value.
        elements: str
        type: list
    type: list
  headers:
    description: Additional headers.
    type: dict
  page:
    description: Dns Services Query's page.
    suboptions:
      limit:
        description: Dns Services Query's limit.
        type: int
      offset:
        description: Dns Services Query's offset.
        type: int
      sortBy:
        description: Dns Services Query's sortBy.
        elements: dict
        suboptions:
          name:
            description: Dns Services Query's name.
            type: str
          order:
            description: Dns Services Query's order.
            type: str
        type: list
    type: dict
  startTime:
    description: Dns Services Query's startTime.
    type: int
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices RetrievesTheListOfDNSServicesForGivenSetOfComplexFilters
    description: Complete reference of the RetrievesTheListOfDNSServicesForGivenSetOfComplexFilters API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-dns-services-for-given-set-of-complex-filters
notes:
  - SDK Method used are
    devices.Devices.retrieves_the_list_of_dns_services_for_given_set_of_complex_filters,
  - Paths used are
    post /dna/data/api/v1/dnsServices/query,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.dns_services_query:
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
          "failures": [
            {
              "failureResponseCode": 0,
              "failureDescription": "string",
              "failedTransactions": 0
            }
          ],
          "successfulTransactions": 0,
          "latency": 0,
          "ssid": "string"
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
