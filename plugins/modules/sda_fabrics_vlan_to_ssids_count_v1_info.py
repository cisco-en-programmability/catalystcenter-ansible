#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: sda_fabrics_vlan_to_ssids_count_v1_info
short_description: Information module for Sda Fabrics Vlan To Ssids Count V1
description:
  - Get all Sda Fabrics Vlan To Ssids Count V1.
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
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Fabric Wireless ReturnTheCountOfAllTheFabricSiteWhichHasSSIDToIPPoolMappingV1
    description: Complete reference of the ReturnTheCountOfAllTheFabricSiteWhichHasSSIDToIPPoolMappingV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!return-the-count-of-all-the-fabric-site-which-has-ssid-to-ip-pool-mapping   # noqa: E501
notes:
  - SDK Method used are
    fabric_wireless.FabricWireless.return_the_count_of_all_the_fabric_site_which_has_ssid_to_ip_pool_mapping_v1,
  - Paths used are get /dna/intent/api/v1/sda/fabrics/vlanToSsids/count,
"""
EXAMPLES = r"""
- name: Get all Sda Fabrics Vlan To Ssids Count V1
  cisco.catalystcenter.sda_fabrics_vlan_to_ssids_count_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
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
