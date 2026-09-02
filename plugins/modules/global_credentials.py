#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: global_credentials
short_description: Resource module for Global Credentials
description:
  - Manage operations create, update and delete of the resource Global Credentials.
  - API to add new global credential.
  - API to delete global credential by the given identifier.
  - API to update the global credential by the given identifier.
version_added: '2.3.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  authPassword:
    description: Authentication password for SNMP. Required if the authentication type is specified. Passwords must contain
      minimum 8 characters and cannot contain spaces or angle brackets(<>). For wireless devices password of length 12 to
      31 characters is required.
    type: str
  authType:
    description: SNMP authentication type. Required if the SNMP security mode is `AUTHPRIV` or `AUTHNOPRIV`. | SNMP authentication
      type| Description | |----------------------|-------------| |`SHA` | The device will be authenticated using SHA. | |`MD5`
      | The device will be authenticated using MD5.| |`SHA256` | The device will be authenticated using SHA256.|.
    type: str
  description:
    description: Description for NETCONF credential.
    type: str
  enablePassword:
    description: CLI Enable Password. Passwords cannot contain spaces or angle brackets(<>).
    type: str
  id:
    description: Id path parameter. Unique identifier of the global credential.
    type: str
  mode:
    description: Security level that an SNMP message requires. | Mode| Description | |----------------------|-------------|
      |`AUTHPRIV` | The device will be authenticated using security mode AUTHPRIV. | |`AUTHNOPRIV` | The device will be authenticated
      using security mode AUTHNOPRIV.| |`NOAUTHNOPRIV` | The device will be authenticated using security mode NOAUTHNOPRIV.|.
    type: str
  password:
    description: HTTP(S) write password. Passwords cannot contain spaces or angle brackets(<>).
    type: str
  port:
    description: NETCONF port of the device.
    type: str
  privacyPassword:
    description: SNMP privacy password. Required if the privacy type is specified. Passwords must contain minimum 8 characters
      and cannot contain spaces or angle brackets(<>). For wireless devices password of length 12 to 31 characters is required.
    type: str
  privacyType:
    description: SNMP privacy type. Required if the SNMP mode is `AUTHPRIV`. | SNMP privacy type | Description | |------------------------------|--------------|
      | `AES128` | AES128 algorithm used for encryption. | | `AES192`| AES192 algorithm used for encryption. | | `AES256`
      | AES256 algorithm used for encryption.| | `CISCOAES192` | CISCOAES192 algorithm used for encryption.| | `CISCOAES256`
      | CISCOAES256 algorithm used for encryption.|.
    type: str
  protocol:
    description: HTTP protocol. Compute device require HTTPS.
    type: str
  readCommunity:
    description: Read-only community string password used to view SNMP information on the device. Passwords cannot contain
      spaces or angle brackets(<>).
    type: str
  type:
    description: Type of the credential. This attribute should not be provided as part of PUT API call, as `type` cannot be
      updated for credential.
    type: str
  username:
    description: HTTP(S) write username.
    type: str
  writeCommunity:
    description: Read-write community string used to read and write SNMP information. Passwords cannot contain spaces or angle
      brackets(<>).
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Network Settings AddsNewGlobalCredential
    description: Complete reference of the AddsNewGlobalCredential API.
    link: https://developer.cisco.com/docs/dna-center/#!adds-new-global-credential
  - name: Cisco Catalyst Center documentation for Network Settings DeleteGlobalCredentialByTheGivenIdentifier
    description: Complete reference of the DeleteGlobalCredentialByTheGivenIdentifier API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-global-credential-by-the-given-identifier
  - name: Cisco Catalyst Center documentation for Network Settings UpdateGlobalCredentialByTheGivenIdentifer
    description: Complete reference of the UpdateGlobalCredentialByTheGivenIdentifer API.
    link: https://developer.cisco.com/docs/dna-center/#!update-global-credential-by-the-given-identifer
notes:
  - SDK Method used are
    network_settings.NetworkSettings.adds_new_global_credential,
    network_settings.NetworkSettings.delete_global_credential_by_the_given_identifier,
    network_settings.NetworkSettings.update_global_credential_by_the_given_identifer,
  - Paths used are
    post /dna/intent/api/v1/globalCredentials,
    delete /dna/intent/api/v1/globalCredentials/{id},
    put /dna/intent/api/v1/globalCredentials/{id},
"""

EXAMPLES = r"""
---
- name: Delete by id
  cisco.catalystcenter.global_credentials:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: 3fa85f64-5717-4562-b3fc-2c963f66afa6
- name: Update by id
  cisco.catalystcenter.global_credentials:
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
    description: string
    enablePassword: string
    id: string
    mode: string
    password: string
    port: string
    privacyPassword: string
    privacyType: string
    protocol: string
    readCommunity: string
    type: string
    username: string
    writeCommunity: string
- name: Create
  cisco.catalystcenter.global_credentials:
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
    description: string
    enablePassword: string
    id: string
    mode: string
    password: string
    port: string
    privacyPassword: string
    privacyType: string
    protocol: string
    readCommunity: string
    type: string
    username: string
    writeCommunity: string
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
