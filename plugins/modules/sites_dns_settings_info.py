#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sites_dns_settings_info
short_description: Information module for Sites Dns Settings
description:
  - Get all Sites Dns Settings.
  - Retrieves domain name and DNS servers for the given site.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Site Id.
    type: str
  _inherited:
    description:
      - >
        _inherited query parameter. Include settings explicitly set for this site and settings inherited from
        sites higher in the site hierarchy; when `false`, `null` values indicate that the site inherits that
        setting from the parent site or a site higher in the site hierarchy.
    type: bool
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Network Settings RetrieveDNSSettingsForASite
    description: Complete reference of the RetrieveDNSSettingsForASite API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-dns-settings-for-a-site
notes:
  - SDK Method used are
    network_settings.NetworkSettings.retrieve_dns_settings_for_a_site,
  - Paths used are
    get /dna/intent/api/v1/sites/{id}/dnsSettings,
"""

EXAMPLES = r"""
---
- name: Get all Sites Dns Settings
  cisco.catalystcenter.sites_dns_settings_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    _inherited: true
    id: e298f95b-cd70-48ae-a590-b2076bfb6033
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
        "dns": {}
      },
      "version": "string"
    }
"""
