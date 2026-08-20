#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sites_wireless_settings_ssids_count_info
short_description: Information module for Sites Wireless Settings Ssids Count
description:
  - Get all Sites Wireless Settings Ssids Count.
  - This API allows the user to get count of all SSIDs Service Set Identifier at `siteId`.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
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
        _inherited query parameter. `_inherited` query parameter indicates wether the current SSID count at
        `siteId` is of the SSID it is inheriting or count of non-inheriting SSIDs. - When `_inherited` is
        `false` then - Should a request include a non-global `siteId` with the `_inherited` flag set to `false`,
        the API will respond with a count of all SSIDs that have been explicitly overridden at the specified
        site identifier (`siteId`). - When `_inherited` is `true` then - In the case where a non-global `siteId`
        is accompanied by the `_inherited` flag set to true, the API is tasked with returning a count that
        aggregates the following - The number of SSIDs inherited from the global level. - The number of SSIDs
        derived from the immediate parent site where an override is present.
    type: bool
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless GETSSIDCOUNTBYSITE
    description: Complete reference of the GETSSIDCOUNTBYSITE API.
    link: https://developer.cisco.com/docs/dna-center/#!g-etssidcountbysite
notes:
  - SDK Method used are
    wireless.Wireless.get_ssid_count_by_site,
  - Paths used are
    get /dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids/count,
"""

EXAMPLES = r"""
---
- name: Get all Sites Wireless Settings Ssids Count
  cisco.catalystcenter.sites_wireless_settings_ssids_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    _inherited: true
    siteId: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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
