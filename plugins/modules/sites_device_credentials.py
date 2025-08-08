#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sites_device_credentials
short_description: Resource module for Sites Device
  Credentials
description:
  - Manage operation update of the resource Sites Device
    Credentials. - > Updates device credential settings
    for a site; `null` values indicate that the setting
    will be inherited from the parent site; empty objects
    `{}` indicate that the credential is unset, and
    that no credential of that type will be used for
    the site.
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
    description: Id path parameter. Site Id, retrievable
      from the `id` attribute in `/dna/intent/api/v1/sites`.
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
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Network
      Settings UpdateDeviceCredentialSettingsForASite
    description: Complete reference of the UpdateDeviceCredentialSettingsForASite
      API.
    link: https://developer.cisco.com/docs/dna-center/#!update-device-credential-settings-for-a-site
notes:
  - SDK Method used are
    network_settings.NetworkSettings.update_device_credential_settings_for_a_site,
  - Paths used are
    put /dna/intent/api/v1/sites/{id}/deviceCredentials,
"""

EXAMPLES = r"""
---
- name: Update all
  cisco.catalystcenter.sites_device_credentials:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
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
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
