#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_replacements_workflow_deploy_create
short_description: Resource module for Network Device Replacements Workflow Deploy Create
description:
  - Manage operation create of the resource Network Device Replacements Workflow Deploy Create. - > API to trigger RMA workflow
    that will replace faulty device with replacement device with same configuration and images.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  configKey:
    description: If the faulty device was configured with AES password encryption, please provide the same master encryption
      config key to enable encryption on the replacement device. `Failing to provide the Master Encryption Configuration Key
      or providing an incorrect one will result in the RMA process transferring only a partial configuration to the replacement
      device. Configurations such as encrypted passwords or keys would fail to restore without the correct encryption key.`.
    type: str
  configureSso:
    description: Flag to configure HA SSO (High Availability Stateful Switchover) .
    type: bool
  faultyDeviceSerialNumber:
    description: Serial number of the faulty device.
    type: str
  haSsoDetail:
    description: Network Device Replacements Workflow Deploy Create's haSsoDetail.
    suboptions:
      haInterfaceName:
        description: An optional HA interface for the primary device, required only for `9800 CL` device type.
        type: str
      localRedundancyIp:
        description: The IP address assigned to the HA interface on the primary device (either the active or standby device).
        type: str
      peerDeviceSerialNumber:
        description: Serial number of the peer device.
        type: str
      peerHaInterfaceName:
        description: An optional HA interface for the peer device, required only for `9800 CL` device type.
        type: str
      redundancyIp:
        description: Specifies the IP address of the HA interface on the peer device (the other device in the HA pair).
        type: str
    type: dict
  outOfBand:
    description: Indicates that device replacement was performed manually outside the system (out-of-band). Set to true to
      complete remaining configuration and integration steps and bring device to managed state.
    type: bool
  primaryGatewayIp:
    description: Primary gateway IP address of PnP device.
    type: str
  primaryGatewayIpv6:
    description: Primary gateway IPv6 address of PnP device.
    type: str
  primaryIpInterfaceName:
    description: Primary IP interface name of PnP device.
    type: str
  primaryNetmask:
    description: Primary netmask of PnP device.
    type: str
  primaryPrefixLength:
    description: IPv6 Primary Prefix Length.Mandatory for IPv6, default is 'null' otherwise.
    type: int
  primaryVlanId:
    description: Primary VLAN ID of PnP device.
    type: int
  primaryWirelessManagementIp:
    description: Primary wireless management IP address of PnP device.
    type: str
  primaryWirelessManagementIpv6:
    description: Primary wireless management IPv6 address of PnP device.
    type: str
  replacementDeviceSerialNumber:
    description: Serial number of the replacement device.
    type: str
  secondaryGatewayIp:
    description: Secondary gateway IP address of PnP device.
    type: str
  secondaryGatewayIpv6:
    description: Secondary gateway IPv6 address of PnP device.
    type: str
  secondaryIpInterfaceName:
    description: Secondary IP interface name of PnP device.
    type: str
  secondaryNetmask:
    description: Secondary netmask of PnP device.
    type: str
  secondaryPrefixLength:
    description: IPv6 Secondary Prefix Length.Mandatory for IPv6, default is 'null' otherwise.
    type: int
  secondaryVlanId:
    description: Secondary VLAN ID of PnP device.
    type: int
  secondaryWirelessManagementIp:
    description: Secondary wireless management IP address of PnP device.
    type: str
  secondaryWirelessManagementIpv6:
    description: Secondary wireless management IPv6 address of PnP device.
    type: str
  type:
    description: Type of the device.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Device Replacement DeployDeviceReplacementWorkflowSiteManagement
    description: Complete reference of the DeployDeviceReplacementWorkflowSiteManagement API.
    link: https://developer.cisco.com/docs/dna-center/#!deploy-device-replacement-workflow-site-management
notes:
  - SDK Method used are
    device_replacement.DeviceReplacement.deploy_device_replacement_workflow_site_management,
  - Paths used are
    post /dna/intent/api/v1/networkDeviceReplacements/workflow/deploy,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.network_device_replacements_workflow_deploy_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    configKey: string
    configureSso: true
    faultyDeviceSerialNumber: string
    haSsoDetail:
      haInterfaceName: string
      localRedundancyIp: string
      peerDeviceSerialNumber: string
      peerHaInterfaceName: string
      redundancyIp: string
    outOfBand: true
    primaryGatewayIp: string
    primaryGatewayIpv6: string
    primaryIpInterfaceName: string
    primaryNetmask: string
    primaryPrefixLength: 0
    primaryVlanId: 0
    primaryWirelessManagementIp: string
    primaryWirelessManagementIpv6: string
    replacementDeviceSerialNumber: string
    secondaryGatewayIp: string
    secondaryGatewayIpv6: string
    secondaryIpInterfaceName: string
    secondaryNetmask: string
    secondaryPrefixLength: 0
    secondaryVlanId: 0
    secondaryWirelessManagementIp: string
    secondaryWirelessManagementIpv6: string
    type: string
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
