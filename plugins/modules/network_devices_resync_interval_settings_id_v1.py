#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_devices_resync_interval_settings_id_v1
short_description: Resource module for Network Devices Resync Interval Settings Id
  V1
description:
  - Manage operation update of the resource Network Devices Resync Interval Settings
    Id V1.
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
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices UpdateResyncIntervalForTheNetworkDeviceV1
    description: Complete reference of the UpdateResyncIntervalForTheNetworkDeviceV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!update-resync-interval-for-the-network-device
notes:
  - SDK Method used are devices.Devices.update_resync_interval_for_the_network_device_v1,
  - Paths used are put /dna/intent/api/v1/networkDevices/{id}/resyncIntervalSettings,
"""
EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.network_devices_resync_interval_settings_id_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    state: present
    id: string
    interval: 0
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
