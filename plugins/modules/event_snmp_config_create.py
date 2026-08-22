#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_snmp_config_create
short_description: Resource module for Event Snmp Config Create
description:
  - Manage operation create of the resource Event Snmp Config Create.
  - Create SNMP Destination.
version_added: '2.3.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  authPassword:
    description: Event Snmp Config Create's authPassword.
    type: str
  community:
    description: Required only if snmpVersion is V2C.
    type: str
  description:
    description: Event Snmp Config Create's description.
    type: str
  ipAddress:
    description: Event Snmp Config Create's ipAddress.
    type: str
  name:
    description: Event Snmp Config Create's name.
    type: str
  port:
    description: Event Snmp Config Create's port.
    type: str
  privacyPassword:
    description: Event Snmp Config Create's privacyPassword.
    type: str
  snmpAuthType:
    description: Event Snmp Config Create's snmpAuthType.
    type: str
  snmpMode:
    description: If snmpVersion is V3 it is required and cannot be NONE.
    type: str
  snmpPrivacyType:
    description: Event Snmp Config Create's snmpPrivacyType.
    type: str
  snmpVersion:
    description: Event Snmp Config Create's snmpVersion.
    type: str
  userName:
    description: Required only if snmpVersion is V3.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Event Management CreateSNMPDestination
    description: Complete reference of the CreateSNMPDestination API.
    link: https://developer.cisco.com/docs/dna-center/#!create-snmp-destination
notes:
  - SDK Method used are
    event_management.EventManagement.create_snmp_destination,
  - Paths used are
    post /dna/intent/api/v1/event/snmp-config,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.event_snmp_config_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    authPassword: string
    community: string
    description: string
    ipAddress: string
    name: string
    port: string
    privacyPassword: string
    snmpAuthType: string
    snmpMode: string
    snmpPrivacyType: string
    snmpVersion: string
    userName: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "errorMessage": {
        "errors": []
      },
      "apiStatus": "string",
      "statusMessage": "string"
    }
"""
