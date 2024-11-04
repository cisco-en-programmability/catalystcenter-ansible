#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: snmpv3_credential
short_description: Resource module for Snmpv3 Credential
description:
- Manage operations create and update of the resource Snmpv3 Credential.
- Adds global SNMPv3 credentials.
- Updates global SNMPv3 credential.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  authPassword:
    description: Auth password for SNMPv3. Required if snmpMode is 'AUTHPRIV' or 'AUTHNOPRIV'.
      Use 'NO!$DATA!$' if no change required.
    type: str
  authType:
    description: SNMPv3 auth protocol. 'SHA' or 'MD5'. Required if snmpMode is 'AUTHPRIV'
      or 'AUTHNOPRIV'.
    type: str
  comments:
    description: Comments to identify the SNMPv3 credential.
    type: str
  credentialType:
    description: Credential type to identify the application that uses the SNMPv3 credential.
    type: str
  description:
    description: Description for SNMPv3 Credential.
    type: str
  id:
    description: Id of the SNMPv3 Credential.
    type: str
  instanceTenantId:
    description: Deprecated. This attribute will be removed in a future release, should
      not be used, and any value supplied will be ignored.
    type: str
  instanceUuid:
    description: Deprecated. This attribute will be removed in a future release, should
      not be used, and any value supplied will be ignored.
    type: str
  privacyPassword:
    description: Privacy password for SNMPv3 privacy. Required if snmpMode is 'AUTHPRIV'.
      Use 'NO!$DATA!$' if no change required.
    type: str
  privacyType:
    description: SNMPv3 privacy protocol. Required is snmpMode is 'AUTHPRIV'.
    type: str
  snmpMode:
    description: Mode of SNMPv3. 'AUTHPRIV' or 'AUTHNOPRIV' or 'NOAUTHNOPRIV'.
    type: str
  username:
    description: SNMPv3 username.
    type: str
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Discovery CreateSNMPv3CredentialsV1
  description: Complete reference of the CreateSNMPv3CredentialsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!create-snm-pv-3-credentials-v-1
- name: Cisco CATALYST Center documentation for Discovery UpdateSNMPv3CredentialsV1
  description: Complete reference of the UpdateSNMPv3CredentialsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!update-snm-pv-3-credentials-v-1
notes:
  - SDK Method used are
    discovery.Discovery.create_snmpv3_credentials_v1,
    discovery.Discovery.update_snmpv3_credentials_v1,

  - Paths used are
    post /dna/intent/api/v1/global-credential/snmpv3,
    put /dna/intent/api/v1/global-credential/snmpv3,

"""

EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.snmpv3_credential:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    authPassword: string
    authType: string
    comments: string
    credentialType: string
    description: string
    id: string
    instanceTenantId: string
    instanceUuid: string
    privacyPassword: string
    privacyType: string
    snmpMode: string
    username: string

- name: Create
  cisco.catalystcenter.snmpv3_credential:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    authPassword: string
    authType: string
    comments: string
    credentialType: string
    description: string
    id: string
    instanceTenantId: string
    instanceUuid: string
    privacyPassword: string
    privacyType: string
    snmpMode: string
    username: string

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
