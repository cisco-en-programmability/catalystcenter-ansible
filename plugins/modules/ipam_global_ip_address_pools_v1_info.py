#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: ipam_global_ip_address_pools_v1_info
short_description: Information module for Ipam Global Ip Address Pools V1
description:
  - Get all Ipam Global Ip Address Pools V1.
  - >
    Retrieves global IP address pools. Global pools are not associated with any particular
    site, but may have portions
    of their address space reserved by site-specific subpools.
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
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Network Settings RetrievesGlobalIPAddressPoolsV1
    description: Complete reference of the RetrievesGlobalIPAddressPoolsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-global-ip-address-pools
notes:
  - SDK Method used are network_settings.NetworkSettings.retrieves_global_ip_address_pools_v1,
  - Paths used are get /dna/intent/api/v1/ipam/globalIpAddressPools,
"""
EXAMPLES = r"""
- name: Get all Ipam Global Ip Address Pools V1
  cisco.catalystcenter.ipam_global_ip_address_pools_v1_info:
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
          "addressSpace": {
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
            "defaultAssignedAddresses": "string"
          },
          "id": "string",
          "name": "string",
          "poolType": "string"
        }
      ],
      "version": "string"
    }
"""
