#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_devices_update_create
short_description: Resource module for Network Devices Update Create
description:
  - Manage operation create of the resource Network Devices Update Create.
  - Updates specified fields of an existing network device. Only include the fields you wish to update.
version_added: '2.3.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  category:
    description: Category of the device. Used to determine the type of the device being added. | Category | Description |
      Required Credentials | Optional Credentials | | -------------------- | ----------------------------------------------------------------------------------...
      | -------------------- | -------------------- | | `NETWORK_DEVICE` | Standard Cisco network devices like switches, routers,
      controllers | CLI, SNMP | HTTP, Netconf | | `COMPUTE_DEVICE` | Server or computing system manufactured by Cisco such
      as Unified Computing System (UCS) | HTTP | CLI, SNMP | | `THIRD_PARTY_DEVICE` | Non-Cisco network devices that support
      SNMP monitoring | SNMP | - | | `MERAKI_DASHBOARD` | Cisco Meraki cloud-managed devices accessed via Meraki Dashboard
      | Meraki | - | | `FIREWALL_MANAGEMENT_CENTER` | Cisco Secure Firewall Management Center (FMC) | HTTP | - |.
    type: str
  credentials:
    description: Credentials used to access the network device.
    suboptions:
      cli:
        description: Network Devices Update Create's cli.
        suboptions:
          protocol:
            description: Protocol used for CLI access. Default is SSH.
            type: str
        type: dict
      http:
        description: Network Devices Update Create's http.
        suboptions:
          protocol:
            description: HTTP protocol. Compute devices require HTTPS.
            type: str
        type: dict
      meraki:
        description: Meraki credentials. Required if type is MERAKI_DASHBOARD.
        suboptions:
          apiKey:
            description: Meraki API key.
            type: str
          orgIds:
            description: Meraki organizations for which the devices needs to be imported. Imports devices from all organizations
              if not provided.
            elements: str
            type: list
        type: dict
      netconf:
        description: NETCONF credentials used to access the network device. The credentials are used to access the device
          using NETCONF.
        type: dict
      snmp:
        description: Extra properties for SNMP credentials.
        suboptions:
          retries:
            description: SNMP retry. Default is Global SNMP retry (if exists) or 3.
            type: int
          timeout:
            description: SNMP timeout in seconds. Default is Global SNMP timeout (if exists) or 5.
            type: int
        type: dict
    type: dict
  id:
    description: Id path parameter. Unique identifier of the network device.
    type: str
  managementAddress:
    description: Either an IP address or a fully-qualified domain name.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices PartiallyUpdatesAnExistingNetworkDevice
    description: Complete reference of the PartiallyUpdatesAnExistingNetworkDevice API.
    link: https://developer.cisco.com/docs/dna-center/#!partially-updates-an-existing-network-device
notes:
  - SDK Method used are
    devices.Devices.partially_updates_an_existing_network_device,
  - Paths used are
    post /dna/intent/api/v1/networkDevices/{id}/update,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.network_devices_update_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    category: string
    credentials:
      cli: {}
      http: {}
      meraki:
        apiKey: string
        orgIds:
          - string
      netconf: {}
      snmp: {}
    id: string
    managementAddress: {}
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
