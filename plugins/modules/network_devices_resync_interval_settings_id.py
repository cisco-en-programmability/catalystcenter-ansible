#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_devices_resync_interval_settings_id
short_description: Resource module for Network Devices
  Resync Interval Settings Id
description:
  - Manage operation update of the resource Network
    Devices Resync Interval Settings Id.
  - Update the resync interval in minutes for the given
    network device id.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. The id of the network
      device.
    type: str
  interval:
    description: Resync interval in minutes. To disable
      periodic resync, set interval as `0`. To use global
      settings, set interval as `null`.
    type: int
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices
      UpdateResyncIntervalForTheNetworkDevice
    description: Complete reference of the UpdateResyncIntervalForTheNetworkDevice
      API.
    link: https://developer.cisco.com/docs/dna-center/#!update-resync-interval-for-the-network-device
notes:
  - SDK Method used are
    devices.Devices.update_resync_interval_for_the_network_device,
  - Paths used are
    put /dna/intent/api/v1/networkDevices/{id}/resyncIntervalSettings,
"""

EXAMPLES = r"""
---
- name: Update all
  cisco.catalystcenter.network_devices_resync_interval_settings_id:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    state: present
    id: string
    interval: 0
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
