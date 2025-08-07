#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_fabric_control_plane_device_info
short_description: Information module for Sda Fabric
  Control Plane Device
description:
  - Get all Sda Fabric Control Plane Device.
  - Get control plane device from SDA Fabric.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deviceManagementIpAddress:
    version_added: "4.0.0"
    description:
      - DeviceManagementIpAddress query parameter.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA GetControlPlaneDeviceFromSDAFabric
    description: Complete reference of the GetControlPlaneDeviceFromSDAFabric
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-control-plane-device-from-sda-fabric
notes:
  - SDK Method used are
    sda.Sda.get_control_plane_device,
  - Paths used are
    get /dna/intent/api/v1/business/sda/control-plane-device,
"""

EXAMPLES = r"""
---
- name: Get all Sda Fabric Control Plane Device
  cisco.catalystcenter.sda_fabric_control_plane_device_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
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
      "deviceName": "string",
      "roles": "string",
      "siteNameHierarchy": "string",
      "routeDistributionProtocol": "string",
      "status": "string",
      "description": "string"
    }
"""
