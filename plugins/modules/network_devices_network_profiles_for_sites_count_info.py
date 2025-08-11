#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_devices_network_profiles_for_sites_count_info
short_description: Information module for Network Devices
  Network Profiles For Sites Count
description:
  - Get all Network Devices Network Profiles For Sites
    Count.
  - Retrieves the count of network profiles for sites.
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
      - Type query parameter. Filter the response to
        only count profiles of a given type.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Site Design
      RetrievesTheCountOfNetworkProfilesForSites
    description: Complete reference of the RetrievesTheCountOfNetworkProfilesForSites
      API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-count-of-network-profiles-for-sites
notes:
  - SDK Method used are
    site_design.SiteDesign.retrieves_the_count_of_network_profiles_for_sites,
  - Paths used are
    get /dna/intent/api/v1/networkProfilesForSites/count,
"""

EXAMPLES = r"""
---
- name: Get all Network Devices Network Profiles For
    Sites Count
  cisco.catalystcenter.network_devices_network_profiles_for_sites_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    type: string
  register: result
"""
RETURN = r"""
dnac_response:
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
