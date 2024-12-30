#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: ipam_global_ip_address_pools_count_v1_info
short_description: Information module for Ipam Global Ip Address Pools Count V1
description:
- Get all Ipam Global Ip Address Pools Count V1.
- >
   Counts global IP address pools. Global pools are not associated with any particular site, but may have portions of
   their address space reserved by site-specific subpools.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Network Settings CountsGlobalIPAddressPoolsV1
  description: Complete reference of the CountsGlobalIPAddressPoolsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!counts-global-ip-address-pools
notes:
  - SDK Method used are
    network_settings.NetworkSettings.counts_global_ip_address_pools_v1,

  - Paths used are
    get /dna/intent/api/v1/ipam/globalIpAddressPools/count,

"""

EXAMPLES = r"""
- name: Get all Ipam Global Ip Address Pools Count V1
  cisco.catalystcenter.ipam_global_ip_address_pools_count_v1_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
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
