#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: business_sda_wireless_controller_create
short_description: Resource module for Business Sda Wireless Controller Create
description:
- Manage operation create of the resource Business Sda Wireless Controller Create.
- Add WLC to Fabric Domain.
version_added: '4.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  deviceName:
    description: WLC Device Name.
    type: str
  siteNameHierarchy:
    description: Fabric Site Name Hierarchy.
    type: str
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Fabric Wireless AddWLCToFabricDomainV1
  description: Complete reference of the AddWLCToFabricDomainV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!add-wlc-to-fabric-domain-v-1
notes:
  - SDK Method used are
    fabric_wireless.FabricWireless.add_w_l_c_to_fabric_domain_v1,

  - Paths used are
    post /dna/intent/api/v1/business/sda/wireless-controller,

  - Removed 'deviceIPAddress' options in v4.3.0.
"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.business_sda_wireless_controller_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    deviceName: string
    siteNameHierarchy: string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }
"""
