#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: networkDevices_resyncIntervalSettings_id
short_description: Resource module for Networkdevices Resyncintervalsettings Id
description:
- Manage operation update of the resource Networkdevices Resyncintervalsettings Id.
- Update the resync interval in minutes for the given network device id.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. The id of the network device.
    type: str
  interval:
    description: Resync interval in minutes. To disable periodic resync, set interval
      as `0`. To use global settings, set interval as `null`.
    type: int
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Devices UpdateResyncIntervalForTheNetworkDeviceV1
  description: Complete reference of the UpdateResyncIntervalForTheNetworkDeviceV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!update-resync-interval-for-the-network-device-v-1
notes:
  - SDK Method used are
    devices.Devices.update_resync_interval_for_the_network_device_v1,

  - Paths used are
    put /dna/intent/api/v1/networkDevices/{id}/resyncIntervalSettings,

"""

EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.networkDevices_resyncIntervalSettings_id:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    id: string
    interval: 0

"""
RETURN = r"""
catalystcenter_response:
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
