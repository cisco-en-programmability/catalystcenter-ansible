#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_devices_unassign_from_site_apply
short_description: Resource module for Network Devices
  Unassign From Site Apply
description:
  - Manage operation create of the resource Network
    Devices Unassign From Site Apply. - > Unassign unprovisioned
    network devices from their site. If device controllability
    is enabled, it will be triggered once device unassigned
    from site successfully. Device Controllability can
    be enabled/disabled using `/dna/intent/api/v1/networkDevices/deviceControllability/settings`.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  deviceIds:
    description: Network device Ids, ranging from a
      minimum of 1 to a maximum of 100.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Site Design
      UnassignNetworkDevicesFromSites
    description: Complete reference of the UnassignNetworkDevicesFromSites
      API.
    link: https://developer.cisco.com/docs/dna-center/#!unassign-network-devices-from-sites
notes:
  - SDK Method used are
    site_design.SiteDesign.unassign_network_devices_from_sites,
  - Paths used are
    post /dna/intent/api/v1/networkDevices/unassignFromSite/apply,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.network_devices_unassign_from_site_apply:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    deviceIds:
      - string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": {
        "url": "string",
        "taskId": "string"
      }
    }
"""
