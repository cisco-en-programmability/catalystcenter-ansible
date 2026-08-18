#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pnp_network_devices
short_description: Resource module for Pnp Network Devices
description:
  - Manage operation delete of the resource Pnp Network Devices.
  - Deletes a specific Plug and Play PNP device using its unique identifier.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  id:
    description: Id path parameter. Unique identifier for the device in PnP.
    type: str
  removePnpProfile:
    description: RemovePnpProfile query parameter. When set to true, this removes all configured PnP profiles from the device
      (if eligible). This ensures the device does not restart PnP discovery automatically. Eligible devices are IOS-XE devices
      (switches, routers, wireless controllers, etc) that are already present in system inventory.
    type: bool
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Device Onboarding (PnP) DeletePnPDeviceByID
    description: Complete reference of the DeletePnPDeviceByID API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-pn-p-device-by-id
notes:
  - SDK Method used are
    device_onboarding_pnp.DeviceOnboardingPnp.delete_pnp_device_by_id,
  - Paths used are
    delete /dna/intent/api/v1/pnpNetworkDevices/{id},
"""

EXAMPLES = r"""
---
- name: Delete by id
  cisco.catalystcenter.pnp_network_devices:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: string
    removePnpProfile: true
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {},
      "version": "string"
    }
"""
