#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: assign_to_site_apply
short_description: Resource module for Assign To Site
  Apply
description:
  - Manage operation create of the resource Assign To
    Site Apply. - > Assign unprovisioned network devices
    to a site. Along with that it can also be used to
    assign unprovisioned network devices to a different
    site. If device controllability is enabled, it will
    be triggered once device assigned to site successfully.
    Device Controllability can be enabled/disabled using
    `/dna/intent/api/v1/networkDevices/deviceControllability/settings`.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  deviceIds:
    description: Unassigned network devices, ranging
      from a minimum of 1 to a maximum of 100.
    elements: str
    type: list
  siteId:
    description: This must be building Id or floor Id.
      Access points, Sensors are assigned to floor.
      Remaining network devices are assigned to building.
      Site Id can be retrieved using '/intent/api/v1/sites'.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Site Design
      AssignNetworkDevicesToASite
    description: Complete reference of the AssignNetworkDevicesToASite
      API.
    link: https://developer.cisco.com/docs/dna-center/#!assign-network-devices-to-a-site
notes:
  - SDK Method used are
    site_design.SiteDesign.assign_network_devices_to_a_site,
  - Paths used are
    post /dna/intent/api/v1/networkDevices/assignToSite/apply,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.assign_to_site_apply:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    deviceIds:
      - string
    siteId: string
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
