#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: fabrics_fabric_id_switch_wireless_setting_reload
short_description: Resource module for Fabrics Fabric Id Switch Wireless Setting Reload
description:
  - Manage operation create of the resource Fabrics Fabric Id Switch Wireless Setting Reload. - > This API is used to reload
    switches after disabling wireless to remove the wireless-controller configuration on the device. When wireless is disabled
    on a switch, all wireless configurations are removed except for the wireless-controller configuration. To completely remove
    the wireless-controller configuration, you can use this API. Please note that using this API will cause a reload of the
    devices. This API should only be used for devices that have wireless disabled but still have the 'wireless-controller'
    configuration present. The reload payload can have a maximum of two switches as only two switches can have a wireless
    role in a fabric site.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  fabricId:
    description: FabricId path parameter. The 'fabricId' represents the Fabric ID of a particular Fabric Site. The 'fabricId'
      can be obtained using the api /dna/intent/api/v1/sda/fabricSites.
    type: str
  response:
    description: Fabrics Fabric Id Switch Wireless Setting Reload's response.
    elements: dict
    suboptions:
      deviceId:
        description: Device ID.
        type: str
    type: list
  version:
    description: Fabrics Fabric Id Switch Wireless Setting Reload's version.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Fabric Wireless ReloadSwitchForWirelessControllerCleanup
    description: Complete reference of the ReloadSwitchForWirelessControllerCleanup API.
    link: https://developer.cisco.com/docs/dna-center/#!reload-switch-for-wireless-controller-cleanup
notes:
  - SDK Method used are
    fabric_wireless.FabricWireless.reload_switch_for_wireless_controller_cleanup,
  - Paths used are
    post /dna/intent/api/v1/sda/fabrics/{fabricId}/switchWirelessSetting/reload,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.fabrics_fabric_id_switch_wireless_setting_reload:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    deviceId: 41828dc1-7481-4ff7-94dc-5b43af9319cb
    fabricId: e290f1ee-6c54-4b01-90e6-d701748f0851
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
