#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_multicast_info
short_description: Information module for Sda Multicast
description:
  - Get all Sda Multicast.
  - Get multicast details from SDA fabric.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  siteNameHierarchy:
    description:
      - SiteNameHierarchy query parameter. Fabric site
        name hierarchy.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA GetMulticastDetailsFromSDAFabric
    description: Complete reference of the GetMulticastDetailsFromSDAFabric
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-multicast-details-from-sda-fabric
notes:
  - SDK Method used are
    sda.Sda.get_multicast_details_from_sda_fabric,
  - Paths used are
    get /dna/intent/api/v1/business/sda/multicast,
"""

EXAMPLES = r"""
---
- name: Get all Sda Multicast
  cisco.catalystcenter.sda_multicast_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
    siteNameHierarchy: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "multicastMethod": "string",
      "multicastType": "string",
      "multicastVnInfo": [
        {
          "virtualNetworkName": "string",
          "ipPoolName": "string",
          "internalRpIpAddress": [
            "string"
          ],
          "externalRpIpAddress": "string",
          "ssmInfo": [
            {
              "ssmGroupRange": "string",
              "ssmWildcardMask": "string"
            }
          ]
        }
      ],
      "status": "string",
      "description": "string"
    }
"""
