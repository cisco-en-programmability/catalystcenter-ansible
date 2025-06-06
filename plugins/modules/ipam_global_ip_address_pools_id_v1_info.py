#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: ipam_global_ip_address_pools_id_v1_info
short_description: Information module for Ipam Global Ip Address Pools Id V1
description:
  - Get Ipam Global Ip Address Pools Id V1 by id.
  - >
    Retrieves a global IP address pool. Global pools are not associated with any particular
    site, but may have
    portions of their address space reserved by site-specific subpools.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. The `id` of the global IP address pool to retrieve.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Network Settings RetrievesAGlobalIPAddressPoolV1
    description: Complete reference of the RetrievesAGlobalIPAddressPoolV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-a-global-ip-address-pool
notes:
  - SDK Method used are network_settings.NetworkSettings.retrieves_a_global_ip_address_pool_v1,
  - Paths used are get /dna/intent/api/v1/ipam/globalIpAddressPools/{id},
"""
EXAMPLES = r"""
- name: Get Ipam Global Ip Address Pools Id V1 by id
  cisco.catalystcenter.ipam_global_ip_address_pools_id_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
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
      },
      "version": "string"
    }
"""
