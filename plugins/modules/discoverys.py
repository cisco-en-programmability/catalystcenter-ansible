#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: discoverys
short_description: Resource module for Discoverys
description:
  - Manage operations create, update and delete of the resource Discoverys.
  - This API creates a discovery. The response includes a task `url` that provides access to the task's details.
  - API to delete discovery by the given discovery id. - > API to edit the discovery details of the given discovery id. Updating
    the discovery details while the discovery is in progress is not allowed.
version_added: '2.3.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  credentials:
    description: Credentials to be used for discovering devices. If multiple credentials are provided, they will be prioritized
      based on specificity and protocol version. Device-specific credentials take precedence over global credentials. Among
      SNMP versions, SNMPv3 credentials are given higher priority over SNMPv2 credentials.
    suboptions:
      cli:
        description: CLI credentials for device.
        suboptions:
          protocolOrder:
            description: Connection protocol for the device. Default value is SSH.
            elements: str
            type: list
        type: dict
      httpRead:
        description: HTTP(S) read credentials for device.
        type: dict
      httpWrite:
        description: HTTP(S) write credentials for device.
        type: dict
      netconf:
        description: NETCONF credentials for device.
        type: dict
      snmp:
        description: SNMP credentials for device.
        suboptions:
          retries:
            description: The number of times to repeat the failed SNMP polling request after a timeout. Max value supported
              is 3. Default is Global SNMP retry (if exists) or 3.
            type: int
          timeout:
            description: The interval (in seconds) after which SNMP failure to respond to the polling request generates a
              timeout. Max value supported is 300. Default is Global SNMP timeout (if exists) or 5.
            type: int
        type: dict
    type: dict
  discoveryTypeDetails:
    description: Details of the discovery type.
    type: dict
  id:
    description: Unique identifier of the discovery settings.
    type: str
  managementIpSelectionMethod:
    description: When Catalyst Center discovers a device, it uses one of the device's IP addresses as the preferred management
      IP address for the device. The IP address can be that of a built-in management interface of the device, another physical
      interface, or a logical interface like Loopback0. You can configure Catalyst Center to log the device's loopback IP
      address as the preferred management IP address, provided the IP address is reachable from Catalyst Center. - `DEFAULT`
      * Uses the IP address provided in the discovery request as the management IP. - `LOOPBACK` If you choose to use a device's
      loopback IP address as the preferred management IP address, Catalyst Center determines the preferred management IP address
      as follows * If the device has one loopback interface, that loopback interface IP address is used. * If the device has
      multiple loopback interfaces, the loopback interface with the highest IP address is used. * If there are no loopback
      interfaces, the Ethernet interface with the highest IP address is used. (Subinterface IP addresses are not considered.)
      * If there are no Ethernet interfaces, the serial interface with the highest IP address is used. Example LOOPBACK.
    type: str
  name:
    description: The name of the discovery job being created. This will be a unique name.
    type: str
  onlyNewDevice:
    description: This flag indicates to discover only new devices that are not in inventory. If set to `true`, only devices
      that are not in the inventory will be discovered. If set to `false`, devices that already exist in the inventory will
      not be listed in the `discovered devices` list.
    type: bool
  siteId:
    description: The site id to which the discovered devices will be assigned.
    type: str
  updateManagementIp:
    description: This flag indicates if the management IP address of existing devices to be updated as part of this discovery.
      If set false devices get discovered with the existing management IP address. If set true it overwrites the management
      IP address with the new IP address used in discovery.
    type: bool
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices CreatesDiscovery
    description: Complete reference of the CreatesDiscovery API.
    link: https://developer.cisco.com/docs/dna-center/#!creates-discovery
  - name: Cisco Catalyst Center documentation for Devices DeletesDiscoveryById
    description: Complete reference of the DeletesDiscoveryById API.
    link: https://developer.cisco.com/docs/dna-center/#!deletes-discovery-by-id
  - name: Cisco Catalyst Center documentation for Devices EditsDiscovery
    description: Complete reference of the EditsDiscovery API.
    link: https://developer.cisco.com/docs/dna-center/#!edits-discovery
notes:
  - SDK Method used are
    devices.Devices.creates_discovery,
    devices.Devices.deletes_discovery_by_id,
    devices.Devices.edits_discovery,
  - Paths used are
    post /dna/intent/api/v1/discoverys,
    delete /dna/intent/api/v1/discoverys/{id},
    put /dna/intent/api/v1/discoverys/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.discoverys:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    credentials:
      cli: {}
      httpRead: {}
      httpWrite: {}
      netconf: {}
      snmp: {}
    discoveryTypeDetails: {}
    id: string
    managementIpSelectionMethod: string
    name: string
    onlyNewDevice: true
    siteId: string
    updateManagementIp: true
- name: Update by id
  cisco.catalystcenter.discoverys:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    credentials:
      cli: {}
      httpRead: {}
      httpWrite: {}
      netconf: {}
      snmp: {}
    discoveryTypeDetails:
      range:
        - ipAddressEnd: {}
          ipAddressStart: {}
      type: string
    id: string
    managementIpSelectionMethod: string
    onlyNewDevice: true
    updateManagementIp: true
- name: Delete by id
  cisco.catalystcenter.discoverys:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: string
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
