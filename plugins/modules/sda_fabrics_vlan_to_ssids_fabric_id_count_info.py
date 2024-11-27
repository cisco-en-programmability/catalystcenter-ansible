#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sda_fabrics_vlan_to_ssids_fabric_id_count_info
short_description: Information module for Sda Fabrics Vlan To Ssids Fabric Id Count Info
description:
- This module represents an alias of the module sda_fabrics_vlan_to_ssids_fabric_id_count_v1_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  fabricId:
    description:
    - FabricId path parameter. The 'fabricId' represents the Fabric ID of a particular Fabric Site.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.6
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Fabric Wireless ReturnsTheCountOfVLANsMappedToSSIDsInAFabricSiteV1
  description: Complete reference of the ReturnsTheCountOfVLANsMappedToSSIDsInAFabricSiteV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!returns-the-count-of-vla-ns-mapped-to-ssi-ds-in-a-fabric-site
notes:
  - SDK Method used are
    fabric_wireless.FabricWireless.returns_the_count_of_vlans_mapped_to_ssids_in_a_fabric_site_v1,

  - Paths used are
    get /dna/intent/api/v1/sda/fabrics/{fabricId}/vlanToSsids/count,
  - It should be noted that this module is an alias of sda_fabrics_vlan_to_ssids_fabric_id_count_v1_info

"""

EXAMPLES = r"""
- name: Get all Sda Fabrics Vlan To Ssids Fabric Id Count Info
  cisco.catalystcenter.sda_fabrics_vlan_to_ssids_fabric_id_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    fabricId: string
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
