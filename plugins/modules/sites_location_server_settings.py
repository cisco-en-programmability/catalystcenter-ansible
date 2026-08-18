#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sites_location_server_settings
short_description: Resource module for Sites Location Server Settings
description:
  - Manage operation update of the resource Sites Location Server Settings.
  - Set Location Server Settings for the given site Cisco Spaces or CMX Server .
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  id:
    description: Id path parameter. Site Id.
    type: str
  locationServer:
    description: Location Server (Cisco Spaces or CMX Server) setting.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Network Settings SetLocationServerSettingsForASiteCiscoSpacesOrCMXServer
    description: Complete reference of the SetLocationServerSettingsForASiteCiscoSpacesOrCMXServer API.
    link: https://developer.cisco.com/docs/dna-center/#!set-location-server-settings-for-a-site-cisco-spaces-or-cmx-server
notes:
  - SDK Method used are
    network_settings.NetworkSettings.set_location_server_settings_for_a_site_cisco_spaces_or_cmx_server,
  - Paths used are
    put /dna/intent/api/v1/sites/{id}/locationServerSettings,
"""

EXAMPLES = r"""
---
- name: Update all
  cisco.catalystcenter.sites_location_server_settings:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    id: e298f95b-cd70-48ae-a590-b2076bfb6033
    locationServer: {}
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
