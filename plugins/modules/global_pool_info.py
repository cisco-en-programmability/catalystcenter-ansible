#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: global_pool_info
short_description: Information module for Global Pool
description:
- Get all Global Pool.
- API to get the global pool.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  offset:
    description:
    - Offset query parameter. Offset/starting row. Indexed from 1. Default value of 1.
    type: float
  limit:
    description:
    - Limit query parameter. Number of Global Pools to be retrieved. Default is 25 if not specified.
    type: float
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Network Settings GetGlobalPoolV1
  description: Complete reference of the GetGlobalPoolV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-global-pool-v-1
notes:
  - SDK Method used are
    network_settings.NetworkSettings.get_global_pool_v1,

  - Paths used are
    get /dna/intent/api/v1/global-pool,

"""

EXAMPLES = r"""
- name: Get all Global Pool
  cisco.catalystcenter.global_pool_info:
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
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "ipPoolName": "string",
          "dhcpServerIps": [
            "string"
          ],
          "gateways": [
            "string"
          ],
          "createTime": 0,
          "lastUpdateTime": 0,
          "totalIpAddressCount": 0,
          "usedIpAddressCount": 0,
          "parentUuid": "string",
          "owner": "string",
          "shared": true,
          "overlapping": true,
          "configureExternalDhcp": true,
          "usedPercentage": "string",
          "clientOptions": {},
          "ipPoolType": "string",
          "unavailableIpAddressCount": 0,
          "availableIpAddressCount": 0,
          "totalAssignableIpAddressCount": 0,
          "dnsServerIps": [
            "string"
          ],
          "hasSubpools": true,
          "defaultAssignedIpAddressCount": 0,
          "context": [
            {
              "owner": "string",
              "contextKey": "string",
              "contextValue": "string"
            }
          ],
          "ipv6": true,
          "id": "string",
          "ipPoolCidr": "string"
        }
      ],
      "version": "string"
    }
"""
