#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: ipam_global_ip_address_pools_global_ip_address_pool_id_subpools_v1_info
short_description: Information module for Ipam Global Ip Address Pools Global Ip Address Pool Id Subpools V1
description:
- Get all Ipam Global Ip Address Pools Global Ip Address Pool Id Subpools V1.
- >
   Retrieves subpools IDs of a global IP address pool. The IDs can be fetched with
   `/dna/intent/api/v1/ipam/siteIpAddressPools/{id}`.
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
    - GlobalIpAddressPoolId path parameter. The `id` of the global IP address pool for which to retrieve subpool IDs.
    type: str
  offset:
    description:
    - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: float
  limit:
    description:
    - Limit query parameter. The number of records to show for this page;The minimum is 1, and the maximum is 500.
    type: float
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Network Settings RetrievesSubpoolsIDsOfAGlobalIPAddressPoolV1
  description: Complete reference of the RetrievesSubpoolsIDsOfAGlobalIPAddressPoolV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!retrieves-subpools-i-ds-of-a-global-ip-address-pool
notes:
  - SDK Method used are
    network_settings.NetworkSettings.retrieves_subpools_ids_of_a_global_ip_address_pool_v1,

  - Paths used are
    get /dna/intent/api/v1/ipam/globalIpAddressPools/{globalIpAddressPoolId}/subpools,

"""

EXAMPLES = r"""
- name: Get all Ipam Global Ip Address Pools Global Ip Address Pool Id Subpools V1
  cisco.catalystcenter.ipam_global_ip_address_pools_global_ip_address_pool_id_subpools_v1_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    offset: 0
    limit: 0
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
      "response": [
        {
          "id": "string"
        }
      ],
      "version": "string"
    }
"""
