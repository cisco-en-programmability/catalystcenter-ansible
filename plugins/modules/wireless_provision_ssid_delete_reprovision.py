#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_provision_ssid_delete_reprovision
short_description: Resource module for Wireless Provision
  Ssid Delete Reprovision
description:
  - Manage operation delete of the resource Wireless
    Provision Ssid Delete Reprovision.
  - Removes SSID or WLAN from the network profile, reprovision
    the devices and deletes the SSID or WLAN from DNA
    Center.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  managedAPLocations:
    description: ManagedAPLocations path parameter.
      List of managed AP locations (Site Hierarchies).
      This parameter needs to be encoded as per UTF-8
      encoding.
    type: str
  ssidName:
    description: SsidName path parameter. SSID Name.
      This parameter needs to be encoded as per UTF-8
      encoding.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless
      DeleteSSIDAndProvisionItToDevices
    description: Complete reference of the DeleteSSIDAndProvisionItToDevices
      API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-ssid-and-provision-it-to-devices
notes:
  - SDK Method used are
    wireless.Wireless.delete_ssid_and_provision_it_to_devices,
  - Paths used are
    delete /dna/intent/api/v1/business/ssid/{ssidName}/{managedAPLocations},
"""

EXAMPLES = r"""
---
- name: Delete by id
  cisco.catalystcenter.wireless_provision_ssid_delete_reprovision:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: '{{my_headers | from_json}}'
    managedAPLocations: string
    ssidName: string
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
