#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sites_banner_settings_info
short_description: Information module for Sites Banner Settings
description:
  - Get all Sites Banner Settings. - > Retrieve banner settings for a site; `null` values indicate that the setting will be
    inherited from the parent site; empty objects `{}` indicate that the setting is unset at a site.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
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
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Network Settings RetrieveBannerSettingsForASite
    description: Complete reference of the RetrieveBannerSettingsForASite API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-banner-settings-for-a-site
notes:
  - SDK Method used are
    network_settings.NetworkSettings.retrieve_banner_settings_for_a_site,
  - Paths used are
    get /dna/intent/api/v1/sites/{id}/bannerSettings,
"""

EXAMPLES = r"""
---
- name: Get all Sites Banner Settings
  cisco.catalystcenter.sites_banner_settings_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    _inherited: true
    id: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "banner": {
          "type": "string",
          "message": "string",
          "inheritedSiteId": "string",
          "inheritedSiteName": "string"
        }
      },
      "version": "string"
    }
"""
