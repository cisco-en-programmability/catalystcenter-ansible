#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: snmpv2_read_community_credential
short_description: Resource module for Snmpv2 Read Community Credential
description:
- Manage operations create and update of the resource Snmpv2 Read Community Credential.
- Adds global SNMP read community.
- Updates global SNMP read community.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  comments:
    description: Comments to identify the credential.
    type: str
  credentialType:
    description: Credential type to identify the application that uses the credential.
    type: str
  description:
    description: Name/Description of the credential.
    type: str
  instanceUuid:
    description: Credential UUID.
    type: str
  readCommunity:
    description: SNMP read community. NO!$DATA!$ for no value change.
    type: str
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Discovery CreateSNMPReadCommunityV1
  description: Complete reference of the CreateSNMPReadCommunityV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!create-snmp-read-community-v-1
- name: Cisco CATALYST Center documentation for Discovery UpdateSNMPReadCommunityV1
  description: Complete reference of the UpdateSNMPReadCommunityV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!update-snmp-read-community-v-1
notes:
  - SDK Method used are
    discovery.Discovery.create_snmp_read_community_v1,
    discovery.Discovery.update_snmp_read_community_v1,

  - Paths used are
    post /dna/intent/api/v1/global-credential/snmpv2-read-community,
    put /dna/intent/api/v1/global-credential/snmpv2-read-community,

"""

EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.snmpv2_read_community_credential:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    comments: string
    credentialType: string
    description: string
    instanceUuid: string
    readCommunity: string

- name: Create
  cisco.catalystcenter.snmpv2_read_community_credential:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    comments: string
    credentialType: string
    description: string
    readCommunity: string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
