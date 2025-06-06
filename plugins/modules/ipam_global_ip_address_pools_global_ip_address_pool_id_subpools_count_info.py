#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: ipam_global_ip_address_pools_global_ip_address_pool_id_subpools_count_info
short_description: Information module for Ipam Global Ip Address Pools Global Ip Address
  Pool Id Subpools Count Info
description:
  - This module represents an alias of the module ipam_global_ip_address_pools_global_ip_address_pool_id_subpools_count_v1_info
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  globalIpAddressPoolId:
    description:
      - GlobalIpAddressPoolId path parameter. The `id` of the global IP address pool
        for which to count subpools.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Network Settings CountsSubpoolsOfAGlobalIPAddressPoolV1
    description: Complete reference of the CountsSubpoolsOfAGlobalIPAddressPoolV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!counts-subpools-of-a-global-ip-address-pool
notes:
  - SDK Method used are network_settings.NetworkSettings.counts_subpools_of_a_global_ip_address_pool_v1,
  - Paths used are get
    /dna/intent/api/v1/ipam/globalIpAddressPools/{globalIpAddressPoolId}/subpools/count,
  - It should be noted that this module is an alias of ipam_global_ip_address_pools_global_ip_address_pool_id_subpools_count_v1_info
"""
EXAMPLES = r"""
- name: Get all Ipam Global Ip Address Pools Global Ip Address Pool Id Subpools
    Count Info
  cisco.catalystcenter.ipam_global_ip_address_pools_global_ip_address_pool_id_subpools_count_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    globalIpAddressPoolId: string
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
        "count": 0
      },
      "version": "string"
    }
"""
