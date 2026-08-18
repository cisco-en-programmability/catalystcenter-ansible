#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: switches_configs_intended_port_convert_create
short_description: Resource module for Switches Configs Intended Port Convert Create
description:
  - Manage operation create of the resource Switches Configs Intended Port Convert Create. - > This API converts port configurations
    between Layer 2 and Layer 3 modes on a switch. The conversion is supported for the physical ports feature ethernetInterfaceConfig
    configurations. The device config learning must have enabled for the switch using the API /dna/campus/api/v1/switches/configs/deployed/enable
    and Error code NCCO15475 can be observed if not enabled.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  id:
    description: Id path parameter. Network device id of the switch. The Network device id is identified from the GET network
      device API /dna/intent/api/v1/network-device response.
    type: str
  names:
    description: List of port names to convert.
    elements: str
    type: list
  targetType:
    description: Type of conversion to perform.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wired ConvertIntendedPortConfigurations
    description: Complete reference of the ConvertIntendedPortConfigurations API.
    link: https://developer.cisco.com/docs/dna-center/#!convert-intended-port-configurations
notes:
  - SDK Method used are
    wired.Wired.convert_intended_port_configurations,
  - Paths used are
    post /dna/campus/api/v1/switches/{id}/configs/intended/port/convert,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.switches_configs_intended_port_convert_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    id: string
    names:
      - string
    targetType: string
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
