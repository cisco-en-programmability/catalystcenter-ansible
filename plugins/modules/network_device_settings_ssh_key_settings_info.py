#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_settings_ssh_key_settings_info
short_description: Information module for Network Device Settings Ssh Key Settings
description:
  - Get all Network Device Settings Ssh Key Settings. - > This API retrieves the current settings for handling SSH key changes
    from network devices during SSH connections. If the `autoAcceptSshKeys` flag is `true`, SSH keys are accepted automatically.
    If it is `false`, manual approval is needed for any SSH key changes.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices GetGlobalSettingsValueForNewSSHKeyHandling
    description: Complete reference of the GetGlobalSettingsValueForNewSSHKeyHandling API.
    link: https://developer.cisco.com/docs/dna-center/#!get-global-settings-value-for-new-ssh-key-handling
notes:
  - SDK Method used are
    devices.Devices.get_global_settings_value_for_new_ssh_key_handling,
  - Paths used are
    get /dna/intent/api/v1/networkDeviceSettings/sshKeySettings,
"""

EXAMPLES = r"""
---
- name: Get all Network Device Settings Ssh Key Settings
  cisco.catalystcenter.network_device_settings_ssh_key_settings_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
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
        "autoAcceptSshKeys": true
      },
      "version": "string"
    }
"""
