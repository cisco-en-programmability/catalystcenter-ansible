#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: location_servers_spaces_activate_via_one_time_token_create
short_description: Resource module for Location Servers Spaces Activate Via One Time Token Create
description:
  - Manage operation create of the resource Location Servers Spaces Activate Via One Time Token Create. - > Activate or re-activate
    Cisco Spaces integration using a one-time-use token generated from Cisco Spaces User Interface. Please refer to Cisco
    Spaces Configuration Guide at https //www.cisco.com for more information on generating a one-time-use token. Once activated,
    you can associate Cisco Spaces to one or more Sites, using '/dna/intent/api/v1/sites/{id}/locationServerSettings'.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  oneTimeUseToken:
    description: Used during Cisco Spaces activation when activating using a one-time-use token generated from Cisco Spaces
      User Interface. Please refer to Cisco Spaces Configuration Guide at https //www.cisco.com for more information on generating
      a one-time-use token.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for System Settings ActivatesWithCiscoSpacesUsingTokenAuthentication
    description: Complete reference of the ActivatesWithCiscoSpacesUsingTokenAuthentication API.
    link: https://developer.cisco.com/docs/dna-center/#!activates-with-cisco-spaces-using-token-authentication
notes:
  - SDK Method used are
    system_settings.SystemSettings.activates_with_cisco_spaces_using_token_authentication,
  - Paths used are
    post /dna/intent/api/v1/locationServers/spaces/activateViaOneTimeToken,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.location_servers_spaces_activate_via_one_time_token_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    oneTimeUseToken: string
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
