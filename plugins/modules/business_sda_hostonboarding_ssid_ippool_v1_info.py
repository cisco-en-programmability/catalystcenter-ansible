#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: business_sda_hostonboarding_ssid_ippool_v1_info
short_description: Information module for Business Sda Hostonboarding Ssid Ippool V1
description:
- Get all Business Sda Hostonboarding Ssid Ippool V1.
- Get SSID to IP Pool Mapping.
version_added: '4.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  vlanName:
    description:
    - VlanName query parameter. VLAN Name.
    type: str
  siteNameHierarchy:
    description:
    - SiteNameHierarchy query parameter. Site Name Heirarchy.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Fabric Wireless GetSSIDToIPPoolMappingV1
  description: Complete reference of the GetSSIDToIPPoolMappingV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-ssid-to-ip-pool-mapping
notes:
  - SDK Method used are
    fabric_wireless.FabricWireless.get_ssid_to_ip_pool_mapping_v1,

  - Paths used are
    get /dna/intent/api/v1/business/sda/hostonboarding/ssid-ippool,

"""

EXAMPLES = r"""
- name: Get all Business Sda Hostonboarding Ssid Ippool V1
  cisco.catalystcenter.business_sda_hostonboarding_ssid_ippool_v1_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    vlanName: string
    siteNameHierarchy: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "vlanName": "string",
      "ssidDetails": [
        {
          "name": "string",
          "scalableGroupName": "string"
        }
      ]
    }
"""
