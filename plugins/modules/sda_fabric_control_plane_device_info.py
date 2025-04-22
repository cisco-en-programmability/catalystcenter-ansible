#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: sda_fabric_control_plane_device_info
short_description: Information module for Sda Fabric Control Plane Device Info
description:
  - This module represents an alias of the module sda_fabric_control_plane_device_v1_info
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
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA GetControlPlaneDeviceFromSDAFabricV1
    description: Complete reference of the GetControlPlaneDeviceFromSDAFabricV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-control-plane-device-from-sda-fabric
notes:
  - SDK Method used are sda.Sda.get_control_plane_device,
  - Paths used are get /dna/intent/api/v1/business/sda/control-plane-device,
  - It should be noted that this module is an alias of sda_fabric_control_plane_device_v1_info
"""
EXAMPLES = r"""
- name: Get all Sda Fabric Control Plane Device Info
  cisco.catalystcenter.sda_fabric_control_plane_device_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    deviceManagementIpAddress: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
