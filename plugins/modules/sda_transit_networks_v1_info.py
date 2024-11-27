#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_transit_networks_v1_info
short_description: Information module for Sda Transit Networks V1
description:
- Get all Sda Transit Networks V1.
- Returns a list of transit networks that match the provided query parameters.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
    - Id query parameter. ID of the transit network.
    type: str
  name:
    description:
    - Name query parameter. Name of the transit network.
    type: str
  type:
    description:
    - >
      Type query parameter. Type of the transit network. Allowed values are IP_BASED_TRANSIT,
      SDA_LISP_PUB_SUB_TRANSIT, SDA_LISP_BGP_TRANSIT.
    type: str
  offset:
    description:
    - Offset query parameter. Starting record for pagination.
    type: float
  limit:
    description:
    - Limit query parameter. Maximum number of records to return.
    type: float
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for SDA GetTransitNetworksV1
  description: Complete reference of the GetTransitNetworksV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-transit-networks
notes:
  - SDK Method used are
    sda.Sda.get_transit_networks_v1,

  - Paths used are
    get /dna/intent/api/v1/sda/transitNetworks,

"""

EXAMPLES = r"""
- name: Get all Sda Transit Networks V1
  cisco.catalystcenter.sda_transit_networks_v1_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
    name: string
    type: string
    offset: 0
    limit: 0
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
          "name": "string",
          "type": "string",
          "ipTransitSettings": {
            "routingProtocolName": "string",
            "autonomousSystemNumber": "string"
          },
          "sdaTransitSettings": {
            "isMulticastOverTransitEnabled": true,
            "controlPlaneNetworkDeviceIds": [
              "string"
            ]
          }
        }
      ],
      "version": "string"
    }
"""
