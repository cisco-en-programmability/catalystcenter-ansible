#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: sda_fabrics_vlan_to_ssids_fabric_id_count_v1_info
short_description: Information module for Sda Fabrics Vlan To Ssids Fabric Id Count
  V1
description:
  - Get all Sda Fabrics Vlan To Ssids Fabric Id Count V1.
  - >
    Returns the count of VLANs mapped to SSIDs in a Fabric Site. The 'fabricId' represents
    the Fabric ID of a
    particular Fabric Site.
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
      - FabricId path parameter. The 'fabricId' represents the Fabric ID of a particular
        Fabric Site.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Fabric Wireless ReturnsTheCountOfVLANsMappedToSSIDsInAFabricSiteV1
    description: Complete reference of the ReturnsTheCountOfVLANsMappedToSSIDsInAFabricSiteV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!returns-the-count-of-vla-ns-mapped-to-ssi-ds-in-a-fabric-site
notes:
  - SDK Method used are
    fabric_wireless.FabricWireless.returns_the_count_of_vlans_mapped_to_ssids_in_a_fabric_site_v1,
  - Paths used are get /dna/intent/api/v1/sda/fabrics/{fabricId}/vlanToSsids/count,
"""
EXAMPLES = r"""
- name: Get all Sda Fabrics Vlan To Ssids Fabric Id Count V1
  cisco.catalystcenter.sda_fabrics_vlan_to_ssids_fabric_id_count_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
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
