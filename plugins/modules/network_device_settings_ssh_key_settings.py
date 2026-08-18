#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_settings_ssh_key_settings
short_description: Resource module for Network Device Settings Ssh Key Settings
description:
  - Manage operation update of the resource Network Device Settings Ssh Key Settings. - > This API lets users control how
    the system handles new SSH key from network devices during SSH connections. With the `autoAcceptSshKeys` flag set to `false`,
    the system will block the SSH connection if a network device presents a new SSH key. If the flag is set to `true`, the
    system will automatically accept the SSH key. Users can also use the device-specific `/dna/intent/api/v1/networkDevices/acceptSshKeyChange`
    API to approve SSH key changes individually when the global auto-accept is turned off.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  autoAcceptSshKeys:
    description: Indicates whether SSH keys are automatically accepted.
    type: bool
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices ConfigureGlobalSettingsForSSHKeyHandling
    description: Complete reference of the ConfigureGlobalSettingsForSSHKeyHandling API.
    link: https://developer.cisco.com/docs/dna-center/#!configure-global-settings-for-ssh-key-handling
notes:
  - SDK Method used are
    devices.Devices.configure_global_settings_for_ssh_key_handling,
  - Paths used are
    put /dna/intent/api/v1/networkDeviceSettings/sshKeySettings,
"""

EXAMPLES = r"""
---
- name: Update all
  cisco.catalystcenter.network_device_settings_ssh_key_settings:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    autoAcceptSshKeys: true
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
