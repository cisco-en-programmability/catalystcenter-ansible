#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: network_device_inventory_insight_link_mismatch_info
short_description: Information module for Network Device Inventory Insight Link Mismatch Info
description:
- This module represents an alias of the module network_device_inventory_insight_link_mismatch_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  siteId:
    description:
    - SiteId path parameter.
    type: str
  offset:
    description:
    - Offset query parameter. Row Number. Default value is 1.
    type: int
  limit:
    description:
    - Limit query parameter. The number of records to show for this page. Min 1, Max 500.
    type: int
  category:
    description:
    - Category query parameter. Links mismatch category. Value can be speed-duplex or vlan.
    type: str
  sortBy:
    description:
    - SortBy query parameter. Sort By.
    type: str
  order:
    description:
    - Order query parameter. Order. Value can be asc or desc. Default value is asc.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices InventoryInsightDeviceLinkMismatchAPIV1
  description: Complete reference of the InventoryInsightDeviceLinkMismatchAPIV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!inventory-insight-device-link-mismatch-api
notes:
  - SDK Method used are
    devices.Devices.inventory_insight_device_link_mismatch,

  - Paths used are
    get /dna/intent/api/v1/network-device/insight/{siteId}/device-link,
  - It should be noted that this module is an alias of network_device_inventory_insight_link_mismatch_v1_info

"""

EXAMPLES = r"""
- name: Get all Network Device Inventory Insight Link Mismatch Info
  cisco.catalystcenter.network_device_inventory_insight_link_mismatch_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    offset: 0
    limit: 0
    category: string
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
          "endPortAllowedVlanIds": "string",
          "endPortNativeVlanId": "string",
          "startPortAllowedVlanIds": "string",
          "startPortNativeVlanId": "string",
          "linkStatus": "string",
          "endDeviceHostName": "string",
          "endDeviceId": "string",
          "endDeviceIpAddress": "string",
          "endPortAddress": "string",
          "endPortDuplex": "string",
          "endPortId": "string",
          "endPortMask": "string",
          "endPortName": "string",
          "endPortPepId": "string",
          "endPortSpeed": "string",
          "startDeviceHostName": "string",
          "startDeviceId": "string",
          "startDeviceIpAddress": "string",
          "startPortAddress": "string",
          "startPortDuplex": "string",
          "startPortId": "string",
          "startPortMask": "string",
          "startPortName": "string",
          "startPortPepId": "string",
          "startPortSpeed": "string",
          "lastUpdated": "string",
          "numUpdates": 0,
          "avgUpdateFrequency": 0,
          "type": "string",
          "instanceUuid": "string",
          "instanceTenantId": "string"
        }
      ],
      "version": "string"
    }
"""
