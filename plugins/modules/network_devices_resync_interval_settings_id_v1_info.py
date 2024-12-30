#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_devices_resync_interval_settings_id_v1_info
short_description: Information module for Network Devices Resync Interval Settings Id V1
description:
- Get all Network Devices Resync Interval Settings Id V1.
- Fetch the reysnc interval for the given network device id.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
    - Id path parameter. The id of the network device.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices GetResyncIntervalForTheNetworkDeviceV1
  description: Complete reference of the GetResyncIntervalForTheNetworkDeviceV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-resync-interval-for-the-network-device
notes:
  - SDK Method used are
    devices.Devices.get_resync_interval_for_the_network_device_v1,

  - Paths used are
    get /dna/intent/api/v1/networkDevices/{id}/resyncIntervalSettings,

"""

EXAMPLES = r"""
- name: Get all Network Devices Resync Interval Settings Id V1
  cisco.catalystcenter.network_devices_resync_interval_settings_id_v1_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "interval": 0
      },
      "version": "string"
    }
"""
