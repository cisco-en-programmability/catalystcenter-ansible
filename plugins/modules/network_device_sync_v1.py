#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_sync_v1
short_description: Resource module for Network Device Sync V1
description:
- Manage operation update of the resource Network Device Sync V1.
- >
   Synchronizes the devices. If forceSync param is false default then the sync would run in normal priority thread.
   If forceSync param is true then the sync would run in high priority thread if available, else the sync will fail.
   Result can be seen in the child task of each device.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  forceSync:
    description: ForceSync query parameter.
    type: bool
  payload:
    description: Network Device Sync's payload.
    elements: str
    type: list
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices SyncDevicesV1
  description: Complete reference of the SyncDevicesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!sync-devices
notes:
  - SDK Method used are
    devices.Devices.sync_devices_using_forcesync,

  - Paths used are
    put /dna/intent/api/v1/network-device/sync,

"""

EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.network_device_sync_v1:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    forceSync: true
    payload:
    - string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
