#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sites_site_id_wireless_settings_flex_connect_aaa_override_info
short_description: Information module for Sites Site
  Id Wireless Settings Flex Connect Aaa Override
description:
  - Get all Sites Site Id Wireless Settings Flex Connect
    Aaa Override.
  - This API allows the user to get all Flex Connect
    AAA Override VLAN settings at the given site.
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  siteId:
    description:
      - SiteId path parameter. Site Id.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless
      GetAAAOverrideVlanSettingsBySite
    description: Complete reference of the GetAAAOverrideVlanSettingsBySite
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-aaa-override-vlan-settings-by-site
notes:
  - SDK Method used are
    wireless.Wireless.get_aaa_override_vlan_settings_by_site,
  - Paths used are
    get /dna/intent/api/v1/sites/{siteId}/wirelessSettings/flexConnectAaaOverride,
"""

EXAMPLES = r"""
---
- name: Get all Sites Site Id Wireless Settings Flex
    Connect Aaa Override
  cisco.catalystcenter.sites_site_id_wireless_settings_flex_connect_aaa_override_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
    siteId: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "vlanId": 0,
          "vlanName": "string",
          "inheritedSiteUUID": "string",
          "inheritedSiteNameHierarchy": "string"
        }
      ],
      "version": "string"
    }
"""
