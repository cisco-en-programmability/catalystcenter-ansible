#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_provision_device_info
short_description: Information module for Sda Provision
  Device
description:
  - Get all Sda Provision Device.
  - Get Provisioned Wired Device.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deviceManagementIpAddress:
    description:
      - DeviceManagementIpAddress query parameter.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA GetProvisionedWiredDevice
    description: Complete reference of the GetProvisionedWiredDevice
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-provisioned-wired-device
notes:
  - SDK Method used are
    sda.Sda.get_provisioned_wired_device,
  - Paths used are
    get /dna/intent/api/v1/business/sda/provision-device,
"""

EXAMPLES = r"""
---
- name: Get all Sda Provision Device
  cisco.catalystcenter.sda_provision_device_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    deviceManagementIpAddress: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "deviceManagementIpAddress": "string",
      "siteNameHierarchy": "string",
      "status": "string",
      "description": "string"
    }
"""
