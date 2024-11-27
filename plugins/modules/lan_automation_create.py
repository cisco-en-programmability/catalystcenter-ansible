#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: lan_automation_create
short_description: Resource module for Lan Automation Create
description:
- This module represents an alias of the module lan_automation_create_v1
version_added: '6.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Lan Automation Create's payload.
    elements: dict
    suboptions:
      discoveredDeviceSiteNameHierarchy:
        description: Discovered device site name.
        type: str
      hostNameFileId:
        description: Use /dna/intent/api/v1/file/namespace/nw_orch api to get the file
          id for the already uploaded file in nw_orch namespace.
        type: str
      hostNamePrefix:
        description: Host name prefix which shall be assigned to the discovered device.
        type: str
      ipPools:
        description: Lan Automation Create's ipPools.
        elements: dict
        suboptions:
          ipPoolName:
            description: Name of the IP pool.
            type: str
          ipPoolRole:
            description: Role of the IP pool. Supported roles are MAIN_POOL and PHYSICAL_LINK_POOL.
            type: str
        type: list
      isisDomainPwd:
        description: IS-IS domain password in plain text.
        type: str
      mulitcastEnabled:
        description: To enable underlay native multicast.
        type: bool
      peerDeviceManagmentIPAddress:
        description: Peer seed management IP address.
        type: str
      primaryDeviceInterfaceNames:
        description: The list of interfaces on primary seed via which the discovered
          devices are connected.
        elements: str
        type: list
      primaryDeviceManagmentIPAddress:
        description: Primary seed management IP address.
        type: str
      redistributeIsisToBgp:
        description: Advertise LAN Automation summary route into BGP.
        type: bool
    type: list
requirements:
- catalystcentersdk >= 2.3.7.6
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for LAN Automation LANAutomationStartV1
  description: Complete reference of the LANAutomationStartV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!l-an-automation-start
notes:
  - SDK Method used are
    lan_automation.LanAutomation.lan_automation_start_v1,

  - Paths used are
    post /dna/intent/api/v1/lan-automation,
  - It should be noted that this module is an alias of lan_automation_create_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.lan_automation_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    payload:
    - discoveredDeviceSiteNameHierarchy: string
      hostNameFileId: string
      hostNamePrefix: string
      ipPools:
      - ipPoolName: string
        ipPoolRole: string
      isisDomainPwd: string
      mulitcastEnabled: true
      peerDeviceManagmentIPAddress: string
      primaryDeviceInterfaceNames:
      - string
      primaryDeviceManagmentIPAddress: string
      redistributeIsisToBgp: true

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "message": "string",
        "id": "string"
      },
      "version": "string"
    }
"""
