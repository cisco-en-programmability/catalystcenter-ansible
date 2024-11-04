#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_fabrics_vlanToSsids_fabricId_info
short_description: Information module for Sda Fabrics Vlantossids Fabricid
description:
- Get all Sda Fabrics Vlantossids Fabricid.
- >
   Retrieve the VLANs and SSIDs mapped to the VLAN, within a Fabric Site. The 'fabricId' represents the Fabric ID of
   a particular Fabric Site.
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
  limit:
    description:
    - Limit query parameter. The number of records to show for this page.
    type: float
  offset:
    description:
    - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: float
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Fabric Wireless RetrieveTheVLANsAndSSIDsMappedToTheVLANWithinAFabricSiteV1
  description: Complete reference of the RetrieveTheVLANsAndSSIDsMappedToTheVLANWithinAFabricSiteV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-vla-ns-and-ssi-ds-mapped-to-the-vlan-within-a-fabric-site-v-1
notes:
  - SDK Method used are
    fabric_wireless.FabricWireless.retrieve_the_vlans_and_ssids_mapped_to_the_vlan_within_a_fabric_site_v1,

  - Paths used are
    get /dna/intent/api/v1/sda/fabrics/{fabricId}/vlanToSsids,

"""

EXAMPLES = r"""
- name: Get all Sda Fabrics Vlantossids Fabricid
  cisco.catalystcenter.sda_fabrics_vlanToSsids_fabricId_info:
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
    fabricId: string
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
          "vlanName": "string",
          "ssidDetails": [
            {
              "name": "string",
              "securityGroupTag": "string"
            }
          ]
        }
      ],
      "version": "string"
    }
"""
