#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sites_wireless_settings_ssids_count_v1_info
short_description: Information module for Sites Wireless Settings Ssids Count V1
description:
- Get all Sites Wireless Settings Ssids Count V1.
- This API allows the user to get count of all SSIDs Service Set Identifier .
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  siteId:
    description:
    - SiteId path parameter. Site UUID.
    type: str
  _inherited:
    description:
    - >
      _inherited query parameter. This query parameter indicates whether the current SSID count at the given
      'siteId' is of the SSID(s) it is inheriting or count of non-inheriting SSID(s).
    type: bool
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless GetSSIDCountBySiteV1
  description: Complete reference of the GetSSIDCountBySiteV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-ssid-count-by-site
notes:
  - SDK Method used are
    wireless.Wireless.get_ssid_count_by_site_v1,

  - Paths used are
    get /dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids/count,

"""

EXAMPLES = r"""
- name: Get all Sites Wireless Settings Ssids Count V1
  cisco.catalystcenter.sites_wireless_settings_ssids_count_v1_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    _inherited: True
    siteId: string
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
