#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sites_banner_settings
short_description: Resource module for Sites Banner Settings
description:
  - Manage operation update of the resource Sites Banner Settings.
  - Sets banner settings for the given site.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  banner:
    description: Sites Banner Settings's banner.
    suboptions:
      inheritedSiteId:
        description: The Site Id of the site that this setting is inherited from.
        type: str
      inheritedSiteName:
        description: The name of the site that this setting is inherited from.
        type: str
    type: dict
  id:
    description: Id path parameter. Site Id.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Network Settings SetBannerSettingsForASite
    description: Complete reference of the SetBannerSettingsForASite API.
    link: https://developer.cisco.com/docs/dna-center/#!set-banner-settings-for-a-site
notes:
  - SDK Method used are
    network_settings.NetworkSettings.set_banner_settings_for_a_site,
  - Paths used are
    put /dna/intent/api/v1/sites/{id}/bannerSettings,
"""

EXAMPLES = r"""
---
- name: Update all
  cisco.catalystcenter.sites_banner_settings:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    banner: {}
    id: e298f95b-cd70-48ae-a590-b2076bfb6033
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
