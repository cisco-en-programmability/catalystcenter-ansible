#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_devices_accept_ssh_key_change_create
short_description: Resource module for Network Devices Accept Ssh Key Change Create
description:
  - Manage operation create of the resource Network Devices Accept Ssh Key Change Create. - > This API allows users to approve
    new SSH keys for specified devices, ensuring the continuation of connection establishment. When the global setting `autoAcceptSshKeys`
    is set to `false`, users can manually approve new SSH keys for selected devices using this API. This approval is valid
    until the SSH key changes again. Users can monitor individual device requests using the `/dna/intent/api/v1/tasks?rootId=${taskId}`
    API. Additionally, if `resync` is set to `true`, the API will submit the device for resynchronization, which is queued
    and processed based on system load.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  networkDeviceIds:
    description: Network Device ids for which to accept the new SSH Keys.
    elements: str
    type: list
  resync:
    description: Optional flag to determine if device resync is needed after accepting a new SSH key.
    type: bool
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices AcceptsNewSSHKeyForSelectedDevices_SchedulesResync
    description: Complete reference of the AcceptsNewSSHKeyForSelectedDevices_SchedulesResync API.
    link: https://developer.cisco.com/docs/dna-center/#!accepts-new-ssh-key-for-selected-devices-schedules-resync
notes:
  - SDK Method used are
    devices.Devices.accepts_new_ssh_key_for_selected_devices_schedules_resync,
  - Paths used are
    post /dna/intent/api/v1/networkDevices/acceptSshKeyChange,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.network_devices_accept_ssh_key_change_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    networkDeviceIds:
      - string
    resync: true
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
