#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: iot_non_fabric_rep_rings
short_description: Resource module for Iot Non Fabric Rep Rings
description:
  - Manage operation create of the resource Iot Non Fabric Rep Rings.
  - This API configures a REP ring on NON-FABRIC deployment. The input payload contains the following fields-.
version_added: '2.2.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  deploymentMode:
    description: FABRIC as well as NON_FABRIC deployments.
    type: str
  id:
    description: REP ring identifier.
    type: str
  macsecConfig:
    description: MACsec configuration for REP Ring create requests (PSK / SHOULD_SECURE only).
    suboptions:
      accessControlMode:
        description: MACsec access control mode. Only `SHOULD_SECURE` is currently supported for PSK Encryption mode.
        type: str
      ciphersuite:
        description: MACsec cipher suite - `GCM_AES_128` or `GCM_AES_256`.
        type: str
      encryptionMode:
        description: MACsec encryption mode. Only `PSK` (Pre-Shared Key) is currently supported.
        type: str
      keys:
        description: List of MACsec keys for the keychain (maximum 12 keys).
        elements: dict
        suboptions:
          cryptoAlgo:
            description: Cryptographic algorithm `AES_128_CMAC` (requires 32 hex digit passPhrase) or `AES_256_CMAC`.
            type: str
          id:
            description: Unique integer identifier for the key in the keychain.
            type: int
          passPhrase:
            description: MACsec pre-shared key in cleartext hex. Must be exactly 32 hex digits for `AES_128_CMAC` or 64 hex
              digits for `AES_256_CMAC`.
            type: str
          startTime:
            description: Activation date/time for this key in HH mm ss dd MMM yyyy format (e.g., 00 00 00 09 Apr 2026). Lifetime
              is set to infinite.
            type: str
        type: list
    type: dict
  networkDeviceId:
    description: Network device id of the REP ring member. It is the `instanceUuid` attribute in the response of `/dna/intent/api/v1/networkDevices`
      API.
    type: str
  repSegmentId:
    description: REP segment is a chain of ports connected to each other and configured with a segment ID.
    type: int
  repZtpMsg:
    description: Summary of REP ring members that either do not have REP ZTP supported and those that have REP ZTP supported
      but not enabled.
    type: str
  ringMembers:
    description: Discovered member nodes in the REP ring.
    elements: dict
    suboptions:
      networkDeviceId:
        description: Network device id of the ring member.
        type: str
      nodeName:
        description: Name of the ring member.
        type: str
      portName1:
        description: Interface name of the node.
        type: str
      portName2:
        description: Interface name of the node.
        type: str
      portRepZtpStatus1:
        description: REP ZTP status for Port 1.
        type: str
      portRepZtpStatus2:
        description: REP ZTP status for Port 2.
        type: str
      ringOrder:
        description: Order of the node in the REP ring.
        type: int
    type: list
  ringName:
    description: Unique name of REP ring configured.
    type: str
  rootNeighbourNetworkDeviceIds:
    description: Hostname of the root node neighbor device.
    elements: str
    type: list
  rootNetworkDeviceId:
    description: Root node network device id of the REP ring member. It is the `instanceUuid` attribute in the response of
      `/dna/intent/api/v1/networkDevices` API.
    type: str
  status:
    description: Status of the previous REP ring operation.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Industrial Configuration ConfigureAREPRingOnNONFABRICDeployment
    description: Complete reference of the ConfigureAREPRingOnNONFABRICDeployment API.
    link: https://developer.cisco.com/docs/dna-center/#!configure-arep-ring-on-nonfabric-deployment
notes:
  - SDK Method used are
    industrial_configuration.IndustrialConfiguration.configure_a_rep_ring_on_non_fabric_deployment,
  - Paths used are
    post /dna/intent/api/v1/iot/nonFabric/repRings,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.iot_non_fabric_rep_rings:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    deploymentMode: string
    id: string
    macsecConfig:
      accessControlMode: string
      ciphersuite: string
      encryptionMode: string
      keys:
        - cryptoAlgo: string
          id: 0
          passPhrase: string
          startTime: string
    networkDeviceId: string
    repSegmentId: 0
    repZtpMsg: string
    ringMembers:
      - networkDeviceId: string
        nodeName: string
        portName1: string
        portName2: string
        portRepZtpStatus1: string
        portRepZtpStatus2: string
        ringOrder: 0
    ringName: string
    rootNeighbourNetworkDeviceIds:
      - string
    rootNetworkDeviceId: string
    status: string
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
