#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: ipam_site_ip_address_pools_v1_info
short_description: Information module for Ipam Site Ip Address Pools V1
description:
  - Get all Ipam Site Ip Address Pools V1.
  - Retrieves IP address subpools, which reserve address space from a global pool
    or global pools .
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first
        record is numbered 1.
    type: float
  limit:
    description:
      - Limit query parameter. The number of records to show for this page;The minimum
        is 1, and the maximum is 500.
    type: float
  sortBy:
    description:
      - SortBy query parameter. A property within the response to sort by.
    type: str
  order:
    description:
      - Order query parameter. Whether ascending or descending order should be used
        to sort the response.
    type: str
  siteId:
    description:
      - >
        SiteId query parameter. The `id` of the site for which to retrieve IP address
        subpools. Only subpools whose
        `siteId` exactly matches will be fetched, parent or child site matches will
        not be included.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Network Settings RetrievesIPAddressSubpoolsV1
    description: Complete reference of the RetrievesIPAddressSubpoolsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-ip-address-subpools
notes:
  - SDK Method used are network_settings.NetworkSettings.retrieves_ip_address_subpools_v1,
  - Paths used are get /dna/intent/api/v1/ipam/siteIpAddressPools,
"""
EXAMPLES = r"""
- name: Get all Ipam Site Ip Address Pools V1
  cisco.catalystcenter.ipam_site_ip_address_pools_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    offset: 0
    limit: 0
    sortBy: string
    order: string
    siteId: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "ipV4AddressSpace": {
            "subnet": "string",
            "prefixLength": 0,
            "gatewayIpAddress": "string",
            "dhcpServers": [
              "string"
            ],
            "dnsServers": [
              "string"
            ],
            "totalAddresses": "string",
            "unassignableAddresses": "string",
            "assignedAddresses": "string",
            "defaultAssignedAddresses": "string",
            "slaacSupport": true,
            "globalPoolId": "string"
          },
          "ipV6AddressSpace": {
            "subnet": "string",
            "prefixLength": 0,
            "gatewayIpAddress": "string",
            "dhcpServers": [
              "string"
            ],
            "dnsServers": [
              "string"
            ],
            "totalAddresses": "string",
            "unassignableAddresses": "string",
            "assignedAddresses": "string",
            "defaultAssignedAddresses": "string",
            "slaacSupport": true,
            "globalPoolId": "string"
          },
          "name": "string",
          "poolType": "string",
          "siteId": "string",
          "siteName": "string"
        }
      ],
      "version": "string"
    }
"""
