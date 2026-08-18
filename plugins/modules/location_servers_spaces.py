#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: location_servers_spaces
short_description: Resource module for Location Servers Spaces
description:
  - Manage operation delete of the resource Location Servers Spaces.
  - Deactivate Catalyst Center from Cisco Spaces.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options: {}
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for System Settings DeletesCiscoSpacesSettings
    description: Complete reference of the DeletesCiscoSpacesSettings API.
    link: https://developer.cisco.com/docs/dna-center/#!deletes-cisco-spaces-settings
notes:
  - SDK Method used are
    system_settings.SystemSettings.deletes_cisco_spaces_settings,
  - Paths used are
    delete /dna/intent/api/v1/locationServers/spaces,
"""

EXAMPLES = r"""
---
- name: Delete all
  cisco.catalystcenter.location_servers_spaces:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
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
