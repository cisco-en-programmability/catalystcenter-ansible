#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sites_device_credentials
short_description: Resource module for Sites Device Credentials
description:
- This module represents an alias of the module sites_device_credentials_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  cliCredentialsId:
    description: Sites Device Credentials's cliCredentialsId.
    suboptions:
      credentialsId:
        description: The `id` of the credentials.
        type: str
    type: dict
  httpReadCredentialsId:
    description: Sites Device Credentials's httpReadCredentialsId.
    suboptions:
      credentialsId:
        description: The `id` of the credentials.
        type: str
    type: dict
  httpWriteCredentialsId:
    description: Sites Device Credentials's httpWriteCredentialsId.
    suboptions:
      credentialsId:
        description: The `id` of the credentials.
        type: str
    type: dict
  id:
    description: Id path parameter. Site Id, retrievable from the `id` attribute in
      `/dna/intent/api/v1/sites`.
    type: str
  snmpv2cReadCredentialsId:
    description: Sites Device Credentials's snmpv2cReadCredentialsId.
    suboptions:
      credentialsId:
        description: The `id` of the credentials.
        type: str
    type: dict
  snmpv2cWriteCredentialsId:
    description: Sites Device Credentials's snmpv2cWriteCredentialsId.
    suboptions:
      credentialsId:
        description: The `id` of the credentials.
        type: str
    type: dict
  snmpv3CredentialsId:
    description: Sites Device Credentials's snmpv3CredentialsId.
    suboptions:
      credentialsId:
        description: The `id` of the credentials.
        type: str
    type: dict
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Network Settings UpdateDeviceCredentialSettingsForASiteV1
  description: Complete reference of the UpdateDeviceCredentialSettingsForASiteV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!update-device-credential-settings-for-a-site
notes:
  - SDK Method used are
    network_settings.NetworkSettings.update_device_credential_settings_for_a_site_v1,

  - Paths used are
    put /dna/intent/api/v1/sites/{id}/deviceCredentials,
  - It should be noted that this module is an alias of sites_device_credentials_v1

"""

EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.sites_device_credentials:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    state: present
    cliCredentialsId:
      credentialsId: string
    httpReadCredentialsId:
      credentialsId: string
    httpWriteCredentialsId:
      credentialsId: string
    id: string
    snmpv2cReadCredentialsId:
      credentialsId: string
    snmpv2cWriteCredentialsId:
      credentialsId: string
    snmpv3CredentialsId:
      credentialsId: string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": {
        "url": "string",
        "taskId": "string"
      }
    }
"""
