#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: wireless_provision_device_update
short_description: Resource module for Wireless Provision Device Update
description:
- This module represents an alias of the module wireless_provision_device_update_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  payload:
    description: Wireless Provision Device Update's payload.
    elements: dict
    suboptions:
      deviceName:
        description: Controller Name.
        type: str
      dynamicInterfaces:
        description: Wireless Provision Device Update's dynamicInterfaces.
        elements: dict
        suboptions:
          interfaceGateway:
            description: Interface Gateway. Required for AireOS.
            type: str
          interfaceIPAddress:
            description: Interface IP Address. Required for AireOS.
            type: str
          interfaceName:
            description: Interface Name. Required for AireOS and EWLC.
            type: str
          interfaceNetmaskInCIDR:
            description: Interface Netmask In CIDR. Required for AireOS.
            type: int
          lagOrPortNumber:
            description: Lag Or Port Number. Required for AireOS.
            type: int
          vlanId:
            description: VLAN ID. Required for AireOS and EWLC.
            type: int
        type: list
      managedAPLocations:
        description: List of managed AP locations (Site Hierarchies).
        elements: str
        type: list
    type: list
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless ProvisionUpdateV1
  description: Complete reference of the ProvisionUpdateV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!provision-update
notes:
  - SDK Method used are
    wireless.Wireless.provision_update,

  - Paths used are
    put /dna/intent/api/v1/wireless/provision,
  - It should be noted that this module is an alias of wireless_provision_device_update_v1

"""

EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.wireless_provision_device_update:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: '{{my_headers | from_json}}'
    payload:
    - deviceName: string
      dynamicInterfaces:
      - interfaceGateway: string
        interfaceIPAddress: string
        interfaceName: string
        interfaceNetmaskInCIDR: 0
        lagOrPortNumber: 0
        vlanId: 0
      managedAPLocations:
      - string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }
"""
