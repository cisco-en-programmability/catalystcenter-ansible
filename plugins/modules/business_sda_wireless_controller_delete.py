#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: business_sda_wireless_controller_delete
short_description: Resource module for Business Sda
  Wireless Controller Delete
description:
  - Manage operation delete of the resource Business
    Sda Wireless Controller Delete.
  - Remove WLC from Fabric Domain.
version_added: '4.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  deviceIPAddress:
    description: DeviceIPAddress query parameter. Device
      Management IP Address.
    type: str
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Fabric
      Wireless RemoveWLCFromFabricDomain
    description: Complete reference of the RemoveWLCFromFabricDomain
      API.
    link: https://developer.cisco.com/docs/dna-center/#!remove-wlc-from-fabric-domain
notes:
  - SDK Method used are
    fabric_wireless.FabricWireless.remove_w_l_c_from_fabric_domain,
  - Paths used are
    delete /dna/intent/api/v1/business/sda/wireless-controller,
    - Removed 'deviceName' and 'siteNameHierarchy' options
    in v4.3.0.
"""

EXAMPLES = r"""
---
- name: Delete all
  cisco.catalystcenter.business_sda_wireless_controller_delete:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    deviceIPAddress: string
    headers: '{{my_headers | from_json}}'
"""
RETURN = r"""
dnac_response:
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
