#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sites_device_credentials_apply
short_description: Resource module for Sites Device
  Credentials Apply
description:
  - Manage operation create of the resource Sites Device
    Credentials Apply. - > When sync is triggered at
    a site with the credential that are associated to
    the same site, network devices in impacted sites
    child sites which are inheriting the credential
    get managed in inventory with the associated site
    credential. Credential gets configured on network
    devices before these get managed in inventory. Please
    make a note that cli credential wouldn't be configured
    on AAA authenticated devices but they just get managed
    with the associated site cli credential.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  deviceCredentialId:
    description: It must be cli/snmpV2Read/snmpV2Write/snmpV3
      Id.
    type: str
  siteId:
    description: Site Id.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Network
      Settings SyncNetworkDevicesCredential
    description: Complete reference of the SyncNetworkDevicesCredential
      API.
    link: https://developer.cisco.com/docs/dna-center/#!sync-network-devices-credential
notes:
  - SDK Method used are
    network_settings.NetworkSettings.sync_network_devices_credential,
  - Paths used are
    post /dna/intent/api/v1/sites/deviceCredentials/apply,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.sites_device_credentials_apply:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    deviceCredentialId: string
    siteId: string
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
