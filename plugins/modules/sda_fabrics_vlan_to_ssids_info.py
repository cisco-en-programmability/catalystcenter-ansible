#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sda_fabrics_vlan_to_ssids_info
short_description: Information module for Sda Fabrics Vlan To Ssids Info
description:
- This module represents an alias of the module sda_fabrics_vlan_to_ssids_v1_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  limit:
    description:
    - >
      Limit query parameter. Return only this many IP Pool to SSID Mapping. Default is 500 if not specified.
      Maximum allowed limit is 500.
    type: float
  offset:
    description:
    - Offset query parameter. Number of records to skip for pagination.
    type: float
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Fabric Wireless ReturnsAllTheFabricSitesThatHaveVLANToSSIDMappingV1
  description: Complete reference of the ReturnsAllTheFabricSitesThatHaveVLANToSSIDMappingV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!returns-all-the-fabric-sites-that-have-vlan-to-ssid-mapping
notes:
  - SDK Method used are
    fabric_wireless.FabricWireless.returns_all_the_fabric_sites_that_have_vlan_to_ssid_mapping_v1,

  - Paths used are
    get /dna/intent/api/v1/sda/fabrics/vlanToSsids,
  - It should be noted that this module is an alias of sda_fabrics_vlan_to_ssids_v1_info

"""

EXAMPLES = r"""
- name: Get all Sda Fabrics Vlan To Ssids Info
  cisco.catalystcenter.sda_fabrics_vlan_to_ssids_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    limit: 0
    offset: 0
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
          "fabricId": "string",
          "vlanDetails": [
            {
              "vlanName": "string",
              "ssidDetails": [
                {
                  "name": "string",
                  "securityGroupTag": "string"
                }
              ]
            }
          ]
        }
      ],
      "version": "string"
    }
"""
