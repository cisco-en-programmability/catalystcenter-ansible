#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_fabrics_vlanToSsids_count_info
short_description: Information module for Sda Fabrics Vlantossids Count
description:
- Get all Sda Fabrics Vlantossids Count.
- Return the count of all the fabric site which has SSID to IP Pool mapping.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Fabric Wireless ReturnTheCountOfAllTheFabricSiteWhichHasSSIDToIPPoolMappingV1
  description: Complete reference of the ReturnTheCountOfAllTheFabricSiteWhichHasSSIDToIPPoolMappingV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!return-the-count-of-all-the-fabric-site-which-has-ssid-to-ip-pool-mapping-v-1
notes:
  - SDK Method used are
    fabric_wireless.FabricWireless.return_the_count_of_all_the_fabric_site_which_has_ssid_to_ip_pool_mapping_v1,

  - Paths used are
    get /dna/intent/api/v1/sda/fabrics/vlanToSsids/count,

"""

EXAMPLES = r"""
- name: Get all Sda Fabrics Vlantossids Count
  cisco.catalystcenter.sda_fabrics_vlanToSsids_count_info:
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
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
