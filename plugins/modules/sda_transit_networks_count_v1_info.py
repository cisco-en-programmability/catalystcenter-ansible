#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: sda_transit_networks_count_v1_info
short_description: Information module for Sda Transit Networks Count V1
description:
  - Get all Sda Transit Networks Count V1.
  - Returns the count of transit networks that match the provided query parameters.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  type:
    description:
      - >
        Type query parameter. Type of the transit network. Allowed values are IP_BASED_TRANSIT,
        SDA_LISP_PUB_SUB_TRANSIT, SDA_LISP_BGP_TRANSIT.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA GetTransitNetworksCountV1
    description: Complete reference of the GetTransitNetworksCountV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-transit-networks-count
notes:
  - SDK Method used are sda.Sda.get_transit_networks_count_v1,
  - Paths used are get /dna/intent/api/v1/sda/transitNetworks/count,
"""
EXAMPLES = r"""
- name: Get all Sda Transit Networks Count V1
  cisco.catalystcenter.sda_transit_networks_count_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    type: string
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
